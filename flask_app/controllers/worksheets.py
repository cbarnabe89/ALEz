from flask import Flask, render_template,request, redirect, session, flash
from flask_app import app
from flask_app.models.worksheet import Worksheet
from flask_app.models.user import User

#new worksheet
@app.route('/new/worksheet')
def new_worksheet():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template('new_worksheet.html' ,user=User.get_by_id(data))

#post new worksheet
@app.route('/worksheet/create',methods=['POST'])
def create_worksheet():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Worksheet.validate_worksheet(request.form):
        return redirect('/new/worksheet')
    data = {
        "claim_number": request.form["claim_number"],
        "date_of_loss": request.form["date_of_loss"],
        "normal_housing": request.form["normal_housing"],
        "normal_utilities_heat": request.form["normal_utilities_heat"],
        "normal_utilities_electricity": request.form["normal_utilities_electricity"],
        "normal_utilities_water": request.form["normal_utilities_water"],
        "normal_food_residence": request.form["normal_food_residence"],
        "normal_food_restaurant": request.form["normal_food_restaurant"],
        "normal_food_other": request.form["normal_food_other"],
        "normal_services_laundry": request.form["normal_services_laundry"],
        "normal_services_dry_cleaning": request.form["normal_services_dry_cleaning"],
        "normal_services_other": request.form["normal_services_other"],
        "normal_transportation_gas": request.form["normal_transportation_gas"],
        "normal_transportation_taxi": request.form["normal_transportation_taxi"],
        "normal_transportation_rideshare": request.form["normal_transportation_rideshare"],
        "normal_storage_unit": request.form["normal_storage_unit"],
        "normal_storage_moving": request.form["normal_storage_moving"],
        "normal_storage_other": request.form["normal_storage_other"],
        "total_NLE": request.form["total_NLE"],
        "addtl_housing": request.form["addtl_housing"],
        "addtl_utilities_heat": request.form["addtl_utilities_heat"],
        "addtl_utilities_electricity": request.form["addtl_utilities_electricity"],
        "addtl_utilities_water": request.form["addtl_utilities_water"],
        "addtl_food_residence": request.form["addtl_food_residence"],
        "addtl_food_restaurant": request.form["addtl_food_restaurant"],
        "addtl_food_other": request.form["addtl_food_other"],
        "addtl_services_laundry": request.form["addtl_services_laundry"],
        "addtl_services_dry_cleaning": request.form["addtl_services_dry_cleaning"],
        "addtl_services_other": request.form["addtl_services_other"],
        "addtl_transportation_gas": request.form["addtl_transportation_gas"],
        "addtl_transportation_taxi": request.form["addtl_transportation_taxi"],
        "addtl_transportation_rideshare": request.form["addtl_transportation_rideshare"],
        "addtl_storage_unit": request.form["addtl_storage_unit"],
        "addtl_storage_moving": request.form["addtl_storage_moving"],
        "addtl_storage_other": request.form["addtl_storage_other"],
        "total_AE": request.form["total_AE"],
        "total_ALE_claim": request.form["total_ALE_claim"],
        "user_id": session["user_id"]
    }
    Worksheet.save(data)
    return redirect('/dashboard')

#edit worksheet
@app.route('/edit/worksheet/<int:id>')
def edit_worksheet(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("edit_worksheet.html",edit=Worksheet.get_one(data),user=User.get_by_id(user_data))

#edit worksheet POST
@app.route('/update/worksheet',methods=['POST'])
def update_worksheet():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Worksheet.validate_worksheet(request.form):
        return redirect(request.referrer)
    data = {
        "claim_number": request.form["claim_number"],
        "date_of_loss": request.form["date_of_loss"],
        "normal_housing": request.form["normal_housing"],
        "normal_utilities_heat": request.form["normal_utilities_heat"],
        "normal_utilities_electricity": request.form["normal_utilities_electricity"],
        "normal_utilities_water": request.form["normal_utilities_water"],
        "normal_food_residence": request.form["normal_food_residence"],
        "normal_food_restaurant": request.form["normal_food_restaurant"],
        "normal_food_other": request.form["normal_food_other"],
        "normal_services_laundry": request.form["normal_services_laundry"],
        "normal_services_dry_cleaning": request.form["normal_services_dry_cleaning"],
        "normal_services_other": request.form["normal_services_other"],
        "normal_transportation_gas": request.form["normal_transportation_gas"],
        "normal_transportation_taxi": request.form["normal_transportation_taxi"],
        "normal_transportation_rideshare": request.form["normal_transportation_rideshare"],
        "normal_storage_unit": request.form["normal_storage_unit"],
        "normal_storage_moving": request.form["normal_storage_moving"],
        "normal_storage_other": request.form["normal_storage_other"],
        "total_NLE": request.form["total_NLE"],
        "addtl_housing": request.form["addtl_housing"],
        "addtl_utilities_heat": request.form["addtl_utilities_heat"],
        "addtl_utilities_electricity": request.form["addtl_utilities_electricity"],
        "addtl_utilities_water": request.form["addtl_utilities_water"],
        "addtl_food_residence": request.form["addtl_food_residence"],
        "addtl_food_restaurant": request.form["addtl_food_restaurant"],
        "addtl_food_other": request.form["addtl_food_other"],
        "addtl_services_laundry": request.form["addtl_services_laundry"],
        "addtl_services_dry_cleaning": request.form["addtl_services_dry_cleaning"],
        "addtl_services_other": request.form["addtl_services_other"],
        "addtl_transportation_gas": request.form["addtl_transportation_gas"],
        "addtl_transportation_taxi": request.form["addtl_transportation_taxi"],
        "addtl_transportation_rideshare": request.form["addtl_transportation_rideshare"],
        "addtl_storage_unit": request.form["addtl_storage_unit"],
        "addtl_storage_moving": request.form["addtl_storage_moving"],
        "addtl_storage_other": request.form["addtl_storage_other"],
        "total_AE": request.form["total_AE"],
        "total_ALE_claim": request.form["total_ALE_claim"],
        "id": request.form['id']
    }
    Worksheet.update(data)
    return redirect('/dashboard')

#show worksheet
@app.route('/worksheet/<int:id>')
def show_worksheet(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("show_worksheet.html",worksheet=Worksheet.get_one(data))

#destroy worksheet
@app.route('/destroy/worksheet/<int:id>')
def destroy_worksheet(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Worksheet.destroy(data)
    return redirect('/dashboard')