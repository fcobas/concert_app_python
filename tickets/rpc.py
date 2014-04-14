
def retornarUsuariosRPC(tel):
    import xmlrpclib
    user = 'daw'
    pwd = 'daw-123'
    import hashlib
    m = hashlib.md5(pwd)
    pwd = m.hexdigest()
    server_url = 'http://{0}:{1}@marcelocaiafa.com/daw/rpc/'.format(user, pwd)
    try:
        proxy = xmlrpclib.ServerProxy(server_url)
        response = proxy.info(tel)
    except xmlrpclib.Fault as err:
        print 'Fault', err.faultCode, err.faultString
        return False
    except xmlrpclib.ProtocolError as err:
        print 'Protocol', err.errcode, err.errmsg
        return False
    except Exception as e:
        print e
        return False
    else:
        return response