from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from flask_table import Table, Col
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db, get_db2
import re

#import pandas

import glob
import os

# Declare your table
class ItemTable(Table):
    col1 = Col('Non-discriminative barcode')
    col2 = Col('Reference')
    col3 = Col(' Odd reference')
    
    
# Get some objects
class Item(object):
    def __init__(self, col1, col2, col3):
        self.col1 = col1
        self.col2 = col2
        self.col3 = col3
        

bp = Blueprint('analize',__name__)

@bp.route('/')
@login_required
def index():
    db = get_db2()
    items = db.execute(
        'SELECT * FROM database'
    ).fetchall()
    
    items = modify_items(items)
    
    return render_template('analize/index.html',items=items)

    

kym='flaskr/static/images/kymograph/1.6x_Gpos_Fragment_21-ZVI Export-21_molecule_1_kymograph.tif'

@bp.route('/', methods=('GET', 'POST'))
@login_required
def compare():
	if request.method == 'POST':
		try:
			ipt = request.form['myinput']
			ipt2 = request.form['myinput2']
			ipt3 = request.form['myinput3']
			ipt4 = request.form['generate']
		except:
			return generate()
		

	img = get_img(ipt)
	# throw exception if the file is not found
	try:
		url = get_url_in_fold(ipt)
	except:
		url = ''
		# /static/images/x1_6x_DA62688_Fragment_21_ZVIExport_21_molecule_1_kymograph_tif.png
		
	try:
		kymo,csv = get_file_in_fold(ipt)
	except:
		kymo = ''
		csv = ''
		
	items = [Item(ipt,ipt2,ipt3)]
	table = ItemTable(items)
	table.border = True
		
	return render_template('analize/compare.html',ipt=ipt,ipt2=ipt2,ipt3=ipt3,url=url,kymo=kymo,csv=csv, table=table)


@bp.route('/generate')
@login_required
def generate():
	return render_template('analize/generate.html')

 
def modify_items(items):
	for i in range(0,len(items)):
		elt = items[i]
		lst = list(elt)
		vals = re.split('ZVIExport_',lst[1])
		vals2 = re.split('_kym',vals[1])
		lst[1] = vals[0]+vals2[0]
		items[i]= tuple(lst)
	return items

def get_file_in_fold(ipt):
	for file in os.listdir('flaskr/static/images/kymograph'):
		if file.endswith(".tif"):
			vals = re.split('ZVI Export-',file)
			vals2 = re.split('_kym',vals[1])
			vv = vals[0]+vals2[0]
			vv = vv.replace(',','_')
			vv = vv.replace('.','_')
			vv = vv.replace('-','_')
			if vv in ipt: 
				kymo = os.path.join("/static/images/kymograph", file)
				csv = os.path.join("/static/images/csv", file.replace('.tif','.csv'))
	return kymo, csv
	
def get_url_in_fold(ipt):
	for file in os.listdir('flaskr/static/images'):
		if file.endswith(".png"):
			vals = re.split('ZVIExport_',file)
			vals2 = re.split('_kym',vals[1])
			vv = vals[0]+vals2[0]
			if vv in ipt: 
				url = os.path.join("/static/images", file)
	return url
        

	
		
def get_img(ipt):
	img = []
	return img
	


	
