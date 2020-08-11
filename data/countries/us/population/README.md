### U.S.A. Populations Data

<br>

### Details

<dl>
  <dt>States</dt>
  <dd>The states.csv file is based on <a href="http://www2.census.gov/programs-surveys/popest/datasets/2010-2019/national/totals/nst-est2019-alldata.csv?#">nst-est2019-alldata.csv</a>; a copy of the file is available <a href="nst-est2019-alldata.csv">in this repository</a>.</dd>

  <dt>Counties</dt>
  <dd>The data of counties.csv was extracted from  <a href="https://www.census.gov/data/developers/guidance/api-user-guide.html">api.census.gov</a>; more notes within the counties section below.</dd>

  <dt>Territories</dt>
  <dd>The content of the territories.csv is courtesy of CIA Factbook; the source field in the file encodes the link to a data's source.</dd>
</dl>

<br>

### Counties

County level population data is available via reference files or an API.  The reference file per state is available via the [Census Bureau](https://www2.census.gov/programs-surveys/popest/datasets/2010-2019/counties/asrh/).  The URL of a state's counties data is

```python
url = 'https://www2.census.gov/programs-surveys/popest/datasets/2010-2019/counties/asrh/cc-est2019-alldata-{STATEFP}.csv'
```

wherein `STATEFP` should be replaced with a `STATEFP`.  The <a href="https://www.census.gov/data/developers/guidance/api-user-guide.html">api.census.gov</a> approach is

```
api = 'https://api.census.gov/data/2019/pep/population?get=POP,NAME&for=county:*&in=state:{statefp}&key={entry}'
```

wherein `entry` is the API key.  Visit [Google Colaboratory](https://colab.research.google.com/drive/1ko7PLgVpuXuKjkI81fx5T79cpvCBvzQg)

<br>

### References

* [Population Estimates API](https://www.census.gov/data/developers/data-sets/popest-popproj/popest.html?#)
* [State Population Totals](https://www.census.gov/data/tables/time-series/demo/popest/2010s-state-total.html)

* **nst-est2019-alldata.csv**: http://www2.census.gov/programs-surveys/popest/datasets/2010-2019/national/totals/nst-est2019-alldata.csv
* **SCPRC-EST2019-18+POP-RES.csv**: https://www2.census.gov/programs-surveys/popest/datasets/2010-2019/state/detail/SCPRC-EST2019-18+POP-RES.csv