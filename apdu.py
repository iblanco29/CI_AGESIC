#! /usr/bin/env python

from smartcard.scard import *
import smartcard.util

SELECTIAS = [0x00, 0xA4, 0x04, 0x00, 0x0C, 0xA0, 0x00, 0x00, 0x00, 0x18, 0x40, 0x00, 0x00, 0x01, 0x63, 0x42, 0x00, 0x00]
SELECTDATA = [0x00, 0xA4, 0x00, 0x00, 0x02, 0x70, 0x01]
READBINARY = [0x00, 0xB0, 0x00, 0x00, 0x15]
COMMAND = [0x00, 0x00, 0x00, 0x00]

try:
    hresult, hcontext = SCardEstablishContext(SCARD_SCOPE_USER)
    if hresult != SCARD_S_SUCCESS:
        raise Exception('Failed to establish context : ' +
            SCardGetErrorMessage(hresult))
    print 'Context established!'

    try:
        hresult, readers = SCardListReaders(hcontext, [])
        if hresult != SCARD_S_SUCCESS:
            raise Exception('Failed to list readers: ' +
                SCardGetErrorMessage(hresult))
        print 'PCSC Readers:', readers

        if len(readers) < 1:
            raise Exception('No smart card readers')

        reader = readers[0]
        print "Using reader:", reader

        try:
            hresult, hcard, dwActiveProtocol = SCardConnect(hcontext, reader,
                SCARD_SHARE_SHARED, SCARD_PROTOCOL_T0 | SCARD_PROTOCOL_T1)
            if hresult != SCARD_S_SUCCESS:
                raise Exception('Unable to connect: ' +
                    SCardGetErrorMessage(hresult))
            print 'Connected with active protocol', dwActiveProtocol

            try:
                hresult, response = SCardTransmit(hcard, dwActiveProtocol, SELECTIAS)
                hresultData, responseData = SCardTransmit(hcard, dwActiveProtocol, SELECTDATA)
                hresultReadB, responseReadB = SCardTransmit(hcard, dwActiveProtocol, READBINARY)
                if hresult != SCARD_S_SUCCESS:
                    raise Exception('Failed to transmit: ' +
                        SCardGetErrorMessage(hresult))
                print 'Select: ' + smartcard.util.toHexString(response,
                    smartcard.util.HEX)
                hresult, response = SCardTransmit(hcard, dwActiveProtocol,
                    COMMAND)
                if hresult != SCARD_S_SUCCESS:
                    raise Exception('Failed to transmit: ' +
                        SCardGetErrorMessage(hresult))
                print 'Command: ' + smartcard.util.toHexString(response,
                    smartcard.util.HEX)
                
                if hresultData != SCARD_S_SUCCESS:
                    raise Exception('Failed to transmit: ' +
                        SCardGetErrorMessage(hresult))
                print 'SelectData: ' + smartcard.util.toHexString(responseData,
                    smartcard.util.HEX)
                hresultData, responseData = SCardTransmit(hcard, dwActiveProtocol,
                    COMMAND)
                if hresultData != SCARD_S_SUCCESS:
                    raise Exception('Failed to transmit: ' +
                        SCardGetErrorMessage(hresult))
                print 'Command: ' + smartcard.util.toHexString(responseData,
                    smartcard.util.HEX)
                
                if hresultReadB != SCARD_S_SUCCESS:
                    raise Exception('Failed to transmit: ' +
                        SCardGetErrorMessage(hresultReadB))
                print 'SelectReadB: ' + smartcard.util.toHexString(responseReadB,
                    smartcard.util.HEX)
                hresultReadB, responseReadB = SCardTransmit(hcard, dwActiveProtocol,
                    COMMAND)
                if hresultReadB != SCARD_S_SUCCESS:
                    raise Exception('Failed to transmit: ' +
                        SCardGetErrorMessage(hresultReadB))
                print 'Command: ' + smartcard.util.toHexString(responseReadB,
                    smartcard.util.HEX)
                
            finally:
                hresult = SCardDisconnect(hcard, SCARD_UNPOWER_CARD)
                if hresult != SCARD_S_SUCCESS:
                    raise Exception('Failed to disconnect: ' +
                        SCardGetErrorMessage(hresult))
                print 'Disconnected'

        except Exception, message:
            print "Exception:", message

    finally:
        hresult = SCardReleaseContext(hcontext)
        if hresult != SCARD_S_SUCCESS:
            raise Exception('Failed to release context: ' +
                    SCardGetErrorMessage(hresult))
        print 'Released context.'

except Exception, message:
    print "Exception:", message

import sys
if 'win32' == sys.platform:
    print 'press Enter to continue'
    sys.stdin.read(1)