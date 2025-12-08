#!/bin/bash

FILES=(
    "project.py"
    "table_initialization.py"
    "base_model_commands.py"
    "agent_client_commands.py"
    "nl2sql_commands.py"
    "AgentClient.sql"
    "AgentCreator.sql"
    "BaseModel.sql"
    "Configuration.sql"
    "CustomizedModel.sql"
    "DataStorage.sql"
    "InternetService.sql"
    "LLMService.sql"
    "ModelConfigurations.sql"
    "ModelServices.sql"
    "User.sql"
    "NL2SQL.csv"
)


OUTPUT_ZIP="submission.zip"


if [ -f "$OUTPUT_ZIP" ]; then
    rm "$OUTPUT_ZIP"
    echo "Removed existing $OUTPUT_ZIP"
fi


echo "Creating $OUTPUT_ZIP with the following files:"
for file in "${FILES[@]}"; do
    if [ -f "$file" ]; then
        echo "  - $file"
    else
        echo "  - WARNING: $file not found"
    fi
done

zip "$OUTPUT_ZIP" "${FILES[@]}" 2>/dev/null

if [ $? -eq 0 ]; then
    echo "Successfully created $OUTPUT_ZIP"
else
    echo "Error creating zip file"
    exit 1
fi

