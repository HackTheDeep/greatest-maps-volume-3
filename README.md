# Greatest-Maps-Volume-3

Map the collections challenge

Data Cleansing and Transformation 

ETL Operations (Extract, Transform, Load) Used To 
Process, Reformat, And Map Real Data To Database

#### About

Given a group of stored records describing Genera, and Species collections,
with a wide amount of columns, We need to pre and post process the data as
part of an ETL pipeline to help structure the data in a usable fashion.

Solving such problems as duplicate columns, incorrect spellings, redundant
data, and the taxonomy of collection information.


#### Process

Process was to tackle the data in several ways to help understand and
enhance the data.

Tools included Postgresql, Python, and Elasticsearch.

Elasticsearch helps in multiple ways. Some of the structured data is helpful
denormalized, and performing a full text search helps us narrow down the scope
of the records.

Some of the data has 6 columns per field name of iterations.  We can break this
down into a single search field with an array, and then apply analyzers to make
our searches more robust.

Analyzers considered were edgengram, pluralizers, and a custom taxonomy corpus
of words to match against.

We can also use this data to format to and from date type fields by indexing
multiple formats at once.

Kibana also provide us a quick and easy access view into the data and perform
some base level analyzics.

The Python Fuzzy Wuzzy was also used to help us manage the edit distance between
characters and group together the similarity of words.  This helps provide an
automated self correct feature. This was needed as the provided database did
not have any data validation, thus data was stored in an unpredictable fashion.

#### Why?

AMNH already has a large amount of data, and reloading data from scratch may
miss information which already exists. Instead we provide data munging on the
current information in order to increase percentage of valid data from 30% to
90% and higher. This would also allow other teams to obtain reliable data.

#### Problems

Managing, manipulating, and modeling data is an art, which one needs to
understand the scope of the project to complete. We spent time researching the
tools available to us, and how we would like to accurately reflect the
experience of interacting with the data. Often times there is a lot of sparse
data, asking if we could model it in a different way. 

