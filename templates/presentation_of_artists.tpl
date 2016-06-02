<!doctype html>
<html lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="/static/styles.css">
    <title>Presentation of Artists</title>
</head>
<body>
    <h2>Presentation of Artists</h2>
    <input action="action" class="btn" type="button" value="Menu" onclick="location='/'" />
    <hr>
    <form  enctype="multipart/form-data" action="/" method="post">
    <input name="action" value="view_artists_results_submit" type="hidden" />
        <table>
            <tr>
                <td><label for="name">Name</label></td>
                <td><input id="name" name="name" type="text" autofocus/></td>
            </tr>
            <tr>
                <td><label for="surname">Surname</label></td>
                <td><input id="surname" name="surname" type="text" /></td>
            </tr>
            <tr>
                <td><label for="year_from">Birth Year - From</label></td>
                <td><input id="year_from" name="year_from" type="number" value="{{min}}" min="{{min}}" max="{{max}}"/></td>
            </tr>
            <tr>
                <td><label for="year_to">Birth Year - To</label></td>
                <td><input id="year_to" name="year_to" type="number" value="{{max}}" min="{{min}}" max="{{max}}"/></td>
            </tr>
            <tr>
                <td>Type</td>
                <td>
                    <input type="radio" name="option" value="singer"> Singer</br>
                    <input type="radio" name="option" value="songwriter"> SongWriter</br>
                    <input type="radio" name="option" value="composer"> Composer</br>
                </td>
            </tr>
            <tr>
                <td></td><td><input value="Submit" class="btn" type="submit" />
                <input class="btn" type="reset" value="Reset" /></td>
            </tr>
        </table>
    </form>
    <hr>
    % if error is not None:
        <p class="message" id="failure"><b>{{response}}</b>{{error}}</p>
    % end
</body>
</html>
