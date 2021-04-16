UPDATE BOTTLE_TYPE SET	
	TYPE_NAME = '{type_name}'
	,UPDATE_DATE = DATETIME('now') 

WHERE
	TYPE_ID = {type_id};
