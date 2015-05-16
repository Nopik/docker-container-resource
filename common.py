import os
import sys
import json
import docker
import urllib3

sys.stdout = sys.stderr

payload = json.load( sys.stdin )

urllib3.disable_warnings()

params = payload.get( 'params', {} )
source = payload.get( 'source', {} )

if source.get( 'tls', 0 ) == 1:
	if not os.path.exists( "/certs" ):
		os.makedirs( "/certs" )

	with open( "/certs/ca.pem", "w" ) as f:
		f.write( source[ 'certs' ][ 'ca' ] )
	with open( "/certs/cert.pem", "w" ) as f:
		f.write( source[ 'certs' ][ 'cert' ] )
	with open( "/certs/key.pem", "w" ) as f:
		f.write( source[ 'certs' ][ 'key' ] )
	
	tls_config = docker.tls.TLSConfig(verify=False,client_cert=('/certs/cert.pem','/certs/key.pem'))
	client = docker.Client(base_url=source['host'], tls=tls_config, version='auto')
else:
	client = docker.Client(base_url=source['host'], tls=None, version='auto')

def find_container( client, name, all=True ):
	res = None
	for c in client.containers(all=all):
		if ("/%s" % name) in c[ 'Names' ]:
			res = c
			break
	return( res )

def stop_container( client, name, remove=False ):
	c = find_container( client, name, True )

	if c is not None:
		print( "Stopping container", name )
		client.stop( name )
		print( "Container stopped" )

		if remove == True:
			client.remove_container( name )
			print( "Container removed" )
	else:
		print( "Old container not found" )

