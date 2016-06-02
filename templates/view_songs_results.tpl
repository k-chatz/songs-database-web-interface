<!doctype html>
<html lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="/static/styles.css">
    <title>View Songs Result</title>
</head>
<body>
    <h2>View Songs Results</h2>
    <input action="action" class="btn" type="button" value="Menu" onclick="location='/'" />
    <input action="action" class="btn" type="button" value="Cancel" onclick="history.go(-1);" />
    <hr>
        <table frame = 'above'>
            <tr>
                % for field in result[0]:
                <th>{{field}}</th>
                % end
            </tr>
            % for row in result[1:]:
            <tr>
                <input name="action" value="edit_song_information" type="hidden" />
                % f = 0
                % for data in row:
                % data = data if data != None else '(Null)'
                <td><input class="field" type="text" name="{{result[0][f]}}" value="{{data}}" readonly ></td>
                % f = f + 1
                % end
            </tr>
            % end
        </table>
    <hr>
    % if response != '':
        % if error is None:
            <p class="message" id="success" ><b>{{response}}</b></p>
        % else:
            <p class="message" id="failure"><b>{{response}}</b></br>{{error}}</p>
        % end
    % end
</body>
</html>
