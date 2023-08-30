# Collection of scripts used for a Master's thesis in digital humanities
## TITLE: 
### « Seuls les petits corpus ont le secret des petits corpus » – Explorative, Automated Analysis and Presentation of the Correspondence of French Writer Constance de Salm (1767–1845) in a Semantic Web Approach
The significance of research data is steadily increasing. Their analysis and re-use enable new scientific insights. Alongside large-scale digitisation projects and the interest in big data, small and medium-sized research institutions have also launched digitisation and indexing projects. Just a few years ago, there were no standards for such projects. Data were often created in accordance with specific research questions and the wishes of researchers – and are therefore not available in a standardised form. Today, the necessary standards are being established by research data infrastructure initiatives such as NFDI. Questions such as “How can data – regardless of size – be standardised and thus saved from ending up in the data graveyard?”, “How can data be made accessible and opened up for new research questions?” are becoming common in the research community and affect researchers regardless of their discipline. This thesis aims to explore the potential of transforming an existing data basis into a standardised linked open data model using the Semantic Web, ontologies and knowledge graphs. In addition, a new exploratory search option for the correspondence in the form of an interactive knowledge graph visualisation intends to enable renewed access to the data. Drawing on the limitations of the resulting user interface and visualisation, the project also outlines potential future research and improvements
____

#### Semantic enrichment of ontology / RDF data
In order to build an ontology for the Constance de Salm correspondence, I converted the available metadata files that were provided by Dr. Mareike König and her project team (2019) on Zenodo from the proprietary format Excel to CSV n order to guarantee a greater number of future uses. According to the 5-star LOD model by Berners-Lee (2006), converting data from a structured, machine-readable format like XLSX to a non-proprietary, structured format like CSV adds a third star to linked data. Transforming the data into RDF is the next step.
So, I filtered the XLSX spreadsheet in accordance to thedr specifications, kept only letters (originals and copies) that were written by Constance de Salm as sender- Then, I extracted and added the year and decade of each letter to a new column in the spreadsheet. This is the pivotal data that later flowed into the KG.
Moreover, I created a baseline ontology for the correspondence. Ontologies are an immanent part of all cycles of linked data production and consumption. The ontology re-uses existing vocabularies like FOAF and RDFS and complies with basic ideas of describing correspondences (i.e. collections of (historical) letters) in an ontology as proposed by, for example, Hyvönent al. (2023), Cristofaro and Spampinato (2021) or Dumont (2019).
I also added results from text mining to the knowledge graph (keyword extraction and sentiment analysis). For this; I followed a tutorial by Kaewnoparat (2023). For the sentiment analysis, I used Textblob for French (Loria, 2018), as well as the DistilCamemBERT model (Delestre & Amar, 2022).

The following figure shows the core concepts of the ontology:

![ontology](https://github.com/sarahondraszek/ma_thesis_cds_ondraszek_2023/assets/69308007/7d1cd1fc-2845-40b0-97b2-1e1bdf1075ce)

To do all this, I used different scripts that are featured in [this folder](src/) and my other [project-related repository](https://github.com/sarahondraszek/stage_IHA_cds/tree/main/code).

#### Visualisations for website / Master's thesis 

I built the visualisation for the knowledge graph in JavaScript, using D3.js and Github user eisman's [<em>neo4jd3</em>](https://github.com/eisman/neo4jd3) tool. For this, I imported the RDF/XML file into Neo4j and then requested the appropriate D3.js JSON format via a REST API call to the local server. In Neo4j, the graph looks the following:

![neo4j](https://github.com/sarahondraszek/ma_thesis_cds_ondraszek_2023/assets/69308007/c604ff32-9f99-42a7-aa72-bbf30716e956)

Through the previously mentioned visualisation tool for JavaScript, I was able to add a customised, interactive knowledge graph to the final website, which I implemented using HTML, CSS and JavaScript (using a Bootstrap template). The corresponding scripts can be found in a different [repository](https://github.com/wissen-vernetzen/wissen-vernetzen.github.io) that I created for the website deployment. [This file](https://github.com/wissen-vernetzen/wissen-vernetzen.github.io/blob/master/index.html) encompasses the embedding of the visualisation on the website, as well as the implementation of the keyword search in the graph.

![website](https://github.com/sarahondraszek/ma_thesis_cds_ondraszek_2023/assets/69308007/638d6a2a-4b6b-4502-b895-6e5fc6916270)

For further information about where to find the different files and data dump, please see the listing below. 

____

#### Data

##### Ontology / RDF dump
[Baseline ontology](data/ontology_baseline/)
[Extended ontology](data/ontology_extended/)
##### Transcriptions
[Letter transcriptions](data/transcriptions/)
##### JSON files / tables 
[Visualisation baseline files](data/visualisation_bases/)
##### Visualisations
[Charts](https://github.com/wissen-vernetzen/wissen-vernetzen.github.io/blob/master/index.html)


#### References

Berners-Lee, T. (2006, July). Linked Data. Retrieved December 14, 2022, from https://www.w3.org/DesignIssues/LinkedData.html </br>

Cristofaro, S., & Spampinato, D. (2021). OntoBelliniLetters: A formal ontology for a corpus of letters of Vincenzo Bellini. In E. Garoufallou & M.-A. Ovalle- Perandones (Eds.), Metadata and Semantic Research (pp. 192–203). Springer International Publishing. </br>

Delestre, C., & Amar, A. (2022). DistilCamemBERT : une distillation du modèle français CamemBERT. CAp (Conférence sur l’Apprentissage automatique). https://hal.archives-ouvertes.fr/hal-03674695 </br>

Dumont, S. (2019). Briefe kommentieren im Semantic Web. DARIAH-DE Working Papers. </br>

Hyvönen, E., Leskinen, P., & Tuominen, J. (2023). Lettersampo–historical letters on the semantic web: A framework and its application to publishing and using epistolary data. J. Comput. Cult. Herit., 16 (1). https://doi.org/10.1145/3569372 </br>

Kaewnoparat, K. (2023). Text summarization and keyword extraction from customer reviews in french. https://developer.ibm.com/articles/ba-data-becomes-knowledge-1/ </br>

König, M., & Peyronnet-Dryden, F. d. (2019). Die Korrespondenz der Constance de Salm (1767-1845) (C. Burgdorff, Trans.). Retrieved April 24, 2023, from https://constance-de-salm.de/ </br>

Loria, S. (2018). Textblob documentation. Release 0.15, 2. </br>
