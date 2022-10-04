import ijson
import csv

jsonfile = 'in/result.json'

header = ['mensagens']

c = open('out/texts.csv', 'w')
csv_writer = csv.writer(c)

csv_writer.writerow(header)

with open(jsonfile, "rb") as f:

    messages = ijson.items(f, "messages.item")

    for message in messages:

        text = message['text']

        if isinstance(text, str):

            trimmed_text = text.strip()

            if trimmed_text != '':
                csv_writer.writerow([trimmed_text])
        else:
            for submessage in text:

                if isinstance(submessage, str):

                    trimmed_submessage = submessage.strip()

                    if trimmed_submessage != '':
                        csv_writer.writerow([trimmed_submessage])
c.close()