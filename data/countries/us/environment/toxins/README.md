## Toxins

Data notes.

<br>

### Chemicals

Note, according to the EPA  [TRI_CHEM_ID](https://enviro.epa.gov/enviro/EF_METADATA_HTML.tri_page?p_column_name=TRI_CHEM_ID) notes, a TRI_CHEM_ID is 9 characters long (if the TRI_CHEM_ID is a formatted Chemical Abstract Service Registry (CAS) number).  However, within the [TRI_CHEM_INFO](https://enviro.epa.gov/enviro/ef_metadata_html.ef_metadata_table?p_table_name=tri_chem_info&p_topic=tri) data set, such TRI_CHEM_ID strings have 10 characters; an extra zero character is prepended.  Herein, [chemicalsEnvirofacts.csv](./chemicalsEnvirofacts.csv).

Additionally, the chemical identification codes are not formatted within the [Latest TRI-Listed Chemicals](https://www.epa.gov/toxics-release-inventory-tri-program/tri-listed-chemicals) data files. The excerpt herein is [R2020.csv](./R2020.csv).


<br>

### Releases Sites

The TRI Explorer option; for details missing in the much more straightforward [TRI Model](https://www.epa.gov/enviro/tri-reported-chemical-information-subject-area-model)

* https://enviro.epa.gov/triexplorer/tri_release.facility

The fields available and their descriptions

* [offsite](./sites/offsite.csv)
* [onsite](./sites/onsite.csv)
* [all](./sites/all.csv); previously named toxins

<br>

### Summaries of Releases

Summaries by state are stored in [data.zip](./releases/data.zip).  The field types, and more, of each file in data.zip, are outlined in [attributes.csv](./releases/attributes.csv)
