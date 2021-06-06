def nlp_analysis(credentials, project, paragraph_text="wallstreetjournal"):
    import pandas as pd
    import numpy as np
    from google.cloud import language_v1
    text = paragraph_text
    client =language_v1.LanguageServiceClient()
    document = {"content": text,
    "type_":language_v1.Document.Type.PLAIN_TEXT,"language": "en"}
    
    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = language_v1.EncodingType.UTF8

    response = client.analyze_entities(request = {'document': document, 'encoding_type': encoding_type})
    
    entity_name=[]
    entity_type=[]
    entity_salience=[]

    for entity in response.entities:
        entity_name.append(entity.name)
        entity_type.append(language_v1.Entity.Type(entity.type_).name)
        entity_salience.append(entity.salience)
    
    result = pd.DataFrame({"entity_name":entity_name, "entity_salience":entity_salience})
    result['entity_salience']=result['entity_salience']*1000
    result['entity_salience']=result['entity_salience'].astype(int)
    result=result.to_dict()
    return result