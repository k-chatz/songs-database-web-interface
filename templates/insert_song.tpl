<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="/static/styles.css">
    <title>Insert Song</title>
</head>
<body>
    <h2>Insert Song</h2>
    <input action="action" class="btn" type="button" value="Menu" onclick="location='/'" />
    <hr>
    <form enctype="multipart/form-data" action="/" method="post">
    <input name="action" value="insert_song_submit" type="hidden" />
        <table>
            <tr>
                <td><label for="title">Title</label></td>
                <td><input id="title" name="title" type="text" maxlength="60" autofocus required/></td>
            </tr>
            <tr>
                <td><label for="year">Production Year</label></td>
                <td><input id="year" name="year" type="number" value="{{max}}" max="{{max}}" required/></td>
            </tr>
            <tr>
                <td><label for="cd">CD</label></td>
                <td>
                    <select id="cd" name="cd" required>
                    % for record in productions:
                      <option value="{{record[0]}}">{{record[1]}} {{record[2]}}</option>
                    % end
                   </select>
                </td>
            </tr>
            <tr>
                <td><label for="singer">Singer</label></td>
                <td>
                    <select id="singer" name="singer" required>
                    % for record in artists:
                      <option value="{{record[0]}}">{{record[1]}} {{record[2]}}</option>
                    % end
                    </select>
                </td>
            </tr>
            <tr>
                <td><label for="composer">Composer</label></td>
                <td>
                    <select id="composer" name="composer" required>
                    % for record in artists:
                      <option value="{{record[0]}}">{{record[1]}} {{record[2]}}</option>
                    % end
                    </select>
                </td>
            </tr>
            <tr>
                <td><label for="songwriter">Song writer</label></td>
                <td>
                    <select id="songwriter" name="songwriter" required>
                    % for record in artists:
                      <option value="{{record[0]}}">{{record[1]}} {{record[2]}}</option>
                    % end
                    </select>
                </td>
            </tr>
            <td></td>
            <td><input type="submit" class="btn" value="Submit"  /></td>
        </table>
    </form>
    <hr>
    % if response != '':
        % if records[0] > 0 or records[1] > 0:
            <p class="message" id="success" ><b>{{response}}</b></p>
        % else:
            <p class="message" id="failure"><b>{{response}}</b></br>
             % for e in error:
                {{e}}</br>
             % end
            </p>
        % end
    % end
</body>
</html>
