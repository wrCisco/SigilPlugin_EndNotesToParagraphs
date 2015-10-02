#!/usr/bin/env python



italiano = {0:"Seleziona i file dove si trovano le note:",
            1:"Cerca la/le lista/e di note con una classe in particolare",
            2:"\nCome mi devo comportare se i riferimenti alle note nel testo hanno già un id?",
            3:"Sovrascrivilo con l'id standard delle note",
            4:"Usa l'id già presente per il backlink",
            5:"Chiedi di volta in volta",
            6:"Sostituisco li.<classe/i delle note> con p.<classe/i "
            "delle note> nei fogli stile?\n(con la casella segnata: sì).",
            7:"Sostituisco ol.<classe/i del contenitore delle note> "
            "con div.<classe/i del contenitore>\ne ol#<id del contenitore> "
            "con div#<id del contenitore> nei fogli stile?\n(con la casella segnata: sì).",
            8:"Ok",
            9:"Annulla",
            10:"Trovato un riferimento nota con già un id",
            11:"Nel file <{}>, il riferimento alla nota {}, <{}>\n"
            "ha già un id: <{}>.\nVuoi mantenerlo o sovrascriverlo?",
            12:"Mantieni",
            13:"Sovrascrivi",
            14:"Mantieni tutti",
            15:"Sovrascrivi tutti",
            16:"Ok, non tocco niente.",
            17:"Non ho trovato nessuna lista in {}",
            18:"Sostituito \"ol\" con \"div\" in {}",
            19:"Sostituiti {} \"li\" con \"p\"",
            20:"Aggiunto il backlink alla nota {}",
            21:"Aggiunta numerazione alla nota {}",
            22:"Voci cercate nel foglio stile {}: {}\nPer sostituirle con: {}"
            "\nOperate {} sostituzioni.",
            23:"Aggiunto l'id per il backlink al riferimento nota {} nel file {}",
            24:"Il riferimento alla nota {} nel file {} ha già un id: {}.\n"
            "Uso l'id esistente per il backlink dalla nota",
            25:"Non ho trovato alcun riferimento per la nota {}: non aggiungo il backlink",
            26:"Quale numerazione uso per le note?\n"
            "Attenzione: questo avrà effetto solo sulle note, non sui rimandi alle note"}
english = {0:"Select notes's files:",
           1:"Look for notes list(s) with a particular class",
           2:"\nWhat shall I do if the references to the notes in the text already have an id?",
           3:"Overwrite it with notes's standard id",
           4:"Use the existent id for the backlink",
           5:"Ask everytime",
           6:"Shall I replace li.<notes class(es)> with p.<notes "
           "class(es)> in stylesheets?\n(signed box: yes).",
           7:"Shall I replace ol.<notes container class(es)> "
           "with div.<container class(es)> and\nol#<container id> "
           "with div#<container id> in stylesheets?\n(signed box: yes).",
           8:"OK",
           9:"Cancel",
           10:"Found a reference to a note that already has an id",
           11:"In file <{}>, the reference to the note {}, <{}>\n"
           "has already an id: <{}>.\nDo you want to keep it or overwrite?",
           12:"Keep",
           13:"Overwrite",
           14:"Keep all",
           15:"Overwrite all",
           16:"OK, I won't touch a thing.",
           17:"I didn\'t find any list in {}",
           18:"Replaced \"ol\" with \"div\" in {}",
           19:"Replaced {} \"li\" with \"p\"",
           20:"Added backlink to note {}",
           21:"Added numbering to note {}",
           22:"\nEntries sought in stylesheet {}: {}\nTo replace with: {}"
           "\nFulfilled {} replacements.",
           23:"Added backlink id to the reference of the note {} in file {}",
           24:"The reference to the note {} in file {} already has an id: {}.\n"
           "I will use the existent id for the backlink from the note",
           25:"I didn't find any reference for the note {}: I won't add the backlink",
           26:"Which numbering shall I use for the notes?\n"
           "Warning: this will affect only notes, not their references."}
