<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="/static/styles.css">
    <title>Insert Artist</title>
</head>
<body>
    <h2>Insert Artist</h2>
    <input action="action" class="btn" type="button" value="Menu" onclick="location='/'" />
    <hr>
    <form enctype="multipart/form-data" action="/" method="post">
    <input name="action" value="insert_artist_submit" type="hidden" />
        <table>
            <tr>
                <td><label for="id">National Id</label></td>
                <td><input id="id" name="id" type="text" minlength="8" maxlength="8" autofocus required /></td>
            </tr>
            <tr>
                <td><label for="name">Name</label></td>
                <td><input id="name" name="name" type="text" maxlength="36"/></td>
            </tr>
            <tr>
                <td><label for="surname">Surname</label></td>
                <td><input id="surname" name="surname" type="text" maxlength="45" required /></td>
            </tr>
            <tr>
                <td><label for="year">Birth Year</label></td>
                <td><input id="year" name="year" type="number" value="{{max}}" max="{{max}}"/></td>
            </tr>
            <td></td>
            <td><input type="submit" class="btn" value="Insert"  /></td>
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
