import os

keys = ["W269N-WFGWX-YVC9B-4J6C9-T83GX","334NH-RXG76-64THK-C7CKG-D3VPT","44RPN-FTY23-9VTTB-MP9BX-T84FV","9FNHH-K3HBT-3W4TD-6383H-6XYWF","DCPHK-NFMTC-H88MJ-PFHPY-QJ4BJ","MH37W-N47XK-V7XM9-C7227-GCQG9","NRG8B-VKK3Q-CXVCJ-9G2XF-6Q84J","PBHCJ-Q2NYD-2PX34-T2TD6-233PK","QFFDN-GRT3P-VKWWX-X7T3R-8B639","VKJG7-NPHTM-C97JM-9MPGT-3V66T","VKJG7-NPHTM-C97JM-9MPGT-3V66T","YYVX9-NTFWV-6MDM3-9PT4T-4M68B"]

for a in keys:
    os.system('slmgr.vbs -upk')
    os.system('slmgr.vbs /ipk '+a)
    os.system('slmgr /skms kms.digiboy.ir')
    os.system('slmgr /ato')
    verify = input("Se ha activado correctamente??[y/n] >> ")
    if verify  == "y" or verify == "Y":
        exit()
