# Survey app
A survey app created with Django. In this website users can create surveys and get insights from the answers.

![app overview](https://github.com/cr1deg0/survey_app/assets/86016298/38d6900b-d52d-443c-a33f-54bca1ae105f)

Users can:

- Sign up/ Sign in to the website
- Create their own surveys adding as many questions and answers as required
- Generate a page with the survey and share the link to the survey
- Analyse surveys results. See what percentage and total number of people answered each question

# App design

The app is built with Django and Djando Guardian (for object level user permissions). Styling is implemented with Bootstrap.
The graphs in the survey results page are implemented with graph.js.

Customer journey and high level app design.

![app design](https://github.com/cr1deg0/survey_app/assets/86016298/a2c59830-8d21-4b09-ad45-d402044798d7)

# Data model

<img width="1077" alt="Model design" src="https://github.com/cr1deg0/survey_app/assets/86016298/c0969160-d8ee-4443-80b7-66e805fb4d02">

# Improvement features

- Make question and option addition more dynamic with javascript

# Learnings

- Creating a high level design of the app, user journey and database model as a first step helped me to have a clear plan and coding sequence, reducing refactorings.
- Using class based views.
- Use of Django Guardian for object level permission.
- Use of formsets and inline formsets.
- Use of json_script tag in the template to safely output data for use with chart.js.

# Acknowledgments

This idea to create this app comes from Matt Segal's [blogpost](https://mattsegal.dev/django-survey-project.html).
