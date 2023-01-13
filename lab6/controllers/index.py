from app import app
from flask import render_template, request
import constants


@app.route('/', methods=['GET'])
def index():
    name = request.values.get('username')
    gender = request.values.get('gender')
    program_id = request.values.get('program')
    subject_id = request.values.getlist('subject[]')
    subjects_select = [constants.subjects[int(i)] for i in subject_id]
    olympiad_id = request.values.getlist('olympiad[]')
    olympiads_select = [constants.olympiads[int(i)] for i in olympiad_id]
    req=request.values.get('req')
    html = render_template(
        'index.html',
        req=req,
        name=name,
        gender=gender,
        program=constants.programs[int(program_id)] if program_id else 0,
        program_list=constants.programs,
        len=len,
        subjects_select=subjects_select,
        subject_list=constants.subjects,
        olympiad_list=constants.olympiads,
        olympiads_select=olympiads_select
    )
    # html = render_template(
    #     'index.html',
    #     program_list=constants.programs,
    #     subject_list=constants.subjects,
    #     olympiad_list=constants.olympiads,
    #     len=len
    # )
    return html
