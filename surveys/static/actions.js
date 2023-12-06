surveyEditForm = document.getElementById("survey-edit-form");
surveyEditFormControl = document.getElementById("control-survey-edit-form");

surveyEditFormControl.addEventListener("click", showSurveyEditForm);

function showSurveyEditForm() {
  
  if (surveyEditForm.style.display == "none" ) {
    surveyEditForm.style.display = "block";
    surveyEditFormControl.classList.remove("btn-outline-primary");
    surveyEditFormControl.classList.add("btn-outline-secondary");
  } else {
    surveyEditForm.style.display = "none";
    surveyEditFormControl.classList.remove("btn-outline-secondary");
    surveyEditFormControl.classList.add("btn-outline-primary");
  }
}