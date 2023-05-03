## Asterisk 20 Setup Adımları 



   ```sh sudo apt update ```

	   ```sh sudo apt upgrade -y ```

	    ```sh cd /usr/src/ ```

	  ```sh sudo wget https://downloads.asterisk.org/pub/telephony/asterisk/asterisk-20-current.tar.gz ```

	   ```sh sudo tar xvf asterisk-20-current.tar.gz ```

	    ```sh cd asterisk-20* ```

	   ```sh sudo git clone  https://github.com/felipem1210/asterisk-res_json.git ```

	  ```sh sudo ./asterisk-res_json/install.sh ```

	  ```sh sudo contrib/scripts/install_prereq  install ```
 
	```sh sudo contrib/scripts/get_mp3_source.sh ```
 
	 ```sh sudo contrib/scripts/get_swagger_ui.sh ```

	 ```sh sudo ./configure ```

	  ```sh sudo make menuselect ```

   ``` sudo make ```

  ``` sudo make install ```

	   ``` sudo make samples ```
 
  ``` sudo make config ```

  ``` sudo service asterisk status ```

  ``` sudo service asterisk start ```
	  ``` sudo service asterisk status ```

	  ``` sudo asterisk -rvvvvv ```
