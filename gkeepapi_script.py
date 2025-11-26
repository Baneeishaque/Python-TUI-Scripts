# Not Working - BadAuthentication Error

import gkeepapi

# Obtain a master token for your account (see docs)
master_token = '...'

keep = gkeepapi.Keep()
success = keep.authenticate('user@gmail.com', master_token)

note = keep.createNote('Todo', 'Eat breakfast')
note.pinned = True
note.color = gkeepapi.node.ColorValue.Red
keep.sync()
