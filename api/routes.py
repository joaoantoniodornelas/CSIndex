# -*- coding: utf-8 -*-

from flask import Flask, make_response, render_template, request
from functions import *

app = Flask(__name__)

##############- Publications section - ###################
@app.route('/publications')
def publicationsSection():
	conferenceName  = request.args.get('conferenceName', None)
	areaName  = request.args.get('areaName', None)

	if areaName is not None:
		if conferenceName is not None:
			#Número de publicações em uma determinada conferência de uma área
			return num_publications_by_conference_in_area(areaName, conferenceName)
		else:
			#Número de publicações no conjunto de conferências de uma área
			return num_publications_by_area(areaName)
	else:
		return "Erro: Por favor, especifique uma área", 412
   

##############- Score section - ###################
@app.route('/scores')
def scoreSection():
	departmentName  = request.args.get('departmentName', None)
	areaName  = request.args.get('areaName', None)

	if areaName is not None:
		if departmentName is not None:
			#Score de um determinado departamento em uma área.
			return department_score(areaName, departmentName)
		else:
			# #Scores de todos os departamentos em uma área
			return department_scores(areaName)
	else:
		return "Erro: Por favor, especifique uma área", 412


##############- Teachers section - ###################
@app.route('/teachers')
def teachersSection():
	departmentName  = request.args.get('departmentName', None)
	areaName  = request.args.get('areaName', None)

	if areaName is not None:
		if departmentName is not None:
			#Número de professores de um determinado departamento que publicam em uma área
			return num_teachers_in_department_by_area(areaName, departmentName)
		else:
			#Número de professores que publicam em uma determinada área (organizados por departamentos)
			return num_teachers_by_area(areaName)
	else:
		return "Erro: Por favor, especifique uma área", 412

##############- Papers section - ###################
@app.route('/papers')
def papersSection():
	departmentName  = request.args.get('departmentName', None)
	areaName  = request.args.get('areaName', None)
	year = request.args.get('year', None)
	teacherName = request.args.get('teacherName', None)

	if areaName is not None:
		if departmentName is not None:
			#Todos os papers de um departamento em uma área
			return papers_by_department_in_area(areaName, departmentName)
		elif year is not None:
			#Todos os papers de uma área em um determinado ano
			return papers_by_area_in_year(areaName, year)
		else:
			#Todos os papers de uma área (ano, título, deptos e autores)
			return papers_by_area(areaName)
	elif teacherName is not None:
		#Todos os papers de um professor (dado o seu nome)
		return papers_by_teacher(teacherName)
	else:
		return "Erro: Por favor, especifique uma área", 412

app.run()