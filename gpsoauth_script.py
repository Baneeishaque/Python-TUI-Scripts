# Not Working - may be due to 2FA

import gpsoauth

email = 'example@gmail.com'
password = 'my-password'
android_id = '0123456789abcdef'

master_response = gpsoauth.perform_master_login(email, password, android_id)
print('Master response:', master_response)
master_token = master_response['Token']
print('Master token:', master_token)

auth_response = gpsoauth.perform_oauth(
    email, master_token, android_id,
    service='sj', app='com.google.android.music',
    client_sig='...')
print('Auth response:', auth_response)
token = auth_response['Auth']
print('Auth token:', token)
