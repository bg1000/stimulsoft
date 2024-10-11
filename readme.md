## Purpose
This repo contains a Django project that replicates a Stimulsoft reporting error for tech support ticket # 3184379.

## Instructions

#### Installing
Note:  A python virtual environment is recommended (not shown).

```
git clone git@github.com:bg1000/stimulsoft.git
pip install -r requirements.txt
python manage.py runserver

```

#### Viewing Report
Browse to: http://localhost:8000/report/

#### Code
The project root the code is on ``` ./reports/views.py ```

There is a view that returns the report (report_view) and a view that returns the report data (report_data).  You will see in the comments that one of two lines needed to commented out for the report to run.