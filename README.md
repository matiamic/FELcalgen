# FEL generator kalendare pro tezke casy v karantene

## nase spolecne dilo: http://collabedit.com/9pvxd

## JAK NA TO?

1. rozjed generate_calendar.sh (linux/MacOS, na windowsech treba ve virtualboxu)   
   (je mozne pouzit i generate_calendar.bat pro windows, ale hodne jsem strilel od oka, a spis to fungovat nebude,
   na win vam to muze omylem nainstalovat ics a requests moduly do system-wide pythonu)  
   co by to melo delat:
   a) jestli neni v lokalnim adresari virtualni prostredi pro python3, vyrobi ho to a nainstaluje
      do nej dependencies (to se da udelat samostatne spustenim install_enviroment.sh)
      upozorneni: jestli nemate nainstalovane virtualenv tak vam ho to nainstaluje (not a big deal)

   b) rozjede to calgen.py, ktery se vas zepta, co chcete do toho kalendare a na jak dlouho
      vstup muzete natahnout ze souboru felcal.in, to je ale spis demo, vic toho bude na netu, kde na
      tom delame spolecne a je tam toho vic
      Pri stahovani z netu se pouzije URL ze souboru felcal_collabedit.txt, to odkazuje na ten spolecny soubor.
      Pri prepsani na: http://collabedit.com/download?id=46b8p se vam natahne rozvrh z releasu, o ktery se
      zkousim starat a mela by tam byt vzdy validni data:)

2. zaloz si novy kalendar(!!!), predevsim, aby slo vsechno naraz snadno odstranit cekam, ze se veci budou jeste menit
   v google se to dela takhle (jestli to chcete delat na telefonu asi se taky najde cesta):
   https://support.google.com/calendar/answer/37095?hl=en

3. importuj si felcal.ics do sveho noveho kalendare
   v google takhle (na telefonu si poslete felcal.ics do mailu kliknete na to (!!!->) kdyz vam to neda volbu kalendare, udelejte to na pocitaci):
   https://support.google.com/calendar/thread/3231927?hl=en

4. chces neco odebrat? smaz stavajici kalendar a projed kroky 1 - 3

5. qed, michal

## TROUBLESHOOTING

1. jeslti pouzivate windows: nepouzivejte windows  
   (nebo zkuste imitovat to, co se ma dit v genereate_calendar.bat manualne v cmd)  
   (taky to zkuste spustit jako spravce)

2. jestli vam to nejde na ubuntu, problem bude nejspis s instalovanim virtualenv (rekl bych ze to spis uz budete mit), 
   to muzete udelat manualne pip / pip3 install virtualenv a pak by ten kod mel dobehnout (snad)

3. dosla ti trpelivost?  
   manualne si nainstalujte ics a request do system-wide pythonu  
   (pip / pip3 install ics requests)  
   a rozjedte calgen.py, jako kdybyste spousteli vlastni program (python / python3 calgen.py)

## FAQ

1-Q. Jak poznam, ze je vsechno vpohode?  
1-A. Do felcal.ics se ulozi vas kalendar, je to plain text, takze se muzete podivat dovnitr, kde by to melo vypadat zhruba takhle:  

BEGIN:VCALENDAR
VERSION:2.0
PRODID:ics.py - http://git.io/lLljaA
BEGIN:VEVENT
DESCRIPTION:Programovani v C s Bartem Simpsonem - Jan Faigl
DTEND:20200331T140000Z
... spousta dalsich radek ...

