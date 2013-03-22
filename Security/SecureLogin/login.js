		function matcher(event){
			var username = document.getElementById("user").value;
			var password = document.getElementById("pwd").value;

			if (password && username){
				handler(username, password);
			}
			else{
				alert('Please check username and password entered');
				window.location = "login.php";
			}
		}
		
		function handler(username, password) {
			
			var pubkeyContent = "-----BEGIN PUBLIC KEY-----MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCRF/CQAFt72U3bzS+RSQH9M23nmChMktHDJZtVdh60w2EUfVaB8rYRzub6aakdJh151Yl78Bwi29om84FeVhNn4i3u21J0u7RgT4S1aABGU1V31AFZFO+bEAktpnAGuKuOLPtFppaOmZgiLmHPwJw8UyYqoyRStFoUET/nDkH+qQIDAQAB-----END PUBLIC KEY-----";
			var pub_key = RSA.getPublicKey(pubkeyContent);
			var un = username;
			var pw = password;
			var time = String(new Date().getTime());
			var encryptedPass = RSA.encrypt(time+sha1(pw), pub_key);
	
			var pform = document.createElement('form');
			pform.action = 'login.php';
			pform.method = 'post';
			var p = document.createElement('input');
			p.type = 'hidden';
			p.name = 'p';
			p.value = encryptedPass;
			pform.appendChild(p);
			var u = document.createElement('input');
			u.type = 'hidden';
			u.name = 'u';
			u.value = un;
			pform.appendChild(u);
			var ts = document.createElement('input');
			ts.type = 'hidden';
			ts.name = 'ts';
			ts.value = time;
			pform.appendChild(ts);
			document.getElementById('encryption').appendChild(pform);
			
			pform.submit();
		}
