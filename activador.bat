keys10H="TX9XD-98N7V-6WMQ6-BX7FG-H8Q99", "KTNPV-KTRK4-3RRR8-39X6W-W44T3", "YTMG3-N6DKC-DKB77-7M9GH-8HVX7", "4CPRK-NM3K3-X6XXQ-RXX86-WXCHW"
keys10P="VK7JG-NPHTM-C97JM-9MPGT-3V66T", "8N67H-M3CY9-QT7C4-2TR7M-TXYCV", "2B87N-8KFHP-DKV6R-Y2C8J-PKCKT", "DXG7C-N36C4-C4HTG-X4T3X-2YV77", "WYPNQ-8C467-V2W6J-TX4WX-WT2RQ"
keys11H="YTMG3-N6DKC-DKB77-7M9GH-8HVX7"
keys11P="VK7JG-NPHTM-C97JM-9MPGT-3V66T"
set /p wversion="Windows [10/11] >> "
set /p wtype="Home or Pro [H/P] >> "

keylist="keys"%wversion%%wtype%
(for %%a in (%keylist%) do ( 
    slmgr.vbs -upk
    slmgr.vbs /ipk %%a
    slmgr /skms kms.digiboy.ir
    slmgr /ato
    echo "[!] Si se ha activado correctamente presiona Ctrl+C"
    pause
))