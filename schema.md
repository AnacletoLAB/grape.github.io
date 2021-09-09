# Website database schema

## Library versions
Table with informations relative to the library versions.

Table name: `versions`

| version_id | version_code | version_name | creation_time|
|------------|--------------|--------------|--------------|

### Keys
The table has one key, the version ID, which is the primary key of the table.

### Constraints
The version code and version name must be unique.

## Modules
Main modules of the library (for example Embiggen and Ensmallen and others like the bindings generator and fuzzers)

Table name: `modules`

| module_id | module_name|
|-----------|------------|

### Keys
The table has one key, the module ID, which is the primary key of the table.

### Constraints
The module name must be unique.

## Programming language
Since in the future we may add other bindings to the library, it is reasonable to create a table for the currently supported languages.

| language_id | language_name |
|-------------|---------------|

### Keys
The table has one key, the language ID, which is the primary key of the table.

### Constraints
The language name must be unique.

## Files
Table with main informations about the files within the library.

Table name: `files`

| file_id | file_name | file_path | creation_time | library_version_id | header | language_id | module_id |
|---------|-----------|-----------|---------------|--------------------|--------|-------------|-----------|

## Methods
Table with main informations about the library methods.

Table name: `methods`

| method_id | method_name | creation_time | library_version_id | description | return_type_id | row_number | file_id | test_coverage |
|-----------|-------------|---------------|--------------------|-------------|----------------|------------|---------|---------------|

### Keys
The table has two keys, the method ID, which is the primary key of the table, and the library version ID.

### Constraints
The combination of the method name and library version ID must be unique.

### Relationships
The library version ID must map to an existing version ID.

## Types
Table with the types used in any of the methods.

| type_id | type_name |
|---------|-----------|

### Keys
The type ID key is unique and it is the primary key of the table.

### Constraints
The type name must be unique.

## Method arguments
Table with the arguments for each argument.

| argument_id | method_id | argument_name | argument_type_id | description | default_value |
|-------------|-----------|---------------|------------------|-------------|---------------|

### Keys
The table has the argument_id unique key, which I would not know the use of but would seem like a good idea to keep it.

## Tags
Table with tags relative to methods. A method may have multiple 

Table name: `tags`

| tag_id | tag_name |
|--------|----------|

### Keys
The table has one key, the tag ID, which is the primary key of the table.

### Constraints
The tag name must be unique.