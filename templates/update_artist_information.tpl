<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="/static/styles.css">
    <title>Update Artist Information</title>
</head>
<body>
    <h2>Update Artist Information</h2>
    <input action="action" class="btn" type="button" value="Menu" onclick="location='/'" />
    <hr>
    <form enctype="multipart/form-data" action="/" method="post">
        <input id="id" name="id" type="hidden" value="{{id}}"/>
        <table>
            <tr>
                <td><label for="name">Name</label></td>
                <td><input id="name" name="name" type="text" value="{{name}}" maxlength="36" /></td>
            </tr>
            <tr>
                <td><label for="surname">Surname</label></td>
                <td><input id="surname" name="surname" type="text" value="{{surname}}" maxlength="45" required /></td>
            </tr>
            <tr>
                <td><label for="year">Birth Year</label></td>
                <td><input id="year" name="year" type="number" value="{{year}}" max="{{max}}" required /></td>
            </tr>
            <td></td>
            <td>
                <input type="submit" class="btn" name="action" value="Update" />
                <input type="submit" class="btn" name="action" value="Delete" />
            </td>
        </table>
    </form>
    <hr>
    % if response != '':
        % if records > 0:
            <p class="message" id="success" ><b>{{response}}</b></p>
        % else:
           <p class="message" id="failure"><b>{{response}}</b></br>{{error}}</p>
        % end
    % end
</body>
</html>
