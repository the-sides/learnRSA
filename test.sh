python3 keygen.py -p key.pub -s key -n 1024
echo '\n++++++++++++++++++++++++++++++++'
echo 'public key (key.pub) contents'
echo '++++++++++++++++++++++++++++++++'
cat key.pub
echo '\ndeleting key...'
echo '\n++++++++++++++++++++++++++++++++'
echo 'private key (key) contents'
echo '++++++++++++++++++++++++++++++++'
cat key
echo '\ndeleting key...'
rm -rf key.pub key