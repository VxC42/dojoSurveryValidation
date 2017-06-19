def formIsValid(client):
    errors=[]
    isValid=True
    if len(client['name'])<1:
        errors.append('Please enter your name.')
        isValid=False
    if len(client['comment'])<1:
        errors.append('Please enter a comment.')
        isValid=False
    if len(client['comment'])>120:
        errors.append('Please input less than 120 characters.')
        isValid=False
    return {"isValid":isValid, "errors":errors}
