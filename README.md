
# QGIS Pluging Italy Inspire Cadastral Downloader (IICD)

QGIS Plugin for downloading and visualizing Italian cadastral data according to INSPIRE directly in QGIS

The Italy Inspire Cadastral Downloader QGIS plugin is designed to facilitate the download of municipal cadastral data in Italy, optimizing access to key information for spatial analysis and territorial management.

The download process uses a REST API developed by Geoinnova, which retrieves Italian cadastral data available for download from the [Repertorio Nazionale dei Dati Territoriali (RNDT)](https://geodati.gov.it/geoportale/visualizzazione-metadati/scheda-metadati/?uuid=age:S_0000_ITALIA), the official repository of geospatial data in Italy.

The data is provided under the [Creative Commons Attribution 4.0 (CC-BY 4.0) license](https://geodati.gov.it/geoportale/notizie/376-cartografia-catastale-nuova-licenza-per-la-consultazione/), allowing its use, distribution, and modification, provided that the original source is credited.

This cadastral data is updated every six months, ensuring that the information remains as accurate and up-to-date as possible.

The downloaded GML cadastral layers (CadastralParcel and CadastralZoning) enable tasks related to territorial planning, urban management, and serve as a base for any project requiring this reference cartography.

- Languages: English, Italian
- QGIS Version: QGIS v3.* or higher
- GitHub Repository: https://github.com/geoinnova/italy_inspire_cadastre_downloader
- Bugs & Improvements: https://github.com/geoinnova/italy_inspire_cadastre_downloader