python3.7 ./rsa-keygen -p key.pub -s key -n 1024
echo '\n++++++++++++++++++++++++++++++++'
echo 'public key (key.pub) contents'
echo '++++++++++++++++++++++++++++++++'
cat key.pub
echo '\n++++++++++++++++++++++++++++++++'
echo 'private key (key) contents'
echo '++++++++++++++++++++++++++++++++'
cat key
python3.7 rsa-enc -k key.pub -i msg
echo '\ndeleting key...'
# rm -rf key.pub key
