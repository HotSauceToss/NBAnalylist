from Sheets.get_service import service

class SheetsWriter:
    def __init__(self, sID):
        self.SPREADSHEET_ID = sID
        self.s = service()

    def update_cell(self, row, col):
        pass

    ## Append new entries to a sheet
    # @param values array of new entries to append
    def append_to_sheet(self, values):
        body = {
            'values' : values
        }
        range = "Test!A:A";
        self.s.spreadsheets().values().append(
            spreadsheetId=self.SPREADSHEET_ID, 
            body=body,
            range = range,
            valueInputOption="USER_ENTERED"
        ).execute()