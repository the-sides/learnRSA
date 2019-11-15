python3.7 ./rsa-keygen -p key.pub -s key -n 4096
echo '\n++++++++++++++++++++++++++++++++'
echo 'public key (key.pub) contents'
echo '++++++++++++++++++++++++++++++++'
cat key.pub
echo '\n++++++++++++++++++++++++++++++++'
echo 'private key (key) contents'
echo '++++++++++++++++++++++++++++++++'
cat key
python3.7 rsa-enc -k key.pub -i msg -o output
python3.7 rsa-dec -k key -i output -o washed
echo '\ndeleting key...'
# rm -rf key.pub key
