<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="/static/styles.css">
    <title>Presentation Of Songs</title>
</head>
<body>
    <h2>Presentation Of Songs</h2>
    <input action="action" class="btn" type="button" value="Menu" onclick="location='/'" />
    <hr>
    <form enctype="multipart/form-data" action="/" method="post">
    <input name="action" value="view_songs_results" type="hidden" />
        <table>
            <tr>
                <td><label for="title">Song Title</label></td>
                <td><input id="title" name="title" type="text" autofocus /></td>
            </tr>
            <tr>
                <td><label for="year">Production Year</label></td>
                <td><input id="year" name="year" type="number" /></td>
            </tr>
            <tr>
                <td><label for="company">Company</label></td>
                <td><input id="company" name="company" type="text" /></td>
            </tr>
            <td></td>
            <td><input type="submit" class="btn" value="Submit"  /></td>
        </table>
    </form>
    <hr>
</body>
</html>
