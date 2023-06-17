# Data Warehouse Architecture

<img width="1523" alt="Screenshot 2023-06-17 at 15 32 48" src="https://github.com/calvinnoval/efishery_DWH/assets/136886566/8a1fc872-1940-47b9-8261-0a1ca46b03be">

Descriptive Explanation of System Architecture and Data Flow.

<details><summary>Details</summary>
<p>

* Data Sources: These are data sources that come from various systems and applications such as transactional databases, third-party systems, text files, APIs, and so on.

* Data Ingestion: This component is responsible for collecting, acquiring, and inserting data from the data sources into the data warehousing system. This process involves activities such as extracting data from the sources, transforming the initial data, and loading data into temporary storage areas.

* Data Transformation: This component involves the process of transforming data from its initial format to a more structured format ready for analysis. The process includes data cleaning, data merging, format conversion, and aggregate calculations as required for analysis.

* Data Quality and Data Validation: This component is responsible for ensuring the quality of data entering the data warehousing system. It involves activities such as data verification, validation, and monitoring to ensure data integrity, consistency, accuracy, completeness, and reliability.

* Data Storage Layer: This layer serves as a storage location for data that has undergone transformation and is ready for use. In this architecture, there are two types of storage layers: Data Lake and Data Warehouse.

* Data Lake: It is a flexible and schema-less storage area capable of storing raw and structured data. The Data Lake allows storing unprocessed data, making it easier to explore and analyze data whose needs have not been determined.

* Data Warehouse: It is a more structured and pre-defined schema storage area. The Data Warehouse stores transformed data ready for analysis.

* Data Mart: It is a subset of the Data Warehouse tailored to specific analysis needs or specific department requirements. The Data Mart stores data relevant to specific analysis and is organized in an optimal format for those needs.

* Data Integration (Orchestration): This component manages and coordinates the data workflow, including task execution schedules, task dependency settings, and overall monitoring of the data pipeline process.

* BI Tools: These are software or applications used to visualize, analyze, and report data. BI Tools enable users to access and interpret data from the Data Warehouse or Data Mart into easier-to-understand information and more interactive visuals.

This architecture initiates the data flow from the Data Sources, then goes through the Data Ingestion process to insert the data into the system. Next, the data goes through the Data Transformation process to convert it into a more structured format ready for analysis. After that, the data passes through Data Quality and Data Validation to ensure its quality and integrity.

After the transformation and validation process, the data is stored in the Data Storage Layer, which consists of the Data Lake for storing raw data and exploration purposes, as well as the Data Warehouse for storing transformed data ready for analysis. From the Data Warehouse, data can be obtained through the Data Mart that is suitable for specific analysis needs.

Finally, the data is consumed and analyzed using BI Tools, which allow users to access, analyze, and visualize data in a more intuitive and interactive manner.


</p>
</details> 
