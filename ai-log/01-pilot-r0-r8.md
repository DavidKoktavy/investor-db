▗ ▗   ▖ ▖  Claude Code v2.1.296
           Opus 5.5 · Claude Pro
 ▘▘   ▝▝   ~/Desktop/Investor DB Starter

  Opus 5.5 is now your default model and it draws down usage faster than Sonnet 5. Switch anytime with /model.

❯ Read CLAUDE.md and PLAN.md, then run the Pilot runbook R0–R8. Work through it 
  without asking me unless something can’t be undone. Commit and push after     
  every step. Stop after R8.                                                    

⏺ I'll start by reading the plan and recent logs.

  Ran 3 shell commands (ctrl+o to expand)

⏺ R0 setup.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && ls .venv
      >/dev/null 2>&1 || python3 -m venv .venv; .venv/bin/python -m pip install
      -q -r requirements.tx…)
  ⎿  .................................................
        [100%]
     49 passed in 3.60s
     … +3 lines (ctrl+o to expand)
  ⎿  Created data/fx/ecb_rates.csv (+30 -0)
       1 +date,currency,rate_per_eur,source_url                          
       2 +2026-10-12,AUD,1.6032,https://www.ecb.europa.eu/stats/eurofxref
         +/eurofxref-daily.xml                                           
       3 +2026-10-12,BRL,5.5819,https://www.ecb.europa.eu/stats/eurofxref
         +/eurofxref-daily.xml                                           
       4 +2026-10-12,CAD,1.5946,https://www.ecb.europa.eu/stats/eurofxref
         +/eurofxref-daily.xml                                           
       5 +2026-10-12,CHF,0.9312,https://www.ecb.europa.eu/stats/eurofxref
         +/eurofxref-daily.xml                                           
       6 +2026-10-12,CNY,7.4832,https://www.ecb.europa.eu/stats/eurofxref
         +/eurofxref-daily.xml                                           
       7 +2026-10-12,CZK,24.391,https://www.ecb.europa.eu/stats/eurofxref
         +/eurofxref-daily.xml                                           
       8 +2026-10-12,DKK,7.4748,https://www.ecb.europa.eu/stats/eurofxref
         +/eurofxref-daily.xml                                           
       9 +2026-10-12,GBP,0.84478,https://www.ecb.europa.eu/stats/eurofxre
         +f/eurofxref-daily.xml                                          
      10 +2026-10-12,HKD,8.7743,https://www.ecb.europa.eu/stats/eurofxref
         +/eurofxref-daily.xml                                           
      11 +2026-10-12,HUF,365.13,https://www.ecb.europa.eu/stats/eurofxref
         +/eurofxref-daily.xml                                           
      12 +2026-10-12,IDR,20036.18,https://www.ecb.europa.eu/stats/eurofxr
         +ef/eurofxref-daily.xml                                         
      13 +2026-10-12,ILS,3.432,https://www.ecb.europa.eu/stats/eurofxref/
         +eurofxref-daily.xml                                            
      14 +2026-10-12,INR,107.086,https://www.ecb.europa.eu/stats/eurofxre
         +f/eurofxref-daily.xml                                          
      15 +2026-10-12,ISK,136.4,https://www.ecb.europa.eu/stats/eurofxref/
         +eurofxref-daily.xml                                            
      16 +2026-10-12,JPY,177.33,https://www.ecb.europa.eu/stats/eurofxref
         +/eurofxref-daily.xml                                           
      17 +2026-10-12,KRW,1490.53,https://www.ecb.europa.eu/stats/eurofxre
         +f/eurofxref-daily.xml                                          
      18 +2026-10-12,MXN,20.5081,https://www.ecb.europa.eu/stats/eurofxre
         +f/eurofxref-daily.xml                                          
      19 +2026-10-12,MYR,4.5663,https://www.ecb.europa.eu/stats/eurofxref
         +/eurofxref-daily.xml                                           
      20 +2026-10-12,NOK,10.6955,https://www.ecb.europa.eu/stats/eurofxre
         +f/eurofxref-daily.xml                                          
      21 +2026-10-12,NZD,1.9968,https://www.ecb.europa.eu/stats/eurofxref
         +/eurofxref-daily.xml                                           
      22 +2026-10-12,PHP,70.169,https://www.ecb.europa.eu/stats/eurofxref
         +/eurofxref-daily.xml                                           
      23 +2026-10-12,PLN,4.385,https://www.ecb.europa.eu/stats/eurofxref/
         +eurofxref-daily.xml                                            
      24 +2026-10-12,RON,5.337,https://www.ecb.europa.eu/stats/eurofxref/
         +eurofxref-daily.xml                                            
      25 +2026-10-12,SEK,11.1965,https://www.ecb.europa.eu/stats/eurofxre
         +f/eurofxref-daily.xml                                          
      26 +2026-10-12,SGD,1.4314,https://www.ecb.europa.eu/stats/eurofxref
         +/eurofxref-daily.xml                                           
      27 +2026-10-12,THB,37.585,https://www.ecb.europa.eu/stats/eurofxref
         +/eurofxref-daily.xml                                           
      28 +2026-10-12,TRY,55.1635,https://www.ecb.europa.eu/stats/eurofxre
         +f/eurofxref-daily.xml                                          
      29 +2026-10-12,USD,1.1181,https://www.ecb.europa.eu/stats/eurofxref
         +/eurofxref-daily.xml                                           
      30 +2026-10-12,ZAR,18.4945,https://www.ecb.europa.eu/stats/eurofxre
         +f/eurofxref-daily.xml                                          
  ⎿  (timeout 5m)

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && git add -A && git
      commit -qm "data: R0 ECB reference rates (2026-10-12)…)
  ⎿  225 candidates -> 9 triage batches of up to 25 in /Users/davidkoktavy/
     Desktop/Investor DB Starter/data/candidates/triage
     attempt1
     … +17 lines (ctrl+o to expand)
  ⎿  Created data/candidates/triage/input_01.csv (+26 -0)
       1 +candidate_id,name,website,hq_guess,suspected_type,note         
       2 +3ts-capital-partners,3TS Capital Partners,,,vc,TCEE Fund III an
         +d Technology in Central and Eastern Europe SICAR (EIF) and TCEE
         + Fund IV (CEFoF); EIF names manager as 3TS Capital Partners Oy.
         + Historic Czech activity (Lupa 2014 mentions 3TS Cisco Growth);
         + current investment team location not checked. Website not iden
         +tified.                                                        
       3 +500-emerging-europe,500 Emerging Europe,,,vc,The Village Networ
         +k investor (Awards 2023 impact). Fund status and HQ not checked
         +.                                                              
       4 +abris-capital,Abris Capital,https://www.abris-capital.com,PL,pe
         +,"Abris Capital Partners. Warsaw office on CVCA profile. Buyout
         + and expansion capital in CEE, 1 CZ deal listed."              
       5 +accel,Accel,https://www.accel.com,US,vc,"Example deal: Viktor U
         +SD 75M (May 2026, lead). HQ from prior knowledge. Website from 
         +Lupa link."                                                    
       6 +accolade,Accolade,https://accolade.eu,CZ,other,"Prague 8. Owns 
         +industrial parks and Brno airport and runs a property fund (Acc
         +olade Fund SICAV). PLAN 2.4 cites it as the associate member th
         +at is a park owner, so likely real_estate_only. Added as a bord
         +erline test case."                                             
       7 +across-private-investments,Across Private Investments,,SK,unkno
         +wn,SuperScale investor (Awards 2024). Identity and HQ not verif
         +ied.                                                           
       8 +ai-startup-incubator,AI Startup Incubator,,,other,"Listed by Ve
         +stbee with USD 150K-1.5M investment; suincubator.ai (single sou
         +rce, not used)."                                               
       9 +air-ventures,Air Ventures,https://airventures.eu,,vc,Listed by 
         +Papermark and Vestbee with airventures.eu; HQ not stated in eit
         +her.                                                           
      10 +airbridge,Airbridge,,,unknown,"Smartlook exit investor (Awards 
         +2024). Identity, HQ and type not verified; name is ambiguous." 
      11 +akcelerator-vsem,Akcelerátor VŠEM,,CZ,other,Accelerator listed 
         +by Vestbee; equity terms not stated.                           
      12 +alea-capital,Alea Capital Partners,https://aleacp.com,PT,vc,"Ex
         +ample deal: Choice USD 7.1M (Mar 2026, lead). Portuguese per Lu
         +pa. Website from Lupa link."                                   
      13 +alfa8,alfa8,,,vc,GA Drilling investor (Awards 2025). Identity a
         +nd HQ not verified.                                            
      14 +alpha-intelligence-capital,Alpha Intelligence Capital,,,vc,Phot
         +oneo investor (Awards 2024). HQ not verified.                  
      15 +angelinvest,Angelinvest,https://www.angelinvest.com,DE,vc,Examp
         +le deal: Modeinspect (Jan 2026). German fund per Lupa. Website 
         +from Lupa link.                                                
      16 +arctern-ventures,ArcTern Ventures,,CA,vc,"Woltair investor (Awa
         +rds 2024). Canada is a guess from knowledge, not verified."    
      17 +arieli-capital,Arieli Capital,,IL,vc,Named as Powerful Medical 
         +investor in Newstream's 2023 winners article. HQ Israel is a gu
         +ess from the name; not verified.                               
      18 +arx-equity-partners,ARX Equity Partners,https://www.arxequity.c
         +om,CZ,pe,"Prague 1 office. MBO/MBI and expansion capital per CV
         +CA profile. | ARX CE V Cooperatief U.A., manager ARX Equity Par
         +tners B.V., Czech team (EIF Czechia list); Arx CEE III/IV also 
         +EIF-backed. Private equity, likely outside VC scope. Awards 202
         +3 PE Fund Manager finalist. Website per scout_cvca.csv (CVCA sc
         +out), not independently fetched here."                         
      19 +aspire11,Aspire11,https://www.aspire11cap.com,CZ,vc,"Example de
         +al: Revolut (Dec 2025, first direct investment, hundreds of mil
         +lions CZK per Lupa); Vinted (Jun 2026). Late-stage platform of 
         +Pavel Mucha (Kaya) and Petr Borkovec targeting EUR 500M; border
         +line growth/PE rather than VC. Website from Lupa link. | Czech 
         +investment platform with EUR 500m inaugural pension-backed fund
         + (Vestbee Q3 2025); co-founded by Pavel Mucha (Kaya VC) and Pet
         +r Borkovec; EUR 20m in Vinted (Lupa 2026-06-23) and in the Revo
         +lut round (Lupa 2025-12-09); deals look late-stage, so type is 
         +uncertain. Website not identified."                            
      20 +aternus-family-office,Aternus Family Office,,CZ,family_office,"
         +In Seedtable Czech ranking (aggregator lead, name only, not ver
         +ified)."                                                       
      21 +atomico,Atomico,,GB,vc,"Example deal: Mews USD 300M (Jan 2026, 
         +new investor). HQ from prior knowledge. Website not identified.
         +"                                                              
      22 +austrian-growth-capital-fund,Austrian Growth Capital Fund,,AT,o
         +ther,"Fund named in CEFoF list; manager not stated. Austrian, p
         +robably outside scope. Website not identified."                
      23 +badideas-fund,BADideas.fund,,,vc,"Named in CzechCrunch deal new
         +sletter. Identity, HQ not verified."                           
      24 +bakala-capital,Bakala Capital,,CZ,private_holding,"In Seedtable
         + Czech ranking (aggregator lead, name only, not verified)."    
      25 +battery-ventures,Battery Ventures,,US,vc,"Example deal: Mews US
         +D 300M (Jan 2026, returning investor); also Mar 2025 round per 
         +Vestbee. HQ from prior knowledge. Website not identified."     
      26 +bd-partners,BD Partners,https://bdpartners.cz,CZ,vc,"Example de
         +al: WanderWallet pre-seed (Mar 2026). Also Myriad AI (Sep 2025)
         +. CzechCrunch Oct 2023 described it as investment vehicle of tw
         +o individuals, so may be private holding. Website per the Lupa 
         +article's link (domain taken from fetch summary)."             
  ⎿  Created data/candidates/triage/input_02.csv (+26 -0)
       1 +candidate_id,name,website,hq_guess,suspected_type,note         
       2 +bohemia-venture-capital,Bohemia Venture Capital,,CZ,vc,"Fund of
         + the BMH group, Feedyou investor per CzechCrunch. Website not i
         +dentified."                                                    
       3 +bolt-accelerator,BOLT,,,other,Accelerator listed by Vestbee; eq
         +uity terms and HQ not stated.                                  
       4 +bond-ventures,Bond Ventures,,SE,vc,"Example deal: Elredo (Oct 2
         +026, new investor). Swedish investor per Lupa. Website not iden
         +tified."                                                       
       5 +bonuvis,Bonuvis,https://www.bonuvis.com,CZ,advisor,Prague 1. Se
         +lf-described corporate finance and investment boutique: M&A and
         + capital-raising advisory plus investment clubs for individuals
         + or families. Advisor that may also invest.                    
       6 +borovicka-capital,Borovicka Capital,https://www.borovickacapita
         +l.com,,vc,Example deal: Outfindo late-seed (Jan 2025). Listed i
         +n tech.eu top investors for Czech Republic H1 2025 (2 deals). H
         +Q not stated in sources seen. Website from Lupa article link.  
       7 +bpd-partners,BPD Partners,,SK,unknown,Powerful Medical investor
         + (Awards 2023). Identity unverified.                           
       8 +braiins,Braiins,,CZ,unknown,"Listed in tech.eu top investors fo
         +r Czech Republic H1 2025 (1 deal); deal not shown. Appears to b
         +e an operating company (bitcoin mining software) rather than a 
         +fund, so may be a corporate investor; HQ from prior knowledge, 
         +not a source. Website not identified."                         
       9 +brightcap-ventures,BrightCap Ventures,,BG,vc,Example deal: Robo
         +sizeME (Feb 2026). Also in tech.eu top investors for Czech Repu
         +blic 2024. Lupa 2022 called a Brightcap fund Bulgarian. Website
         + not identified.                                               
      10 +btcz-ventures,BTCZ Ventures,,,vc,"Example deal: Taveren Therape
         +utics (Dec 2025, undisclosed). HQ and nature not stated. Websit
         +e not identified."                                             
      11 +budeto,Budeto,,,unknown,"Example deal: Vetstor seed EUR 1M (Dec
         + 2025, with JSK, Zaka VC, Purple). Nature of the entity (fund, 
         +angel vehicle, company) unknown. Website not identified."      
      12 +category-ventures,Category Ventures,,US,vc,"Example deal: Myria
         +d AI seed USD 7.8M (Sep 2025, lead, with N1 Ventures, BD Partne
         +rs and others). Myriad is Czech-American. HQ from prior knowled
         +ge. Website not identified."                                   
      13 +cb-espri,CB Espri,,,unknown,Named as Powerful Medical investor 
         +in Newstream's 2023 winners article. Identity unverified.      
      14 +chilli-ventures,Chilli Ventures,,,vc,"Listed in tech.eu top inv
         +estors for Czech Republic H1 2025 (1 deal); the specific deal w
         +as not shown on the page, so no example deal. Aggregator lead o
         +nly. Website and HQ not identified."                           
      15 +creandum,Creandum,,SE,vc,Better Stack investor (Awards 2023 VC 
         +Deal CZ finalist).                                             
      16 +credo-ventures,Credo Ventures,https://www.credoventures.com,CZ,
         +vc,"Prague (Karlovo namesti 10). Start-up and growth VC in IT/i
         +nternet per CVCA profile. | Example deal: Delta Green (Oct 2025
         +, with Tilia and Purple). Also Picogrid (US, Jun 2026) and Duvo
         +.ai (Dec 2025). Website: homepage fetched, lists offices in Pra
         +gue and Krakow. | EIF-backed active funds: Credo Stage 2 LP (si
         +gned 2018-10-02) and Credo Stage III SCSp (2023-11-09), manager
         + Credo Ventures a.s. Also named in EIF's 17 Czech funds (CzechC
         +runch). Awards: VC Fund Manager finalist 2023 and 2025; investo
         +r in Better Stack, Upheal, Delta Green; fifth fund announced 20
         +26-03-23 (Lupa listing). Website listed by Papermark, ellty, Ve
         +stbee, Failory and scout_cvca.csv."                            
      17 +crescendo-ventures,Crescendo Ventures,,RO,vc,"Example deal: Aiv
         +iro EUR 450k (Dec 2025, with Danube Angels and JIC Ventures). R
         +omanian fund per Lupa. Website not identified. | Romanian fund 
         +in the Aiviro round (Lupa 2025-12-12)."                        
      18 +crowdberry,Crowdberry,,SK,vc,"Slovak; investor in Powerful Medi
         +cal (2023), Sensoneo (2024), MultiplexDX (2025). CzechCrunch ne
         +wsletter names Crowdberry Investment Management; may be partly 
         +a crowdfunding platform (not verified)."                       
      19 +cvi,CVI,https://www.cvi.eu,PL,lender,Warsaw. CVCA profile: dire
         +ct lending / senior debt / mezzanine and minority equity only e
         +xceptionally. PLAN 2.4 names it as the debt-focused full member
         +. Domain taken from CVCA profile only: a domain-restricted sear
         +ch returned no hits for cvi.eu.                                
      20 +czech-business-angels-association,Czech Business Angels Associa
         +tion (CBAA),,CZ,angel,"Association of angel clubs; ellty lists 
         +cbaa.cz (single source, not used). Probably not an investor its
         +elf."                                                          
      21 +czech-founders-vc,Czech Founders VC,,CZ,vc,"Example deal: Merch
         +antee (Jun 2026, participated). Named most active investor of 2
         +024 (9 deals) in CzechCrunch review (Jan 2025). Fund of the Cze
         +ch Founders community. Website not found without guessing. | Fo
         +unders-backed alternative investment fund (45 founders, about E
         +UR 10m; CzechCrunch 2022). Awards 2024 impact finalist NOLD lis
         +ts Czech Founders Ventures. Papermark lists czechfounders.vc (s
         +ingle source, not used). Relationship to United Founders not st
         +ated in sources."                                              
      22 +czechinvest,CzechInvest,https://czechinvest.gov.cz,CZ,other,"Go
         +vernment agency; ellty.com says CZK 646M committed to about 260
         + startups in 2025 (grants / incubation). Expected exclusion as 
         +grant program. Domain confirmed by a czechinvest.gov.cz URL in 
         +search results. | State agency running startup programmes (Czec
         +hAccelerator, CzechStartups, ESA BIC). Expected exclusion (gran
         +t_or_program_only). Domain seen in a CzechInvest URL in search 
         +results."                                                      
      23 +danube-angels,Danube Angels,,AT,angel,Example deal: Aiviro EUR 
         +450k (Dec 2025). Vienna-based platform pooling about twenty pri
         +vate investors per Lupa. Angel platform; borderline. Website no
         +t identified. | Vienna angel platform in the Aiviro round (Lupa
         + 2025-12-12).                                                  
      24 +day-one-capital,Day One Capital,,HU,vc,"Example deal: Whalebone
         + Series B (Feb 2025, existing investor). HQ country is a guess 
         +from a search-result title only (bbj.hu article on its CEE fund
         +), not from the source article. Website not identified."       
      25 +decibel,Decibel,,US,vc,"Example deal: E2B seed USD 11.5M (Oct 2
         +024, lead, with KAYA VC and Sunflower Capital). HQ from prior k
         +nowledge. Website not identified."                             
      26 +decibel-vc,Decibel VC,,US,vc,E2B investor (Awards 2025).       
  ⎿  Created data/candidates/triage/input_03.csv (+26 -0)
       1 +candidate_id,name,website,hq_guess,suspected_type,note         
       2 +dendis-capital,Dendis Capital,https://www.dendiscapital.com,CZ,
         +private_holding,"Example deal: Carebot EUR 400k (Jan 2026). Als
         +o HTG Medical (Jul 2026, Vestbee). Led by the Dendis couple per
         + Lupa. Website from Lupa link."                                
       3 +depo-ventures,DEPO Ventures,https://depoventures.com,CZ,vc,"Pra
         +gue 7. CVCA profile shows no website; domain found via search o
         +f its own news/portfolio pages (angel fund and syndicate deals)
         +. Tickets EUR 50-300k per profile. | Example deal: WanderWallet
         + pre-seed USD 500k (Mar 2026, with BD Partners). Also Readmio (
         +Feb 2026), ArcSpace (France, Aug 2026); new Ukraine fund with N
         +RI commitment (Oct 2026). Website from Lupa link (ellty.com lis
         +ts depoventures.com instead). | DEPO Ventures One SCSp (manager
         + DEPO Ventures Sarl, Luxembourg vehicle) selected by NRI for Fo
         +nd Ukrajina (announced 2026-08-26; NRI initial CZK 94m). Czech 
         +managing partner Petr Šíma. Also Awards 2024 impact finalist NO
         +LD investor; listed by ellty, Papermark, AIN. Website per Paper
         +mark, ellty and scout_cvca.csv."                               
       4 +dff-ventures,DFF Ventures,https://www.dff.ventures,NL,vc,"Examp
         +le deal: Grid.online EUR 4M (Jun 2026, lead; its first Czech in
         +vestment). Amsterdam per Lupa. Website from Lupa link."        
       5 +diaspora-ventures,Diaspora Ventures,,,vc,"Named in CzechCrunch 
         +deal newsletter. Identity, HQ not verified."                   
       6 +dreamcraft-ventures,Dreamcraft Ventures,,,vc,"Listed in tech.eu
         + top investors for Czech Republic H1 2025 (1 deal); the specifi
         +c deal was not shown on the page, so no example deal. Aggregato
         +r lead only. Website and HQ not identified."                   
       7 +dtcp-growth,DTCP Growth,,DE,vc,"Example deal: Resistant AI Seri
         +es B USD 25M (Oct 2025, lead). German investor per Lupa. Websit
         +e not identified."                                             
       8 +earlybird,Earlybird,,DE,vc,"Example deal: TopK seed CZK 120M (J
         +ul 2025, with Kaya and Irregular Expressions). HQ from prior kn
         +owledge (tech.eu also lists Earlybird Venture Capital). Website
         + not identified."                                              
       9 +ebrd-venture-capital,EBRD Venture Capital,,GB,vc,Manta investor
         + (Awards 2024 VC Exit); Brightpick investor listed as EBRD in 2
         +025. Programme of a multilateral bank (London).                
      10 +eic-fund,EIC Fund,,,vc,Sensoneo investor (Awards 2024). Europea
         +n Innovation Council Fund (EU public fund); HQ not verified.   
      11 +electron-capital-partners,Electron Capital Partners,,,vc,"Examp
         +le deal: Groundcom seed EUR 1.5M (Jun 2025); also HTG Medical (
         +Jul 2026, Vestbee). HQ and website not identified."            
      12 +elevator-ventures,Elevator Ventures,,AT,cvc,"Example deal: Wult
         +ra Series A EUR 6.8M (Jun 2026, existing investor). Type and HQ
         + from prior knowledge (Erste Group corporate VC), not the sourc
         +e. Website not identified."                                    
      13 +eleven-ventures,Eleven Ventures,https://www.11.vc,BG,vc,"Exampl
         +e deal: Outfindo late-seed EUR 1.2M (Jan 2025, lead). HQ countr
         +y from prior knowledge, not the source. Website from Lupa link.
         +"                                                              
      14 +emun,EMUN investiční společnost,https://www.emun.cz,CZ,family_o
         +ffice,Prague. Multi-family office platform and licensed fund ma
         +nager (12 funds: access funds and co-investment structures). Ma
         +y fall under fund_of_funds_or_lp_only.                         
      15 +enterprise-investors,Enterprise Investors,https://www.ei.com.pl
         +,PL,pe,Warsaw HQ with a Prague office. CVCA profile links www.e
         +i.com.pl/cz. Own site also mentions a venture capital fund clos
         +ing (date not checked).                                        
      16 +eqt-ventures,EQT Ventures,,SE,vc,Example deal: EQT Growth led M
         +ews USD 300M (Jan 2026); EQT Ventures earlier investor in Super
         +nova (Sep 2025 article). One row for EQT brands; HQ from prior 
         +knowledge. Website not identified.                             
      17 +esa-bic-czech-republic,ESA BIC Czech Republic,,CZ,other,"ESA bu
         +siness incubation centre (EUR 50K per Vestbee), CzechInvest pro
         +gramme per Businessinfo. Expected exclusion (grant_or_program_o
         +nly)."                                                         
      18 +espira-investments,Espira Investments,https://www.espirainvestm
         +ents.com,CZ,pe,"Prague 6. Growth financing and MBO, EUR 1-3m ti
         +ckets per CVCA profile. | Espira Fund I in CEFoF list; also nam
         +ed among EIF-backed funds (CzechCrunch) and Awards 2023 PE Fund
         + Manager finalist (ICON Communication). Website per scout_cvca.
         +csv (CVCA scout), not independently fetched here."             
      19 +european-investment-fund,European Investment Fund (EIF),https:/
         +/www.eif.org,LU,other,"Fund-of-funds LP: about CZK 656M (EUR 27
         +M) mandate into IP Lab Ventures I (Sep 2026); also behind Tenso
         +r Ventures (Lupa May 2024). No direct startup deals. HQ from pr
         +ior knowledge. Website not identified (eif.org seen only in ell
         +ty.com list). | Fund-of-funds manager behind Czech ESIF FoF, RR
         +F Czech Republic FoF and CEFoF; LP in Czech VC funds. Expected 
         +exclusion (fund_of_funds_or_lp_only). Domain seen in eif.org UR
         +Ls of fetched pages."                                          
      20 +euroventures,Euroventures,,,vc,Euroventures V Technology and Gr
         +owth Fund in CEFoF list; Euroventures also named as Daytrip inv
         +estor (Awards 2024 VC Investice CR finalist). HQ and website no
         +t verified.                                                    
      21 +everita-capital,EVERITA Capital,https://everitacap.com,CZ,pe,"P
         +rague. PE/growth capital in healthcare, education, food, manufa
         +cturing and services; CZ/HR/PL/SK/SI per CVCA profile. | EVERIT
         +A Fund I Cooperatief U.A., manager EVERITA Capital sro; lower-m
         +id-market private equity (EIF Czechia list). Website per scout_
         +cvca.csv (CVCA scout), not independently fetched here."        
      22 +evolving-europe,Evolving Europe,,,pe,"Evolving Europe Principal
         + Investments Fund in CEFoF list; manager, HQ and website not ve
         +rified."                                                       
      23 +experian,Experian,,IE,cvc,"Example deal: Resistant AI Series B 
         +(Oct 2025, existing investor). Operating company investing stra
         +tegically, not a fund. HQ from prior knowledge. Website not ide
         +ntified."                                                      
      24 +fasanara-capital,Fasanara Capital,,GB,lender,"Example deal: EUR
         + 30M debt financing line for Flowpay (Mar 2025). Debt provider,
         + expected exclusion as lender. HQ from prior knowledge. Website
         + not identified."                                              
      25 +fazole-ventures,Fazole Ventures,https://www.fazole.vc,CZ,vc,"Ex
         +ample deal: Everbot (Sep 2025, 12.2% stake). Run by Pavel Bousk
         +a, Lubos Cerny, Pavel Prikryl per Lupa. HQ is a guess from the 
         +Czech context. Website from Lupa link. | Named as CBAA founding
         + member by ellty. Not verified."                               
      26 +fiedler-capital,Fiedler Capital,,,unknown,Munch investor (Award
         +s 2023 impact). Entity not verified.                           
  ⎿  Created data/candidates/triage/input_04.csv (+26 -0)
       1 +candidate_id,name,website,hq_guess,suspected_type,note         
       2 +fifth-wall,Fifth Wall,,US,vc,Woltair investor (Awards 2024; wri
         +tten Fifthwall on the page).                                   
       3 +fil-rouge-capital,Fil Rouge Capital,,HR,vc,"Example deal: FaceU
         +p (May 2026, lead). Croatian fund per Lupa. Website not identif
         +ied."                                                          
       4 +fivesquare,Fivesquare,,CZ,unknown,"In Seedtable Czech ranking a
         +s Fivesquare s.r.o. (aggregator lead, name only, not verified).
         +"                                                              
       5 +forward-one,Forward.one,https://www.forward.one,,vc,"Example de
         +al: Edmund EUR 2.5M (Apr 2026, lead). Foreign fund; HQ not stat
         +ed in the article. Website from Lupa link."                    
       6 +founder-institute-prague,Founder Institute Prague,,CZ,other,Acc
         +elerator chapter listed by Vestbee; equity terms not stated in 
         +fetched pages.                                                 
       7 +ftmo,FTMO,,CZ,other,"Example deal: USD 1M into Zerohash (US, Oc
         +t 2025); also acquirer of Oanda (Dec 2025, headline). Operating
         + company making strategic investments, not a fund. Website not 
         +identified without guessing."                                  
       8 +gain-ventures,GAIN (Gain Ventures),,,vc,"Earlier investor in Ca
         +rebot (named in Jan 2026 article, printed only as GAIN; CzechCr
         +unch Apr 2024 spells Gain Ventures). Identity uncertain. HQ and
         + website not identified. | Carebot / Flowpay investor in CzechC
         +runch article. HQ not verified."                               
       9 +garage-angels,Garage Angels,https://g-angels.cz,CZ,angel,"Examp
         +le deal: Flae Robotics (Oct 2026). Also Groundcom (Jun 2025), H
         +TG Medical (Jul 2026). Angel club / syndicate; borderline. Webs
         +ite from Lupa link. | Named as CBAA founding member by ellty. H
         +Q guessed CZ; not verified."                                   
      10 +genesis-capital,Genesis Capital Equity,https://www.genesis.cz,C
         +Z,pe,"CVCA name is Genesis Capital Equity s.r.o.; own site uses
         + the brand Genesis Capital. Prague 10. Buyouts and growth, EUR 
         +10-35m equity tickets. | Example deal: majority of Slevomat (No
         +v 2025; headline and teaser only, page fetch blocked). Context:
         + Knihobot via Genesis Growth Equity Fund I (Aug 2024, just outs
         +ide window). PE / growth equity. Website not identified. | Gene
         +sis Private Equity Fund V SCSp, manager Genesis Capital Equity 
         +s.r.o. (GPEF III also EIF-backed). Awards PE Fund Manager final
         +ist 2023-2025 (2023 winner per Newstream). Private equity, like
         +ly outside VC scope. Website per scout_cvca.csv (CVCA scout), n
         +ot independently fetched here. | Genesis Growth Equity Fund I (
         +EIF signed 2024-11-08; also CEFoF), manager Genesis Capital Gro
         +wth s.r.o.; Awards 2025 PE Fund Manager finalist and Homecare H
         +olding exit. Possibly same group site as Genesis Capital Equity
         + (genesis.cz); not confirmed, so website empty."               
      11 +gi21-capital,Gi21 Capital,https://www.gi21capital.com,CZ,vc,"Ex
         +ample deal: FaceUp (May 2026). Also Hermetiq (US, Aug 2026) and
         + Zerops (May 2026, Lupa teaser). Fund of Damir Spoljaric per Lu
         +pa. Website from Lupa link. | Prague fund of Damir Špoljarič; l
         +ead investor in Zerops seed round of EUR 1.7m (Lupa 2026-05-18)
         +. Website not identified."                                     
      12 +goldman-sachs-alternatives,Goldman Sachs Alternatives,,US,pe,Ex
         +ample deal: Mews EUR 69.3M (Mar 2025). Alternative investments 
         +arm of a bank; HQ from prior knowledge. Website not identified.
      13 +google-ventures,Google Ventures (GV),,US,cvc,"Example deal: Res
         +istant AI Series B (Oct 2025, existing investor). Corporate VC 
         +of Alphabet. Website not identified."                          
      14 +grouport-ventures,Grouport Ventures,,CZ,vc,"In Seedtable Czech 
         +ranking (aggregator lead, name only, not verified)."           
      15 +harbourvest-partners,HarbourVest Partners,,US,pe,"Example deal:
         + Mews USD 300M (Jan 2026, new investor). Fund-of-funds / second
         +aries manager; HQ from prior knowledge. Website not identified.
         +"                                                              
      16 +hartenberg,Hartenberg,,CZ,private_holding,Named in CzechCrunch 
         +deal newsletter among funds / investors; entity details unverif
         +ied. Website not identified.                                   
      17 +headline,Headline,,US,vc,"Example deal: Upheal Series A USD 10M
         + (Nov 2024, lead, with Credo Ventures and Kaya). HQ not stated 
         +in the source. Website not identified. | Upheal investor listed
         + as Headline VC (Awards 2025). HQ is a guess; fund has offices 
         +in several countries."                                         
      18 +henq-capital-partners,HenQ Capital Partners,,NL,vc,"CloudTalk i
         +nvestor (Awards 2024, 2025), listed as HenQ Capital Partners B.
         +V."                                                            
      19 +i-and-i-biotech,i&i Biotech Fund (i&i Bio),https://www.inibio.e
         +u,CZ,vc,"Brand i&i Bio (i&i Biotech Fund). Prague 8. Early-stag
         +e biotech VC per own site title. | Example deal: Antiverse (Mar
         + 2026, led by Soulmates Ventures). Czech link from CzechCrunch 
         +Jan 2024 (CasInvent Pharma, with i&i Prague), outside window. W
         +ebsite not identified. | EUR 50m biomedical tech-transfer fund,
         + EIF committed EUR 25m (2021-09-24); named among EIF's Czech fu
         +nds in CzechCrunch. Fund manager entity not named in fetched so
         +urces; Česká spořitelna reported as LP. Website per IOCB page a
         +nd scout_cvca.csv (there as i&i Biotech Investments, so overlap
         +s)."                                                           
      20 +i-and-i-prague,i&i Prague,,CZ,other,"Biotech incubator at IOCB;
         + co-created i&i Biotech Fund with EIF; Vestbee lists iniprague.
         +com (single source, not used)."                                
      21 +impulse-ventures,Impulse Ventures,,CZ,vc,"Wikipedia list and AI
         +N rank 14 (H1 2022); Lupa names Ondřej Tomek (Impulse Ventures)
         + as a Spinoffy backer. Vestbee lists impulseventures.com (singl
         +e source, not used)."                                          
      22 +incomming-ventures,InCOMMing Ventures,,CZ,vc,"In Seedtable Czec
         +h ranking (aggregator lead, name only, not verified)."         
      23 +index-ventures,Index Ventures,,GB,vc,Example deal: Duvo.ai pre-
         +seed and seed USD 16.5M (Dec 2025). HQ from prior knowledge. We
         +bsite not identified.                                          
      24 +innova-capital,Innova Capital,https://www.innovacap.com,PL,pe,"
         +Warsaw. Expansion capital and buyouts, EUR 20-50m per CVCA prof
         +ile."                                                          
      25 +inovo-venture-partners,Inovo Venture Partners,,PL,vc,Listed on 
         +VC Beast Prague page; search results describe Inovo as Poland-b
         +ased (not verified). Website not identified.                   
      26 +insight-partners,Insight Partners,,US,vc,"Example deal: E2B Ser
         +ies A USD 21M (Jul 2025, lead). New York fund per Lupa. Website
         + not identified."                                              
  ⎿  Created data/candidates/triage/input_05.csv (+26 -0)
       1 +candidate_id,name,website,hq_guess,suspected_type,note         
       2 +integral-capital-group,Integral Capital Group,https://integralc
         +apgroup.com,HU,pe,Budapest address. PE in CEE. Own site also sh
         +ows Integral Venture Partners with a first fund close (VC arm; 
         +date not checked).                                             
       3 +inven-capital,Inven Capital,https://www.invencapital.cz,CZ,cvc,
         +"Prague 4. Corporate fund of CEZ Group, later-stage cleantech g
         +rowth investments. | Corporate VC of CEZ Group. Awards 2024 VC 
         +Fund Manager finalist; Woltair investor. Website per Papermark,
         + Failory and scout_cvca.csv."                                  
       4 +invera,Invera,,SI,pe,"Invera Private Equity Fund (formerly Asce
         +ndant Buy Out Fund) in CEFoF list. Search results suggest Inver
         +a Equity Partners is Slovenia/Croatia-based (not verified), so 
         +probably outside scope geography. Website not identified."     
       5 +investown,Investown,https://www.investown.cz,CZ,platform,Online
         + investment / lending platform; search-result title says Seed S
         +tarter became co-owner (snippet only). Expected exclusion (crow
         +dfunding_platform). Domain seen in search-result URL.          
       6 +ip-lab-ventures,IP Lab Ventures,,CZ,vc,"Manager of IP Lab Ventu
         +res I (EIF mandate from National Recovery Plan, EUR 27M plus pr
         +ivate capital; Lupa Sep 2026). No portfolio deal seen. Website 
         +not found. | IP Lab Ventures Fund I, university AI technology-t
         +ransfer fund, about CZK 656m from EIF / RRF Czech FoF (article 
         +dated 2026-09-23); partners Filip Fingl, Andrew Hladký, Jiří Na
         +vrátil. Website not found in fetched pages."                   
       7 +ipm,IPM,,,unknown,"Photoneo investor (Awards 2024). Ambiguous s
         +hort name, identity unverified."                               
       8 +irregular-expressions,Irregular Expressions,,,vc,"Example deal:
         + TopK seed CZK 120M (Jul 2025, with Earlybird and Kaya). HQ and
         + website not identified."                                      
       9 +itaca-business-incubator,ITACA Business Incubator,,,other,Incub
         +ator listed by Vestbee; equity terms and HQ not stated.        
      10 +ivbf,IVBF,,CZ,vc,Crypto-focused fund launched by Ondřej Tomek p
         +er CzechCrunch article. Size and status not given.             
      11 +j-t-arch,J&T Arch Investments (J&T Arch II),https://www.jtis.cz
         +/fond/A2PCA,CZ,pe,"Example deal: 68% of Sandberg Capital's port
         +folio incl. Seyfor, EUR 278M (Aug 2026). Qualified-investor fun
         +d linked to J&T group. URL is the fund page on the J&T fund-man
         +ager site, not a brand homepage. PE, expected out of VC scope."
      12 +j-t-ventures,J&T Ventures,https://www.jtventures.cz,CZ,vc,"Exam
         +ple deal: Definic seed (Jun 2026, lead). Also Wultra Series A (
         +Jun 2026, existing investor) and Oddin.gg (Jun 2025, main inves
         +tor). Website from Lupa article links. | Daytrip investor (Awar
         +ds 2024); linked to J&T group per Lupa. Website per Papermark, 
         +ellty, Vestbee, Failory."                                      
      13 +jafam-holding,Jafam Holding,,DE,private_holding,German holding 
         +named in a CzechCrunch deal summary. Type not verified.        
      14 +jaro-capital,JARO Capital,,,angel,"Earlier investor in Outfindo
         + (Jan 2025 article); vehicle of Robert Kyncl and Jaroslav Beck 
         +per Lupa. Angel vehicle, borderline. Website not identified."  
      15 +jet-investment,Jet Investment (Jet Ventures),https://www.jetinv
         +estment.eu,CZ,pe,"Brno. Buyout/growth/turnaround; CVCA profile 
         +also lists late-stage venture; tickets EUR 15-80m. | Example de
         +al: AppNava (US, Sep 2026, USD 1.8M via Jet Venture 1). Also He
         +rmetiq (Aug 2026), IAG (Jun 2026), Boost.space (Oct 2025). Brno
         + group of Igor Fait; venture vehicles Jet Ventures (ventures.je
         +tinvestment.cz) and Jen Venture 1 SICAV. Website from Lupa link
         +."                                                             
      16 +jic-ventures,JIC Ventures,https://www.jic.cz/ventures/,CZ,vc,"E
         +xample deal: FaceUp (May 2026, fund's first investment; Fil Rou
         +ge Capital led). Also Elredo lead (Oct 2026), Aiviro (Dec 2025)
         +, Groundcom (Jun 2025). Brno; fund still raising (E15 Apr 2026:
         + about 40 LPs); parent JIC agency invested from own money earli
         +er. Website fetched. | Brno, CZK 400m pre-seed/seed fund launch
         +ed 2026-04-07; managers Radim Kocourek and Miloš Sochor; backed
         + by South Moravian Region, City of Brno, four universities, CTP
         +, Česká spořitelna and others; not finally closed. Aiviro round
         + Dec 2025 (Lupa). Website not identified."                     
      17 +jinej-fond,Jinej fond,,,vc,"Example deal: HTG Medical EUR 450k 
         +(Jul 2026, with Garage Angels, Electron Capital Partners, JIC V
         +entures, Dendis Capital). Name taken from Vestbee headline list
         +ing. HQ and website not identified."                           
      18 +jsk-investments,JSK Investments,https://www.jskinvestments.cz,C
         +Z,private_holding,"Prague 1. Investment group investing own cap
         +ital: private/growth equity plus venture capital. Own site show
         +s startup deals (e.g. Andromeda Surgical; dates not checked). O
         +perates as SICAV. | Example deal: Elin.ai pre-seed (Dec 2024, E
         +UR 420k of EUR 1M). Also iSono Health (US, Oct 2025), Vetstor (
         +Dec 2025), Andromeda Surgical (US, Sep 2026). Investment compan
         +y of Simona Kijonkova. Website domain from a Lupa link to a pre
         +ss release on that domain. | Named among new funds in VC Deals 
         +Report 2025 coverage (2026-03-24); Vetstor investor (Lupa 2025-
         +12-09). Family investment group. Not the JSK advisory law firm 
         +of the Awards advisor category. Website per scout_cvca.csv (CVC
         +A scout), not independently fetched here."                     
      19 +kaya-vc,KAYA VC,https://www.kaya.vc,CZ,vc,"Prague 8 (Karlin). C
         +VCA profile body is empty, so type and strategy are unverified;
         + type guessed from the name. | Example deal: Viktor (USD 75M le
         +d by Accel, May 2026). Also TopK (Jul 2025), E2B seed (Oct 2024
         +), Upheal Series A (Nov 2024). Website fetched; lists offices i
         +n Warsaw, Prague, San Francisco and London with no HQ stated, s
         +o location of investment team to be confirmed. | Kaya 5 SCSp, m
         +anager KAYA Advisory s.r.o. (EIF Czechia list). Group vehicle E
         +nern Investments SICAV a.s. runs ENERN Tech III/IV sub-funds (E
         +IF active funds, CEFoF); same group, no separate row. Awards: V
         +C Fund Manager finalist 2023 (winner per Newstream), 2024, 2025
         +; investor in Better Stack, Woltair, E2B, Upheal. Website liste
         +d by Papermark, Vestbee, Failory, scout_cvca.csv."             
      20 +keiretsu-forum-prague,Keiretsu Forum Prague,,CZ,angel,"Angel ne
         +twork, named as CBAA founding member by ellty; also named in Lu
         +pa 2016 articles on the National Innovation Fund."             
      21 +kendaxa-group,Kendaxa Group,,CZ,unknown,"In Seedtable Czech ran
         +king (aggregator lead, name only, not verified)."              
      22 +kinnevik,Kinnevik,,SE,vc,Example deal: Mews (Mar 2025 and Jan 2
         +026). HQ from prior knowledge. Website not identified. | Mews i
         +nvestor (Awards 2025 VC Investments CR finalist).              
      23 +kkcg,KKCG,https://kkcg.com,CZ,private_holding,"Example deal: pl
         +aced funds into Link-XPV fund of Link Ventures (US, Dec 2025), 
         +as LP; no startup stake in that item. Investment group of Karel
         + Komarek; owner of Springtide Ventures. Website from Lupa link.
         + | Czech investment group, owner of Springtide Ventures; invest
         +ed in the Link-XPV fund (Lupa 2025-12-17). Website not identifi
         +ed."                                                           
      24 +koopeo-ventures,Koopeo Ventures,,CZ,vc,"Prague impact investor;
         + Vestbee lists koopeoventures.com (single source, not used). De
         +afcom investor in Awards 2022 (outside 2023-2025 window)."     
      25 +kpn-ventures,KPN Ventures,,NL,cvc,"CloudTalk investor (Awards 2
         +024, 2025); corporate venture arm of KPN."                     
      26 +lead-ventures,Lead Ventures,,,vc,"CloudTalk investor (Awards 20
         +24, 2025). HQ not verified."                                   
  ⎿  … 4 more files changed

⏺ R1: launching triage batches 01–03 in parallel.

⏺ 3 background agents launched (↓ to manage)
   ├ Triage batch 01
   ├ Triage batch 02
   └ Triage batch 03

⏺ While those run, I'll review decide.py's triage and queue logic, plus the
  schema.

  Ran 2 shell commands (ctrl+o to expand)

⏺ Triage batches 01–03 are running; I'll continue when they report back.

✻ Cooked for 35s · done Monday 5:06 PM

› Message from candidate-triage
  Wrote 25 rows to /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/candidates/triage/batch_02.csv (input order, header included).
  Unknown: 8 rows with investor_type=unknown (bohemia-venture-capital,
  bolt-accelerator, bond-ventures, braiins, budeto, cb-espri, chilli-ventures,
  crowdberry); 8 rows with hq_country=unknown (bohemia, bolt, bond,
  borovicka-capital, brightcap-ventures, crescendo-ventures, decibel,
  decibel-vc).
  Snippet: 16 rows evidence_kind=snippet (no fetched page); 9 rows are
  page-backed.
  Possible Czech VCs I was unsure of: chilli-ventures (Pardubice per snippets,
  PitchBook primary type PE/Buyout, so type left unknown) and btcz-ventures
  (Prague VC per PitchBook snippet only). Also check: decibel-vc looks like a
  duplicate of decibel, and crescendo-ventures conflicts with the input (search
  points to a Silicon Valley firm, not Romania).
  Caveat: several quotes come from WebFetch summaries, not verbatim page text,
  so check_quotes must verify them. cvi.eu fetch failed on a certificate error.

⏺ Batch 02: 8/25 unknown (32%), which is under the one-third rerun threshold.
  I'll log the run.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-12,candidate-triage,haiku,batch_02,,,,ok" >>
      data/runs/run_log.csv && wc -l data/candidate…)
  ⎿        26 data/candidates/triage/batch_02.csv
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      11  2026-10-11,candidate-triage,haiku,attempt1/batch_07,108698,20,7
          11.6,failed
      12  2026-10-11,candidate-triage,haiku,attempt1/batch_08,114325,30,7
          18.5,failed
      13  2026-10-11,candidate-triage,haiku,attempt1/batch_09,110833,22,7
          12.3,failed
      14 +2026-10-12,candidate-triage,haiku,batch_02,,,,ok               

⏺ Agent "Triage batch 02" finished · 1m 54s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && sed -i '' '$
      s/.*/2026-10-12,candidate-triage,haiku,batch_02,60054,37,114.3,ok/'
      data/runs/run_log.csv &…)
  ⎿  2026-10-12,candidate-triage,haiku,batch_02,60054,37,114.3,ok
  ⎿  Updated data/runs/run_log.csv (+1 -1)
      11  2026-10-11,candidate-triage,haiku,attempt1/batch_07,108698,20,7
          11.6,failed
      12  2026-10-11,candidate-triage,haiku,attempt1/batch_08,114325,30,7
          18.5,failed
      13  2026-10-11,candidate-triage,haiku,attempt1/batch_09,110833,22,7
          12.3,failed
      14 -2026-10-12,candidate-triage,haiku,batch_02,,,,ok               
      14 +2026-10-12,candidate-triage,haiku,batch_02,60054,37,114.3,ok   

⏺ Launching batch 04 to keep 3 running.

⏺ candidate-triage(Triage batch 04)
  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)

⏺ Batch 04 is running alongside 01 and 03; I'll continue when they report back.

✻ Sautéed for 11s · done Monday 5:08 PM

› Message from candidate-triage
  Wrote 25 rows to /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/candidates/triage/batch_03.csv (input order, header included).
  Unknown: 6 rows have hq_country unknown (diaspora-ventures, eic-fund,
  electron-capital-partners, european-investment-fund, evolving-europe,
  experian); 1 row has investor_type unknown (electron-capital-partners).
  Snippet evidence: 11 rows (diaspora-ventures, dtcp-growth,
  ebrd-venture-capital, eic-fund, electron-capital-partners, elevator-ventures,
  enterprise-investors, esa-bic-czech-republic, euroventures, evolving-europe,
  fasanara-capital). Page fetch failed or returned empty for these.
  Possible Czech VC not sure: fazole-ventures (CZ from the Praha 1 address on a
  garbled page, vc from press snippets only, medium). Electron Capital Partners
  could not be found at all, so it stays unknown.

⏺ Batch 03: 6/25 unknown, so no rerun is needed. I'll log it once the usage
  notification arrives.

✻ Churned for 1s · done Monday 5:09 PM

⏺ Agent "Triage batch 03" finished · 2m 41s

› Message from candidate-triage
  Wrote 25 rows to /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/candidates/triage/batch_01.csv (input order, header included).
  Unknown: hq_country unknown in 14 rows, investor_type unknown in 8 rows. 17
  rows have at least one unknown field.
  Snippet evidence: 10 rows (3ts-capital-partners, 500-emerging-europe,
  across-private-investments, air-ventures, airbridge, alfa8,
  alpha-intelligence-capital, arieli-capital, atomico,
  austrian-growth-capital-fund). Atomico's official site returned 403/429 and
  air-ventures has no fetched page, so both need a re-check.
  Possible Czech VCs I was not sure of: air-ventures (Prague per aggregators,
  website does not resolve), aspire11 (Czech platform per leads, type mixed),
  bd-partners (.cz site, team location not on fetched text),
  ai-startup-incubator (fetched lookai.vc says Prague, type not stated). Also
  bakala-capital (Greenville and Prague, set US) and arx-equity-partners (PE,
  Prague lead only).

⏺ Batch 01 is over the threshold: hq unknown in 14/25 rows. I'll keep the first
  output and re-run the batch once, and launch batch 05 alongside it.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && mkdir -p
      data/candidates/triage/rerun_first && git mv -k
      data/candidates/triage/batch_01.csv data/candid…)
  ⎿  batch_01.csv
  ⎿  Deleted data/candidates/triage/batch_01.csv (+0 -26)
       1 -candidate_id,website,hq_country,investor_type,equity_investor,e
         -vidence_url,evidence_kind,evidence_quote,evidence_date,confiden
         -ce,note                                                        
       2 -3ts-capital-partners,,unknown,unknown,unknown,https://f4.fund/f
         -irms/3ts-capital-partners,snippet,"growth-stage investor rather
         - than an early-stage one",,low,"Website not resolved (3ts.capit
         -al ENOTFOUND). TCEE funds. Offices Vienna, Warsaw, Bucharest, B
         -udapest, Bratislava per search summary; team location and type 
         -not verified"                                                  
       3 -500-emerging-europe,https://e2.vc/,unknown,vc,yes,https://tech.
         -eu/2024/11/18/500-emerging-europe-transforms-into-e2vc-new-era-
         -for-global-focused-startups/,snippet,"aim to support pre-seed a
         -nd seed-stage startups across CEE, the Baltics, and Turkey",,lo
         -w,"Renamed e2vc (2024). Fetched e2.vc shows no type or team loc
         -ation; footer clocks show San Francisco, London, Istanbul only.
         - Type from snippet, not verified on page"                      
       4 -abris-capital,https://www.abris-capital.com,unknown,pe,yes,http
         -s://www.abris-capital.com,page,"Abris Capital Partners is the l
         -eading ESG transformation specialist private equity investor fo
         -cused on Central Europe.",,medium,"Offices listed: Warsaw, Buch
         -arest, Nicosia; page does not say where the investment team sit
         -s. Warsaw per CVCA profile (lead only). Acquired majority stake
         - per page news"                                                
       5 -accel,https://www.accel.com,unknown,unknown,unknown,https://www
         -.accel.com/about,page,,,low,"Fetched pages show only tagline an
         -d navigation; type and location not on page. Palo Alto HQ and L
         -ondon office come from search snippets only, not used as eviden
         -ce. Needs extraction or manual check"                          
       6 -accolade,https://accolade.eu,unknown,not_an_investor,no,https:/
         -/accolade.eu,page,"Skupina Accolade připravuje, vlastní a dlouh
         -odobě pronajímá průmyslové budovy renomovaným společnostem",,me
         -dium,"Real estate developer and owner of industrial buildings; 
         -not a startup investor. Prague 8 is only the scout note; page d
         -oes not give HQ. Quote is the Czech original"                  
       7 -across-private-investments,,SK,unknown,unknown,https://www.capl
         -ight.com/investor/acrossgroup,snippet,"Bratislava-based investm
         -ent management firm offering private banking, asset management 
         -and corporate finance",,low,"No website fetched; Caplight aggre
         -gator summary only. Co-investor in SuperScale Series A (2023) p
         -er snippet. Type unknown: private banking and asset management,
         - not clearly VC"                                               
       8 -ai-startup-incubator,https://lookai.vc/,CZ,unknown,unknown,http
         -s://lookai.vc/,page,"create a network connecting AI startup fou
         -nders with investors",,medium,"Reached via redirect from suincu
         -bator.ai. Page: Prague, Czech Republic, where it was founded. L
         -ook AI Ventures fund described as the investing entity; AISI eq
         -uity role unclear. Possible CZ VC: flag"                       
       9 -air-ventures,,unknown,unknown,unknown,https://vestbee.com/vc-li
         -st/air-ventures,snippet,,,low,"airventures.eu did not resolve (
         -ENOTFOUND); airvcs.com is a parked domain. Aggregator summaries
         - describe a Prague early-stage VC, unverified. Possible CZ VC: 
         -flag"                                                          
      10 -airbridge,,NL,unknown,unknown,https://cc.cz/2020/12/brnensky-st
         -artup-smartlook-nabira-81-milionu-korun-velka-investice-mu-ma-n
         -aplno-otevrit-dvere-do-usa/,snippet,"the Dutch fund Airbridge E
         -quity Partners",,low,"Not fetched. Identity from Czech press sn
         -ippet: led Smartlook Series A (Dec 2020). Type and team locatio
         -n not verified"                                                
      11 -akcelerator-vsem,https://en.vsem.cz/accelerator-vsem.html,CZ,ac
         -celerator,unknown,https://en.vsem.cz/accelerator-vsem.html,page
         -,"is a program which supports starting businessmen and companie
         -s with a short history.",,medium,"Page calls itself an accelera
         -tor; no equity mentioned. Programme funded by EU Operational Pr
         -ogramme Employment (project 2017-2019 on page). Czech location 
         -inferred from VSEM, not stated on page. Possible public_agency-
         -type programme"                                                
      12 -alea-capital,https://aleacp.com,PT,pe,yes,https://aleacp.com,pa
         -ge,"Alea Capital Partners is a Lisbon-based Multi-Strategy Priv
         -ate Equity Firm that invests in Alternative Assets.",,medium,"L
         -isbon and Porto offices listed on page. Venture and Innovation 
         -strategy also present, so vc is possible. Website from Lupa lin
         -k"                                                             
      13 -alfa8,,unknown,family_office,unknown,https://www.cbinsights.com
         -/investor/alfa8,snippet,"describes it as a family office with a
         - strong focus on investment",,low,"Not fetched; aggregator snip
         -pet only. HQ conflicts: Germany (CB Insights) vs London (Seedta
         -ble). GA Drilling investor role conflicting across sources. Run
         -s venture unit COlab per snippet"                              
      14 -alpha-intelligence-capital,,unknown,unknown,unknown,https://www
         -.vestbee.com/vc-list/alpha-intelligence-capital,snippet,,,low,"
         -Not fetched; no website. Aggregator profiles conflict: Luxembou
         -rg HQ in one, US, Singapore and Europe team in another. Type un
         -known"                                                         
      15 -angelinvest,https://www.angelinvest.com,unknown,angel,no,https:
         -//www.angelinvest.com,page,"Angelinvest is an independent globa
         -l platform where pre- and early-seed startups meet active angel
         - investors.",,medium,"Online angel network platform; page says 
         -it does not manage funds. HQ not stated on page (German fund is
         - only a Lupa lead). Not a crowdfunding platform"               
      16 -arctern-ventures,https://www.arcternventures.com,CA,vc,yes,http
         -s://www.arcternventures.com,page,"ArcTern Ventures is a venture
         - capital firm that backs mission-driven founders.",,medium,"Pag
         -e lists offices Toronto, Canada; San Francisco, USA; Oslo, Norw
         -ay. Toronto as HQ per search summary; page does not say which o
         -ffice is HQ"                                                   
      17 -arieli-capital,,unknown,unknown,unknown,https://unicorn-nest.co
         -m/funds/arieli-capital/,snippet,,,low,"Not fetched; no website 
         -checked. Aggregator profiles conflict: HQ New York, Tel Aviv, o
         -r Israel with NY and London offices. Parent Arieli Group descri
         -bed as a family office, so private_holding or vc both possible"
      18 -arx-equity-partners,https://www.arxequity.com,unknown,pe,yes,ht
         -tps://www.arxequity.com,page,"We are proud of our 20-year track
         - record building great companies in successful partnerships wit
         -h business owners",,medium,"Page lists no office. Prague office
         - and Czech team are CVCA and EIF leads, not on fetched page. Ty
         -pe pe inferred from majority-stake news, not stated directly. P
         -ossible CZ PE: flag"                                           
      19 -aspire11,https://www.aspire11cap.com,unknown,vc,yes,https://www
         -.aspire11cap.com,page,"Investing in generational growth compani
         -es and leading venture funds.",,low,"Two arms: Eternals (direct
         - late-stage) and Tribes (partnerships with VC funds, LP-like). 
         -Type mixed: vc, growth or lp_only possible. Team location not o
         -n page; Czech per Vestbee and Lupa leads. Possible CZ VC: flag"
      20 -aternus-family-office,https://www.aternus.cz,CZ,family_office,u
         -nknown,https://www.aternus.cz,page,"nám. Svobody 527 / 739 61 T
         -řinec / 6. patro.",,medium,"Page: investor and partner in Czech
         - and foreign investment funds, so lp_only possible. Multi famil
         -y office per summary. ATERNUS Investment Group invests directly
         - per snippet. Address on page is Třinec, CZ"                   
      21 -atomico,https://www.atomico.com,GB,vc,yes,https://superscout.co
         -/investor/atomico-com,snippet,"Atomico is a London-headquartere
         -d venture firm founded in 2006 by Skype co-founder Niklas Zenns
         -tröm.",,low,"Official site returned HTTP 403 and 429; not fetch
         -ed. Quote is from aggregator search summary and must be re-chec
         -ked. Paris, Berlin, Stockholm offices also in summary"         
      22 -austrian-growth-capital-fund,,AT,pe,yes,https://ceelegalmatters
         -.com/austria/18755-herbst-kinsky-advises-ag-capital-on-structur
         -ing-austrian-growth-capital-fund,snippet,"It takes majority and
         - minority stakes in SMEs in Austria and neighboring countries."
         -,,low,"Not fetched. Managed by AG Capital, Vienna, per law-firm
         - snippet. Fund named in CEFoF list per scout. Website not ident
         -ified. Type pe inferred from SME stakes, not stated as pe"     
      23 -badideas-fund,https://badideas.fund,unknown,vc,yes,https://badi
         -deas.fund,page,"Pre-seed and seed VC for CEE",,medium,"Page giv
         -es no HQ. Riga, Latvia per aggregator snippets only. Type vc pe
         -r page; fund size and team not verified"                       
      24 -bakala-capital,https://www.bakalacapital.com,US,private_holding
         -,unknown,https://www.bakalacapital.com,page,"Based in Greenvill
         -e, South Carolina, and Prague, Czech Republic.",,medium,"Team l
         -isted in both Greenville SC and Prague; hq set to US by first-l
         -isted office. Possible CZ: flag. Page does not use the term fam
         -ily office, so private_holding by definition. Invests for one p
         -erson per page summary"                                        
      25 -battery-ventures,https://www.battery.com,unknown,vc,yes,https:/
         -/www.battery.com,page,"We are a technology and software-focused
         - investment firm.",,medium,"Six offices listed: Boston, San Fra
         -ncisco, Menlo Park, Tel Aviv, London, New York. HQ not stated o
         -n page. Backs founders at all stages of growth per page. Not CZ
         -"                                                              
      26 -bd-partners,https://bdpartners.cz,unknown,vc,yes,https://bdpart
         -ners.cz,page,"Backing Europe's most ambitious early-stage found
         -ers.",,low,"Page truncated; no team location on fetched text. E
         -arly-stage investor per tagline. CzechCrunch 2023 lead says inv
         -estment vehicle of two individuals, so private_holding possible
         -. Possible CZ VC: flag"                                        
  ⎿  Created data/candidates/triage/rerun_first/batch_01.csv (+26 -0)
       1 +candidate_id,website,hq_country,investor_type,equity_investor,e
         +vidence_url,evidence_kind,evidence_quote,evidence_date,confiden
         +ce,note                                                        
       2 +3ts-capital-partners,,unknown,unknown,unknown,https://f4.fund/f
         +irms/3ts-capital-partners,snippet,"growth-stage investor rather
         + than an early-stage one",,low,"Website not resolved (3ts.capit
         +al ENOTFOUND). TCEE funds. Offices Vienna, Warsaw, Bucharest, B
         +udapest, Bratislava per search summary; team location and type 
         +not verified"                                                  
       3 +500-emerging-europe,https://e2.vc/,unknown,vc,yes,https://tech.
         +eu/2024/11/18/500-emerging-europe-transforms-into-e2vc-new-era-
         +for-global-focused-startups/,snippet,"aim to support pre-seed a
         +nd seed-stage startups across CEE, the Baltics, and Turkey",,lo
         +w,"Renamed e2vc (2024). Fetched e2.vc shows no type or team loc
         +ation; footer clocks show San Francisco, London, Istanbul only.
         + Type from snippet, not verified on page"                      
       4 +abris-capital,https://www.abris-capital.com,unknown,pe,yes,http
         +s://www.abris-capital.com,page,"Abris Capital Partners is the l
         +eading ESG transformation specialist private equity investor fo
         +cused on Central Europe.",,medium,"Offices listed: Warsaw, Buch
         +arest, Nicosia; page does not say where the investment team sit
         +s. Warsaw per CVCA profile (lead only). Acquired majority stake
         + per page news"                                                
       5 +accel,https://www.accel.com,unknown,unknown,unknown,https://www
         +.accel.com/about,page,,,low,"Fetched pages show only tagline an
         +d navigation; type and location not on page. Palo Alto HQ and L
         +ondon office come from search snippets only, not used as eviden
         +ce. Needs extraction or manual check"                          
       6 +accolade,https://accolade.eu,unknown,not_an_investor,no,https:/
         +/accolade.eu,page,"Skupina Accolade připravuje, vlastní a dlouh
         +odobě pronajímá průmyslové budovy renomovaným společnostem",,me
         +dium,"Real estate developer and owner of industrial buildings; 
         +not a startup investor. Prague 8 is only the scout note; page d
         +oes not give HQ. Quote is the Czech original"                  
       7 +across-private-investments,,SK,unknown,unknown,https://www.capl
         +ight.com/investor/acrossgroup,snippet,"Bratislava-based investm
         +ent management firm offering private banking, asset management 
         +and corporate finance",,low,"No website fetched; Caplight aggre
         +gator summary only. Co-investor in SuperScale Series A (2023) p
         +er snippet. Type unknown: private banking and asset management,
         + not clearly VC"                                               
       8 +ai-startup-incubator,https://lookai.vc/,CZ,unknown,unknown,http
         +s://lookai.vc/,page,"create a network connecting AI startup fou
         +nders with investors",,medium,"Reached via redirect from suincu
         +bator.ai. Page: Prague, Czech Republic, where it was founded. L
         +ook AI Ventures fund described as the investing entity; AISI eq
         +uity role unclear. Possible CZ VC: flag"                       
       9 +air-ventures,,unknown,unknown,unknown,https://vestbee.com/vc-li
         +st/air-ventures,snippet,,,low,"airventures.eu did not resolve (
         +ENOTFOUND); airvcs.com is a parked domain. Aggregator summaries
         + describe a Prague early-stage VC, unverified. Possible CZ VC: 
         +flag"                                                          
      10 +airbridge,,NL,unknown,unknown,https://cc.cz/2020/12/brnensky-st
         +artup-smartlook-nabira-81-milionu-korun-velka-investice-mu-ma-n
         +aplno-otevrit-dvere-do-usa/,snippet,"the Dutch fund Airbridge E
         +quity Partners",,low,"Not fetched. Identity from Czech press sn
         +ippet: led Smartlook Series A (Dec 2020). Type and team locatio
         +n not verified"                                                
      11 +akcelerator-vsem,https://en.vsem.cz/accelerator-vsem.html,CZ,ac
         +celerator,unknown,https://en.vsem.cz/accelerator-vsem.html,page
         +,"is a program which supports starting businessmen and companie
         +s with a short history.",,medium,"Page calls itself an accelera
         +tor; no equity mentioned. Programme funded by EU Operational Pr
         +ogramme Employment (project 2017-2019 on page). Czech location 
         +inferred from VSEM, not stated on page. Possible public_agency-
         +type programme"                                                
      12 +alea-capital,https://aleacp.com,PT,pe,yes,https://aleacp.com,pa
         +ge,"Alea Capital Partners is a Lisbon-based Multi-Strategy Priv
         +ate Equity Firm that invests in Alternative Assets.",,medium,"L
         +isbon and Porto offices listed on page. Venture and Innovation 
         +strategy also present, so vc is possible. Website from Lupa lin
         +k"                                                             
      13 +alfa8,,unknown,family_office,unknown,https://www.cbinsights.com
         +/investor/alfa8,snippet,"describes it as a family office with a
         + strong focus on investment",,low,"Not fetched; aggregator snip
         +pet only. HQ conflicts: Germany (CB Insights) vs London (Seedta
         +ble). GA Drilling investor role conflicting across sources. Run
         +s venture unit COlab per snippet"                              
      14 +alpha-intelligence-capital,,unknown,unknown,unknown,https://www
         +.vestbee.com/vc-list/alpha-intelligence-capital,snippet,,,low,"
         +Not fetched; no website. Aggregator profiles conflict: Luxembou
         +rg HQ in one, US, Singapore and Europe team in another. Type un
         +known"                                                         
      15 +angelinvest,https://www.angelinvest.com,unknown,angel,no,https:
         +//www.angelinvest.com,page,"Angelinvest is an independent globa
         +l platform where pre- and early-seed startups meet active angel
         + investors.",,medium,"Online angel network platform; page says 
         +it does not manage funds. HQ not stated on page (German fund is
         + only a Lupa lead). Not a crowdfunding platform"               
      16 +arctern-ventures,https://www.arcternventures.com,CA,vc,yes,http
         +s://www.arcternventures.com,page,"ArcTern Ventures is a venture
         + capital firm that backs mission-driven founders.",,medium,"Pag
         +e lists offices Toronto, Canada; San Francisco, USA; Oslo, Norw
         +ay. Toronto as HQ per search summary; page does not say which o
         +ffice is HQ"                                                   
      17 +arieli-capital,,unknown,unknown,unknown,https://unicorn-nest.co
         +m/funds/arieli-capital/,snippet,,,low,"Not fetched; no website 
         +checked. Aggregator profiles conflict: HQ New York, Tel Aviv, o
         +r Israel with NY and London offices. Parent Arieli Group descri
         +bed as a family office, so private_holding or vc both possible"
      18 +arx-equity-partners,https://www.arxequity.com,unknown,pe,yes,ht
         +tps://www.arxequity.com,page,"We are proud of our 20-year track
         + record building great companies in successful partnerships wit
         +h business owners",,medium,"Page lists no office. Prague office
         + and Czech team are CVCA and EIF leads, not on fetched page. Ty
         +pe pe inferred from majority-stake news, not stated directly. P
         +ossible CZ PE: flag"                                           
      19 +aspire11,https://www.aspire11cap.com,unknown,vc,yes,https://www
         +.aspire11cap.com,page,"Investing in generational growth compani
         +es and leading venture funds.",,low,"Two arms: Eternals (direct
         + late-stage) and Tribes (partnerships with VC funds, LP-like). 
         +Type mixed: vc, growth or lp_only possible. Team location not o
         +n page; Czech per Vestbee and Lupa leads. Possible CZ VC: flag"
      20 +aternus-family-office,https://www.aternus.cz,CZ,family_office,u
         +nknown,https://www.aternus.cz,page,"nám. Svobody 527 / 739 61 T
         +řinec / 6. patro.",,medium,"Page: investor and partner in Czech
         + and foreign investment funds, so lp_only possible. Multi famil
         +y office per summary. ATERNUS Investment Group invests directly
         + per snippet. Address on page is Třinec, CZ"                   
      21 +atomico,https://www.atomico.com,GB,vc,yes,https://superscout.co
         +/investor/atomico-com,snippet,"Atomico is a London-headquartere
         +d venture firm founded in 2006 by Skype co-founder Niklas Zenns
         +tröm.",,low,"Official site returned HTTP 403 and 429; not fetch
         +ed. Quote is from aggregator search summary and must be re-chec
         +ked. Paris, Berlin, Stockholm offices also in summary"         
      22 +austrian-growth-capital-fund,,AT,pe,yes,https://ceelegalmatters
         +.com/austria/18755-herbst-kinsky-advises-ag-capital-on-structur
         +ing-austrian-growth-capital-fund,snippet,"It takes majority and
         + minority stakes in SMEs in Austria and neighboring countries."
         +,,low,"Not fetched. Managed by AG Capital, Vienna, per law-firm
         + snippet. Fund named in CEFoF list per scout. Website not ident
         +ified. Type pe inferred from SME stakes, not stated as pe"     
      23 +badideas-fund,https://badideas.fund,unknown,vc,yes,https://badi
         +deas.fund,page,"Pre-seed and seed VC for CEE",,medium,"Page giv
         +es no HQ. Riga, Latvia per aggregator snippets only. Type vc pe
         +r page; fund size and team not verified"                       
      24 +bakala-capital,https://www.bakalacapital.com,US,private_holding
         +,unknown,https://www.bakalacapital.com,page,"Based in Greenvill
         +e, South Carolina, and Prague, Czech Republic.",,medium,"Team l
         +isted in both Greenville SC and Prague; hq set to US by first-l
         +isted office. Possible CZ: flag. Page does not use the term fam
         +ily office, so private_holding by definition. Invests for one p
         +erson per page summary"                                        
      25 +battery-ventures,https://www.battery.com,unknown,vc,yes,https:/
         +/www.battery.com,page,"We are a technology and software-focused
         + investment firm.",,medium,"Six offices listed: Boston, San Fra
         +ncisco, Menlo Park, Tel Aviv, London, New York. HQ not stated o
         +n page. Backs founders at all stages of growth per page. Not CZ
         +"                                                              
      26 +bd-partners,https://bdpartners.cz,unknown,vc,yes,https://bdpart
         +ners.cz,page,"Backing Europe's most ambitious early-stage found
         +ers.",,low,"Page truncated; no team location on fetched text. E
         +arly-stage investor per tagline. CzechCrunch 2023 lead says inv
         +estment vehicle of two individuals, so private_holding possible
         +. Possible CZ VC: flag"                                        
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      12  2026-10-11,candidate-triage,haiku,attempt1/batch_08,114325,30,7
          18.5,failed
      13  2026-10-11,candidate-triage,haiku,attempt1/batch_09,110833,22,7
          12.3,failed
      14  2026-10-12,candidate-triage,haiku,batch_02,60054,37,114.3,ok
      15 +2026-10-12,candidate-triage,haiku,batch_03,67124,44,161.4,ok   

⏺ Agent "Triage batch 01" finished · 2m 54s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-12,candidate-triage,haiku,batch_01,66963,46,173.8,rerun" >>
      data/runs/run_log.csv)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      13  2026-10-11,candidate-triage,haiku,attempt1/batch_09,110833,22,7
          12.3,failed
      14  2026-10-12,candidate-triage,haiku,batch_02,60054,37,114.3,ok
      15  2026-10-12,candidate-triage,haiku,batch_03,67124,44,161.4,ok
      16 +2026-10-12,candidate-triage,haiku,batch_01,66963,46,173.8,rerun

⏺ 2 background agents launched (↓ to manage)
   ├ Triage batch 01 rerun
   └ Triage batch 05
  Ran 1 shell command (ctrl+o to expand)

⏺ Committed and pushed. Batch 04, batch 05 and the batch 01 rerun are now in
  progress; I'll pick up when they report.

✻ Baked for 19s · done Monday 5:09 PM

› Message from candidate-triage
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/candidates/triage/batch_04.csv: 25 rows, in input order.
  Unknown: 14 hq_country and 5 investor_type. Snippet evidence: 4 rows
  (fivesquare, gain-ventures, goldman-sachs-alternatives, grouport-ventures).
  Possible Czech VCs I was unsure of: gi21-capital (Prague per scout only, page
  does not say where), impulse-ventures (Czech roots, Tomek-backed, own site not
  fetched), fivesquare (Seedtable name only). Also note
  founder-institute-prague (Prague chapter, team country not stated) and ftmo
  (CZ, but not_an_investor vs cvc is borderline).
  Not run: run_log.csv entry (no token or duration figures available to me).

⏺ Batch 04 has 14/25 with hq unknown, which is over a third, so I'm re-running
  it once.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && mv
      data/candidates/triage/batch_04.csv
      data/candidates/triage/rerun_first/batch_04.csv && ls data/candid…)
  ⎿  batch_01.csv
     batch_04.csv
  ⎿  Deleted data/candidates/triage/batch_04.csv (+0 -26)
       1 -candidate_id,website,hq_country,investor_type,equity_investor,e
         -vidence_url,evidence_kind,evidence_quote,evidence_date,confiden
         -ce,note                                                        
       2 -fifth-wall,https://www.fifthwall.com,unknown,vc,yes,https://www
         -.fifthwall.com,page,"The largest investment firm focused on tec
         -hnology for the built environment, founded by Brendan Wallace",
         -,medium,"Team location not on the page; US is scout prior knowl
         -edge only. Page shows about $3B AUM. No date on page."         
       3 -fil-rouge-capital,https://filrougecapital.com,unknown,vc,yes,ht
         -tps://filrougecapital.com,page,"investment fund manager whose f
         -unds focus on early stage businesses from pre-seed, seed, and S
         -eries A rounds of investment",,medium,"Page shows only the Luxe
         -mbourg legal address of FRC Fund Management S.a.r.l. Zagreb/Cro
         -atia comes from search summaries, not from a fetched page. Foot
         -er copyright 2025."                                            
       4 -fivesquare,,unknown,unknown,unknown,https://seedtable.com/ranki
         -ngs/investors/country/Czech%20Republic,snippet,,,low,"Search sn
         -ippet only (page not fetched): Seedtable Czech ranking lists Fi
         -vesquare S.R.O. as type Other. No website, team location or act
         -ivity found."                                                  
       5 -forward-one,https://www.forward.one,NL,vc,yes,https://www.forwa
         -rd.one,page,"Dorpsstraat 28, 1182 JD Amstelveen, the Netherland
         -s",,medium,"Location is the office address on the page. Type fr
         -om the page: 'Performance-engineered venture capital.' Footer c
         -opyright 2026, no publication date."                           
       6 -founder-institute-prague,,unknown,accelerator,unknown,https://f
         -i.co/insight/silicon-valley-based-founder-institute-officially-
         -launches-new-startup-program-in-prague,page,"the world’s premie
         -r pre-seed startup accelerator",2018-11-21,medium,"Accelerator 
         -type. Team country not stated; the page is the global Silicon V
         -alley-based programme announcing Prague. Equity terms not on fe
         -tched page (search summary mentions about 2.5% warrant pool, un
         -verified). Page dated 2018."                                   
       7 -ftmo,https://www.ftmo.com,CZ,not_an_investor,yes,https://www.lu
         -pa.cz/aktuality/ceske-ftmo-posila-milion-dolaru-do-americkeho-k
         -rypto-jednorozce/,page,"Česká technologická společnost FTMO",20
         -25-10-06,medium,"Czech company (legal name FTMO s.r.o. on ftmo.
         -com). Operating prop-trading firm, not a fund. Minority stake i
         -n Zerohash (Oct 2025) per Lupa; OANDA acquisition (Dec 2025) pe
         -r search summary. Type borderline between not_an_investor and c
         -vc; for decide.py review."                                     
       8 -gain-ventures,,unknown,unknown,unknown,https://www.cbinsights.c
         -om/investor/gain-ventures,snippet,,,low,"Search snippet only (n
         -ot fetched). CB Insights snippet lists a seed round in Carebot 
         -dated 2024-03-22 and a Coronado, California base; Round Funded 
         -snippet says Seattle. Identity unresolved; no website found."  
       9 -garage-angels,https://g-angels.cz,CZ,angel,yes,https://g-angels
         -.cz,page,"Jsme neformální uskupení individuálních investorů.",,
         -medium,"Angel club (informal group of individual investors). Lo
         -cation is inferred from the Czech-language site and a Brno refe
         -rence only; no address on page. Footer copyright 2026, no publi
         -cation date."                                                  
      10 -genesis-capital,https://www.genesis.cz,CZ,pe,yes,https://www.ge
         -nesis.cz,page,"Na Šafránce 22, 101 00 Praha 10, Czech Republic"
         -,,medium,"Location is the listed office address. Type from the 
         -page (Czech text, private equity and growth equity in Czech SME
         -s and mid-sized firms; verify quote). Footer copyright 2026. CV
         -CA name Genesis Capital Equity s.r.o. per scout."              
      11 -gi21-capital,https://www.gi21capital.com,unknown,vc,yes,https:/
         -/www.gi21capital.com,page,"Backing technical founders solving c
         -omplex problems through Deep Tech, B2B SaaS, AI.",,low,"Page ca
         -lls itself a 'multi-stage investment group' and also holds hote
         -ls and arts; could be a private_holding of one person (scout: f
         -und of Damir Spoljaric). No team location on page; Prague per s
         -cout/Lupa not confirmed. Footer copyright 2025."               
      12 -goldman-sachs-alternatives,,US,pe,yes,https://en.wikipedia.org/
         -wiki/Goldman_Sachs_Alternatives,snippet,,,low,"Not fetched: gol
         -dmansachs.com returned HTTP 403. Search snippets say New York (
         -200 West Street) and cover private equity and growth equity. We
         -bsite not verified."                                           
      13 -google-ventures,https://www.gv.com,unknown,unknown,unknown,http
         -s://www.gv.com,page,"GV (Google Ventures)",,low,"Page shows onl
         -y the name and 'EST. 2009'; no team location, type or investmen
         -t activity. Corporate VC of Alphabet is scout prior knowledge, 
         -not on the page."                                              
      14 -grouport-ventures,,unknown,unknown,unknown,https://nordic9.com/
         -companies/grouport-ventures/,snippet,,,low,"Not fetched: groupo
         -rt.cz certificate expired. Directory snippets describe an early
         --stage investor, but locations conflict across directories. See
         -dtable Czech ranking is the only scout lead."                  
      15 -harbourvest-partners,https://www.harbourvest.com,unknown,pe,yes
         -,https://www.harbourvest.com,page,"an independent, global priva
         -te markets firm with 40+ years of experience.",,low,"Page lists
         - about 30 countries but no HQ. Fund-of-funds, secondaries or PE
         - not stated on page, so pe is a low-confidence label. Consider 
         -lp_only if the check confirms fund-of-funds. Mews investment fr
         -om scout lead, unverified."                                    
      16 -hartenberg,,unknown,private_holding,yes,https://www.e15.cz/doma
         -ci/babis-ve-stretu-zajmu-hartenberg-neni-investicni-fond-minist
         -r-ma-na-nej-vliv-1325985,page,"Fond Hartenberg, který investuje
         - do zdravotnictví peníze ministra financí",2016-11-29,medium,"I
         -nvestment group tied to Andrej Babiš (e15 article: Hartenberg H
         -olding is a subsidiary of SynBiol, which Babiš fully owns). Buy
         -s majority stakes per Newstream snippets. Team location not on 
         -fetched page; CZ not confirmed."                               
      17 -headline,,unknown,unknown,unknown,https://webroker.vc/domain/HE
         -ADLINE.VC,page,,,low,"headline.vc redirects to a domain-sale li
         -sting (webroker.vc), not the fund's own site; no quote used. Sc
         -out lead (Upheal Series A, Awards 2025) not verified on any fet
         -ched page. No type or team location found."                    
      18 -henq-capital-partners,https://henq.vc,NL,vc,yes,https://henq.vc
         -/,page,"We're henQ, the venture capital fund for B2B startups."
         -,,medium,"Team location from Dutch RVO fund listing (henQ Capit
         -al Partners B.V., Herengracht 124-128 Amsterdam, checked 2025-0
         -4-17; https://www.rvo.nl/subsidies-financiering/seed-capital/to
         -taaloverzicht-fondsen/henq-iii-seed-fund-bv), not on henq.vc. P
         -age has no office address. Copyright 2026."                    
      19 -i-and-i-biotech,https://www.inibio.eu,CZ,vc,yes,https://www.ini
         -bio.eu,page,"one of the very few VC funds in Europe focused exc
         -lusively on life science ventures",,medium,"Fund domiciled in L
         -uxembourg (L-2661). Investment adviser Biotech Investments, s. 
         -r. o. is in Prague, so the team is treated as CZ. Team members 
         -not named on page. Footer copyright 2026."                     
      20 -i-and-i-prague,https://www.iniprague.com,CZ,accelerator,unknown
         -,https://www.iniprague.com,page,"We are a biotech incubator and
         - venture builder, helping groundbreaking ideas leap from lab to
         - market.",,medium,"Incubator and venture builder at Pobřežní 39
         -4/12, 186 00 Prague. Equity terms not stated on page, so equity
         -_investor unknown. Footer 2022, no publication date. Separate V
         -C vehicle i&i Biotech Fund is covered in its own row."         
      21 -impulse-ventures,,unknown,vc,yes,https://cc.cz/mame-pro-startup
         -y-ve-stredni-evrope-ctyri-miliardy-korun-hlasi-novy-cesky-fond-
         -stoji-za-nim-ondrej-tomek-a-spol/,page,"nově zformovaném fondu 
         -Impulse Ventures",2020-09-08,low,"Own site not fetched (certifi
         -cate error on impulseventures.com). Article: fund backed by Ond
         -řej Tomek and colleagues, invests own capital, managing partner
         - Samuel Huba; could be private_holding. Team location not state
         -d; article says team has Czech roots and portfolio in CZ and PL
         -. Possible Czech VC, check manually."                          
      22 -incomming-ventures,,CZ,vc,yes,https://www.finmag.cz/obchodni-re
         -jstrik/04991087-incomming-ventures-a-s,page,"Bílkova 855/19, 11
         -0 00 Praha - Staré Město",,medium,"Registered seat in Praha per
         - Czech business register (INCOMMING ventures a.s., IČO 04991087
         -). Type from cc.cz 2017-07-12: 'Jednou z mladších investičních 
         -firem na českém trhu je INCOMMING Ventures'; invests in startup
         -s, mainly e-commerce. No website found. Team location inferred 
         -from registry seat."                                           
      23 -index-ventures,https://www.indexventures.com,unknown,vc,yes,htt
         -ps://www.indexventures.com,page,"We back visionaries across ind
         -ustries.",,medium,"Page lists offices in San Francisco, New Yor
         -k and London; no HQ stated. GB in scout is prior knowledge. Foo
         -ter copyright 2026, no publication date."                      
      24 -innova-capital,https://www.innovacap.com,PL,pe,yes,https://www.
         -innovacap.com,page,"independent private equity firm established
         - in 1994 in Poland",,medium,"Type from the page: investing in c
         -ontrolling stakes of mid-sized companies in the CEE region. Tea
         -m location not explicitly stated; Warsaw per CVCA (scout, not o
         -n page). Footer 2022; news items dated 2025 and 2026."         
      25 -inovo-venture-partners,https://inovo.vc,PL,vc,yes,https://inovo
         -.vc,page,"We're Inovo, a seed-stage VC focused on CEE founders.
         -",,medium,"Page says 'remote first' with offices in Warsaw, Ams
         -terdam and Luxembourg; HQ not stated. PL from the Warsaw office
         - and search summaries (Warsaw-based). Fund vintages 2014, 2018,
         - 2022 on page. No publication date."                           
      26 -insight-partners,https://www.insightpartners.com,unknown,vc,yes
         -,https://www.insightpartners.com,page,"the industry's most expe
         -rienced late-stage software experts",,low,"Page says it works a
         -cross stages, from early to late; quote supports late-stage onl
         -y. Growth-equity label possible (pe). Office locations not on p
         -age; New York per scout (Lupa) not verified. Footer copyright 2
         -026."                                                          
  ⎿  Created data/candidates/triage/rerun_first/batch_04.csv (+26 -0)
       1 +candidate_id,website,hq_country,investor_type,equity_investor,e
         +vidence_url,evidence_kind,evidence_quote,evidence_date,confiden
         +ce,note                                                        
       2 +fifth-wall,https://www.fifthwall.com,unknown,vc,yes,https://www
         +.fifthwall.com,page,"The largest investment firm focused on tec
         +hnology for the built environment, founded by Brendan Wallace",
         +,medium,"Team location not on the page; US is scout prior knowl
         +edge only. Page shows about $3B AUM. No date on page."         
       3 +fil-rouge-capital,https://filrougecapital.com,unknown,vc,yes,ht
         +tps://filrougecapital.com,page,"investment fund manager whose f
         +unds focus on early stage businesses from pre-seed, seed, and S
         +eries A rounds of investment",,medium,"Page shows only the Luxe
         +mbourg legal address of FRC Fund Management S.a.r.l. Zagreb/Cro
         +atia comes from search summaries, not from a fetched page. Foot
         +er copyright 2025."                                            
       4 +fivesquare,,unknown,unknown,unknown,https://seedtable.com/ranki
         +ngs/investors/country/Czech%20Republic,snippet,,,low,"Search sn
         +ippet only (page not fetched): Seedtable Czech ranking lists Fi
         +vesquare S.R.O. as type Other. No website, team location or act
         +ivity found."                                                  
       5 +forward-one,https://www.forward.one,NL,vc,yes,https://www.forwa
         +rd.one,page,"Dorpsstraat 28, 1182 JD Amstelveen, the Netherland
         +s",,medium,"Location is the office address on the page. Type fr
         +om the page: 'Performance-engineered venture capital.' Footer c
         +opyright 2026, no publication date."                           
       6 +founder-institute-prague,,unknown,accelerator,unknown,https://f
         +i.co/insight/silicon-valley-based-founder-institute-officially-
         +launches-new-startup-program-in-prague,page,"the world’s premie
         +r pre-seed startup accelerator",2018-11-21,medium,"Accelerator 
         +type. Team country not stated; the page is the global Silicon V
         +alley-based programme announcing Prague. Equity terms not on fe
         +tched page (search summary mentions about 2.5% warrant pool, un
         +verified). Page dated 2018."                                   
       7 +ftmo,https://www.ftmo.com,CZ,not_an_investor,yes,https://www.lu
         +pa.cz/aktuality/ceske-ftmo-posila-milion-dolaru-do-americkeho-k
         +rypto-jednorozce/,page,"Česká technologická společnost FTMO",20
         +25-10-06,medium,"Czech company (legal name FTMO s.r.o. on ftmo.
         +com). Operating prop-trading firm, not a fund. Minority stake i
         +n Zerohash (Oct 2025) per Lupa; OANDA acquisition (Dec 2025) pe
         +r search summary. Type borderline between not_an_investor and c
         +vc; for decide.py review."                                     
       8 +gain-ventures,,unknown,unknown,unknown,https://www.cbinsights.c
         +om/investor/gain-ventures,snippet,,,low,"Search snippet only (n
         +ot fetched). CB Insights snippet lists a seed round in Carebot 
         +dated 2024-03-22 and a Coronado, California base; Round Funded 
         +snippet says Seattle. Identity unresolved; no website found."  
       9 +garage-angels,https://g-angels.cz,CZ,angel,yes,https://g-angels
         +.cz,page,"Jsme neformální uskupení individuálních investorů.",,
         +medium,"Angel club (informal group of individual investors). Lo
         +cation is inferred from the Czech-language site and a Brno refe
         +rence only; no address on page. Footer copyright 2026, no publi
         +cation date."                                                  
      10 +genesis-capital,https://www.genesis.cz,CZ,pe,yes,https://www.ge
         +nesis.cz,page,"Na Šafránce 22, 101 00 Praha 10, Czech Republic"
         +,,medium,"Location is the listed office address. Type from the 
         +page (Czech text, private equity and growth equity in Czech SME
         +s and mid-sized firms; verify quote). Footer copyright 2026. CV
         +CA name Genesis Capital Equity s.r.o. per scout."              
      11 +gi21-capital,https://www.gi21capital.com,unknown,vc,yes,https:/
         +/www.gi21capital.com,page,"Backing technical founders solving c
         +omplex problems through Deep Tech, B2B SaaS, AI.",,low,"Page ca
         +lls itself a 'multi-stage investment group' and also holds hote
         +ls and arts; could be a private_holding of one person (scout: f
         +und of Damir Spoljaric). No team location on page; Prague per s
         +cout/Lupa not confirmed. Footer copyright 2025."               
      12 +goldman-sachs-alternatives,,US,pe,yes,https://en.wikipedia.org/
         +wiki/Goldman_Sachs_Alternatives,snippet,,,low,"Not fetched: gol
         +dmansachs.com returned HTTP 403. Search snippets say New York (
         +200 West Street) and cover private equity and growth equity. We
         +bsite not verified."                                           
      13 +google-ventures,https://www.gv.com,unknown,unknown,unknown,http
         +s://www.gv.com,page,"GV (Google Ventures)",,low,"Page shows onl
         +y the name and 'EST. 2009'; no team location, type or investmen
         +t activity. Corporate VC of Alphabet is scout prior knowledge, 
         +not on the page."                                              
      14 +grouport-ventures,,unknown,unknown,unknown,https://nordic9.com/
         +companies/grouport-ventures/,snippet,,,low,"Not fetched: groupo
         +rt.cz certificate expired. Directory snippets describe an early
         +-stage investor, but locations conflict across directories. See
         +dtable Czech ranking is the only scout lead."                  
      15 +harbourvest-partners,https://www.harbourvest.com,unknown,pe,yes
         +,https://www.harbourvest.com,page,"an independent, global priva
         +te markets firm with 40+ years of experience.",,low,"Page lists
         + about 30 countries but no HQ. Fund-of-funds, secondaries or PE
         + not stated on page, so pe is a low-confidence label. Consider 
         +lp_only if the check confirms fund-of-funds. Mews investment fr
         +om scout lead, unverified."                                    
      16 +hartenberg,,unknown,private_holding,yes,https://www.e15.cz/doma
         +ci/babis-ve-stretu-zajmu-hartenberg-neni-investicni-fond-minist
         +r-ma-na-nej-vliv-1325985,page,"Fond Hartenberg, který investuje
         + do zdravotnictví peníze ministra financí",2016-11-29,medium,"I
         +nvestment group tied to Andrej Babiš (e15 article: Hartenberg H
         +olding is a subsidiary of SynBiol, which Babiš fully owns). Buy
         +s majority stakes per Newstream snippets. Team location not on 
         +fetched page; CZ not confirmed."                               
      17 +headline,,unknown,unknown,unknown,https://webroker.vc/domain/HE
         +ADLINE.VC,page,,,low,"headline.vc redirects to a domain-sale li
         +sting (webroker.vc), not the fund's own site; no quote used. Sc
         +out lead (Upheal Series A, Awards 2025) not verified on any fet
         +ched page. No type or team location found."                    
      18 +henq-capital-partners,https://henq.vc,NL,vc,yes,https://henq.vc
         +/,page,"We're henQ, the venture capital fund for B2B startups."
         +,,medium,"Team location from Dutch RVO fund listing (henQ Capit
         +al Partners B.V., Herengracht 124-128 Amsterdam, checked 2025-0
         +4-17; https://www.rvo.nl/subsidies-financiering/seed-capital/to
         +taaloverzicht-fondsen/henq-iii-seed-fund-bv), not on henq.vc. P
         +age has no office address. Copyright 2026."                    
      19 +i-and-i-biotech,https://www.inibio.eu,CZ,vc,yes,https://www.ini
         +bio.eu,page,"one of the very few VC funds in Europe focused exc
         +lusively on life science ventures",,medium,"Fund domiciled in L
         +uxembourg (L-2661). Investment adviser Biotech Investments, s. 
         +r. o. is in Prague, so the team is treated as CZ. Team members 
         +not named on page. Footer copyright 2026."                     
      20 +i-and-i-prague,https://www.iniprague.com,CZ,accelerator,unknown
         +,https://www.iniprague.com,page,"We are a biotech incubator and
         + venture builder, helping groundbreaking ideas leap from lab to
         + market.",,medium,"Incubator and venture builder at Pobřežní 39
         +4/12, 186 00 Prague. Equity terms not stated on page, so equity
         +_investor unknown. Footer 2022, no publication date. Separate V
         +C vehicle i&i Biotech Fund is covered in its own row."         
      21 +impulse-ventures,,unknown,vc,yes,https://cc.cz/mame-pro-startup
         +y-ve-stredni-evrope-ctyri-miliardy-korun-hlasi-novy-cesky-fond-
         +stoji-za-nim-ondrej-tomek-a-spol/,page,"nově zformovaném fondu 
         +Impulse Ventures",2020-09-08,low,"Own site not fetched (certifi
         +cate error on impulseventures.com). Article: fund backed by Ond
         +řej Tomek and colleagues, invests own capital, managing partner
         + Samuel Huba; could be private_holding. Team location not state
         +d; article says team has Czech roots and portfolio in CZ and PL
         +. Possible Czech VC, check manually."                          
      22 +incomming-ventures,,CZ,vc,yes,https://www.finmag.cz/obchodni-re
         +jstrik/04991087-incomming-ventures-a-s,page,"Bílkova 855/19, 11
         +0 00 Praha - Staré Město",,medium,"Registered seat in Praha per
         + Czech business register (INCOMMING ventures a.s., IČO 04991087
         +). Type from cc.cz 2017-07-12: 'Jednou z mladších investičních 
         +firem na českém trhu je INCOMMING Ventures'; invests in startup
         +s, mainly e-commerce. No website found. Team location inferred 
         +from registry seat."                                           
      23 +index-ventures,https://www.indexventures.com,unknown,vc,yes,htt
         +ps://www.indexventures.com,page,"We back visionaries across ind
         +ustries.",,medium,"Page lists offices in San Francisco, New Yor
         +k and London; no HQ stated. GB in scout is prior knowledge. Foo
         +ter copyright 2026, no publication date."                      
      24 +innova-capital,https://www.innovacap.com,PL,pe,yes,https://www.
         +innovacap.com,page,"independent private equity firm established
         + in 1994 in Poland",,medium,"Type from the page: investing in c
         +ontrolling stakes of mid-sized companies in the CEE region. Tea
         +m location not explicitly stated; Warsaw per CVCA (scout, not o
         +n page). Footer 2022; news items dated 2025 and 2026."         
      25 +inovo-venture-partners,https://inovo.vc,PL,vc,yes,https://inovo
         +.vc,page,"We're Inovo, a seed-stage VC focused on CEE founders.
         +",,medium,"Page says 'remote first' with offices in Warsaw, Ams
         +terdam and Luxembourg; HQ not stated. PL from the Warsaw office
         + and search summaries (Warsaw-based). Fund vintages 2014, 2018,
         + 2022 on page. No publication date."                           
      26 +insight-partners,https://www.insightpartners.com,unknown,vc,yes
         +,https://www.insightpartners.com,page,"the industry's most expe
         +rienced late-stage software experts",,low,"Page says it works a
         +cross stages, from early to late; quote supports late-stage onl
         +y. Growth-equity label possible (pe). Office locations not on p
         +age; New York per scout (Lupa) not verified. Footer copyright 2
         +026."                                                          

⏺ candidate-triage(Triage batch 04 rerun)
  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)

⏺ Agent "Triage batch 04" finished · 3m 27s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-12,candidate-triage,haiku,batch_04,73436,49,207.3,rerun" >>
      data/runs/run_log.csv)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      14  2026-10-12,candidate-triage,haiku,batch_02,60054,37,114.3,ok
      15  2026-10-12,candidate-triage,haiku,batch_03,67124,44,161.4,ok
      16  2026-10-12,candidate-triage,haiku,batch_01,66963,46,173.8,rerun
      17 +2026-10-12,candidate-triage,haiku,batch_04,73436,49,207.3,rerun

⏺ I've logged the first batch 04 run. Three agents are now running: the batch 01
  rerun, batch 04 rerun and batch 05.

✻ Cogitated for 9s · done Monday 5:12 PM

› Message from candidate-triage
  Rows written: 25 to /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/candidates/triage/batch_05.csv, one per input candidate, in input
  order.
  Unknown: 9 team countries (hq_country) and 6 investor types. Snippet-only
  evidence: 8 rows (ip-lab-ventures, ipm, irregular-expressions,
  itaca-business-incubator, jafam-holding, jinej-fond, kendaxa-group,
  lead-ventures).
  Possible Czech VCs I was unsure of: ip-lab-ventures (Czech state-backed fund,
  team country not confirmed) and kaya-vc (Prague office listed, but no HQ on
  the page).

  Caveats: quotes come from WebFetch output, which is a model summary, so they
  still need verbatim checking by src/check_quotes.py. The Invera row is backed
  by a tportal.hr article because inveraep.com was not reachable. The Jet
  Investment row uses the Brno office address as its quote.

  Sources: https://integralcapgroup.com, https://www.invencapital.cz,
  https://www.tportal.hr/biznis/clanak/invera-equity-partners-prikupio-160-milij
  una-eura-za-fond-ii-20260427, https://www.investown.cz,
  https://www.jtventures.cz, https://www.jetinvestment.cz/en,
  https://www.jic.cz/ventures/, https://www.jskinvestments.cz,
  https://www.kaya.vc, https://kkcg.com, https://www.jtis.cz/fond/A2PCA,
  https://www.koopeoventures.com, https://www.kpnventures.com,
  https://www.kinnevik.com, https://www.czechinvest.gov.cz/en/Homepage/News/Apri
  l-2017/On-global-trends-in-angel-investing-with-Randy-Williams,
  https://cc.cz/bicykly-jedou-jaroslav-beck-a-robert-kyncl-posilaji-pres-10-mili
  onu-do-ceskeho-projektu-outfindo/, https://www.e15.cz/kryptomeny/do-sveta-kryp
  tomen-vstupuje-dalsi-cesky-miliardar-ondrej-tomek-rozjizdi-novy-fond-1411749

⏺ Batch 05: 9/25 unknown, which is not over a third, so it's accepted. Launching
  batch 06.

⏺ candidate-triage(Triage batch 06)
  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)

⏺ Agent "Triage batch 05" finished · 2m 38s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-12,candidate-triage,haiku,batch_05,69225,41,157.7,ok" >>
      data/runs/run_log.csv)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      15  2026-10-12,candidate-triage,haiku,batch_03,67124,44,161.4,ok
      16  2026-10-12,candidate-triage,haiku,batch_01,66963,46,173.8,rerun
      17  2026-10-12,candidate-triage,haiku,batch_04,73436,49,207.3,rerun
      18 +2026-10-12,candidate-triage,haiku,batch_05,69225,41,157.7,ok   

⏺ I've logged batch 05. The batch 01 rerun, batch 04 rerun and batch 06 are
  still running.

✻ Worked for 6s · done Monday 5:12 PM

› Message from candidate-triage
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/candidates/triage/batch_01.csv: 25 rows, input order, header as
  specified.
  Unknown: 18 hq_country unknown, 10 investor_type unknown. Snippet evidence: 12
  rows (snippet only where no fetched page carries the location or type).
  Possible Czech VC, unsure: Look AI Ventures (LAIV, Vestbee page fetched: "the
  first investment fund in the Czech Republic focusing exclusively on
  early-stage AI startups", linked to the ai-startup-incubator candidate, not an
  input row). BD Partners (Prague per search snippet, type unresolved pe vs
  private_holding). BADideas.fund (Czech status not shown; page says only CEE).

⏺ The rerun came back worse: 18 hq unknown, against 14 in the first pass. I'll
  compare the two runs candidate by candidate before choosing which to keep.

  Ran 1 shell command (ctrl+o to expand)

⏺ Agent "Triage batch 01 rerun" finished · 2m 50s

⏺ Neither run is clearly better—the rerun fixed aspire11 and bd-partners but
  lost some foreign locations, while Accel and Battery Ventures remain unknown
  in both. Per the runbook I'll keep the rerun output (unknowns just go to the
  extraction queue, not excluded) and log this as an AI error plus decision.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-12,candidate-triage,haiku,batch_01_rerun,75977,57,170.0,ok" >>
      data/runs/run_log.csv && ca…)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      16  2026-10-12,candidate-triage,haiku,batch_01,66963,46,173.8,rerun
      17  2026-10-12,candidate-triage,haiku,batch_04,73436,49,207.3,rerun
      18  2026-10-12,candidate-triage,haiku,batch_05,69225,41,157.7,ok
      19 +2026-10-12,candidate-triage,haiku,batch_01_rerun,75977,57,170.0
         +,ok                                                            
  ⎿  Updated docs/ai-errors.md (+1 -0)
       9  | E-03 | 2026-10-11 | candidate-triage (všech 9 dávek) | 180 z 
          225 kandidátů | vše | Výsledek `unknown` u 80 % kandidátů. Příč
          ina je infrastrukturní: agenti v cloudovém prostředí sdílejí li
          mit 200 vyhledávání na jedno kolo konverzace (spotřebovali ho s
          couti) a stažení stránky, která nepřišla z výsledků vyhledávání
          , vyžaduje ruční schválení uživatelem, které nikdo nedal. | Sou
          hrn výstupu (`attempt1/`) a zprávy agentů. | Běh agentů přesunu
          t do Claude Code na mém počítači s projektovými oprávněními (`.
          claude/settings.json`), paralelismus snížen na 3–4, triáž poběž
          í znovu. Neúspěšný pokus zůstává v `data/candidates/triage/atte
          mpt1/`. |
      10  | E-04 | 2026-10-11 | candidate-triage (batch 06) | InCOMMing |
           — | Titulek výsledku vyhledávání (Dealroom) obsahoval instrukc
          i určenou jazykovým modelům (prompt injection). | Agent ji rozp
          oznal a ignoroval. | Nic; potvrzuje, že obsah stránek je třeba 
          brát jako data, ne jako pokyny. |
      11  | E-05 | 2026-10-11 | candidate-scout (cvca) | Tilia Impact Ven
          tures | `website` | Ne chyba AI, ale chyba ve zdroji: odkaz v p
          rofilu CVCA vede na skylimit.cz, ačkoli text uvádí tilia.vc. | 
          Agent si nesouladu všiml. | Použita doména tilia.vc; příklad to
          ho, proč ani asociační profil není tier-1 zdroj. |
      12 +| E-06 | 2026-10-12 | candidate-triage (batch 01, 04) | Accel, 
         +Battery Ventures, Atomico… | `hq_country` | Haiku nechal `unkno
         +wn` u sídla i zjevně zahraničních fondů (Accel, Battery Venture
         +s); u batch 01 a 04 byla neznámá země u 14/25. Opakovaný běh ba
         +tch 01 dopadl hůř (18/25) a mezi běhy se odpovědi liší (např. a
         +irbridge NL → unknown, aspire11 unknown → CZ). | Kontrola podíl
         +u `unknown` po dávce (runbook R1) a porovnání obou běhů. | Plat
         +í opakovaný běh (podle runbooku); první výstup je v `data/candi
         +dates/triage/rerun_first/`. `unknown` nevyřazuje, kandidát jde 
         +do fronty extrakce, takže chyba zvyšuje náklad, ne ztrátu kandi
         +dátů. |                                                        

⏺ candidate-triage(Triage batch 07)
  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)

⏺ Batch 07 is running alongside the batch 04 rerun and batch 06. I've logged
  E-06 in docs/ai-errors.md.

✻ Sautéed for 19s · done Monday 5:12 PM

› Message from candidate-triage
  Wrote 25 rows to /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/candidates/triage/batch_06.csv (input order, header included).
  Unknown: 6 rows have an unknown field (longevity-fellows, new-vision-3,
  np-investments and muni-ventures have unknown type or HQ; mid-europa-partners
  and northzone have unknown HQ). Four rows have investor_type unknown.
  Snippet-only evidence: 11 rows (longevity-fellows, longevitytech-fund, lumus,
  metatron, muni-ventures, nato-diana, new-vision-3, novira-capital,
  np-investments, odyssey-44, one-peak). Quotes are empty for these, and their
  summaries are not verbatim.
  Possible Czech VCs I am unsure of: novira-capital (CZ vc, snippet only,
  businessinfo returned 403), longevitytech-fund (CZ vc, snippet only), miton
  (CZ, vc vs private_holding unclear). Also note neulogy-ventures rests on an
  aggregator page (Vestbee), not its own site.

⏺ Batch 06 has 6/25 unknown, so no rerun is needed. Launching batch 08.

⏺ candidate-triage(Triage batch 08)
  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)

⏺ Agent "Triage batch 06" finished · 2m 15s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-12,candidate-triage,haiku,batch_06,61319,40,134.9,ok" >>
      data/runs/run_log.csv)  ⎿  Updated data/runs/run_log.csv (+1 -0)
      17  2026-10-12,candidate-triage,haiku,batch_04,73436,49,207.3,rerun
      18  2026-10-12,candidate-triage,haiku,batch_05,69225,41,157.7,ok
      19  2026-10-12,candidate-triage,haiku,batch_01_rerun,75977,57,170.0
          ,ok
      20 +2026-10-12,candidate-triage,haiku,batch_06,61319,40,134.9,ok   

⏺ I've logged batch 06. Still running: batch 04 rerun, batch 07 and batch 08.
  Batch 09 is the last one left to start.

✻ Crunched for 6s · done Monday 5:14 PM

› Message from candidate-triage
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/candidates/triage/batch_07.csv: 25 rows, input order.
  12 rows have unknown hq_country or investor_type (partech, patero,
  pilulka-lab, point-nine, presto-ventures, proxy-finance,
  qi-investicni-spolecnost, riverside-acceleration-capital, rockawayx,
  rsj-investments, rtp-global, safar-and-partners). 6 rows are snippet-only
  (orizon-systems, patero, pilulka-lab, proxy-finance, rtp-global,
  safar-and-partners).
  Possible Czech VCs I am not sure of: presto-ventures (Tech Horizons page shows
  only a Luxembourg registered office, team not shown), qq-capital (Prague
  family venture office, profile labelled VC, only an aggregator page),
  rockaway-ventures (fund seat Luxembourg, team location not stated), rockawayx
  (Prague office but no HQ named).
  Quotes come from WebFetch summaries, not raw page text, so check_quotes must
  verify them. seed-starter and seed-starter-ceske-sporitelny share one operator
  and one URL (dedupe downstream). No run_log row written.

  Ran 1 shell command (ctrl+o to expand)

⏺ Agent "Triage batch 07" finished · 2m 26s

⏺ I realize I misjudged batches 05 and 07 earlier—both exceed the one-third
  unknown hq_country threshold (9/25 and 10/25). Applying the rule consistently,
  I'll rerun both now.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-12,candidate-triage,haiku,batch_07,69691,43,146.5,rerun" >>
      data/runs/run_log.csv && .venv…)
  ⎿  Deleted data/candidates/triage/batch_05.csv (+0 -26)
       1 -candidate_id,website,hq_country,investor_type,equity_investor,e
         -vidence_url,evidence_kind,evidence_quote,evidence_date,confiden
         -ce,note                                                        
       2 -integral-capital-group,https://integralcapgroup.com,unknown,pe,
         -yes,https://integralcapgroup.com,page,"the leading mid-market p
         -rivate equity platform in Central and Eastern Europe",2026-08-2
         -0,medium,"Team hubs London, Budapest, Belgrade; GP office Luxem
         -bourg; no single team HQ on page. Integral Venture Partners (VC
         - arm) not checked."                                            
       3 -inven-capital,https://www.invencapital.cz,CZ,vc,yes,https://www
         -.invencapital.cz,page,"As a venture capital fund we invest EUR 
         -500m from institutional investors and global corporates",,mediu
         -m,"Office Pod Krizkem 1773/2, Praha 4. CEZ name only in footer;
         - no explicit corporate VC wording on page, so vc not cvc."     
       4 -invera,,HR,pe,yes,https://www.tportal.hr/biznis/clanak/invera-e
         -quity-partners-prikupio-160-milijuna-eura-za-fond-ii-20260427,p
         -age,"upravitelj alternativnih investicijskih fondova iz Zagreba
         -",2026-04-27,high,"Candidate is Invera PE fund; manager Invera 
         -Equity Partners, Zagreb. Page: private equity manager for SE Eu
         -rope, controlling stakes. Quote is Croatian from WebFetch outpu
         -t. inveraep.com not reachable."                                
       5 -investown,https://www.investown.cz,CZ,platform,no,https://www.i
         -nvestown.cz,page,"Investown je online platforma s investičními 
         -úvěry do nemovitostí.",,medium,"Real-estate loan platform (lend
         -ing/crowd). CZ inferred from CZK, ČNB licence line and Investow
         -n Technologies s.r.o.; no address seen. Future blog dates ignor
         -ed."                                                           
       6 -ip-lab-ventures,,unknown,vc,yes,https://www.businessinfo.cz/cla
         -nky/prvni-cesky-fond-na-transfer-technologii-zamereny-na-aplika
         -ce-ai-a-dalsi-pokrocile-technologie-investuje-do-komercionaliza
         -ce-vyzkumu-temer-miliardu/,snippet,,,low,"businessinfo.cz retur
         -ned 403; type from search summary (pre-seed to Series A, Czech 
         -technology-transfer fund). e15 page fetched but gives no team l
         -ocation or stage. Likely Czech, unconfirmed."                  
       7 -ipm,,CZ,unknown,yes,https://globalprivatecapital.org/?p=34494,s
         -nippet,,,low,"Snippet: IPM Group, a Prague-based asset manager,
         - led Photoneo USD 21m Series B (Dec 2021). Investor type not st
         -ated; short name ambiguous."                                   
       8 -irregular-expressions,,US,vc,yes,https://f4.fund/firms/irregula
         -r-expressions,snippet,,,low,"f4.fund returned 403; snippet: New
         - York-based pre-seed/seed fund. Example: TopK seed Jul 2025 wit
         -h Earlybird and KAYA."                                         
       9 -itaca-business-incubator,,unknown,unknown,unknown,,snippet,,,lo
         -w,"No search result for an ITACA incubator; Vestbee link not co
         -nfirmed. Triage type other is not a valid value, so unknown."  
      10 -ivbf,,unknown,unknown,no,https://www.e15.cz/kryptomeny/do-sveta
         --kryptomen-vstupuje-dalsi-cesky-miliardar-ondrej-tomek-rozjizdi
         --novy-fond-1411749,page,"smartkontraktové blockchainy",2023-11-
         -22,low,"Crypto-asset fund (smart-contract blockchains, staked e
         -ther), not a startup investor, so not vc. Team location not sta
         -ted. Article dated 2023-11-22."                                
      11 -j-t-arch,https://www.jtis.cz/fond/A2PCA,unknown,pe,yes,https://
         -www.jtis.cz/fond/A2PCA,page,"především z oblasti private equity
         -",2026-04-28,medium,"Qualified-investor fund of J&T INVESTIČNÍ 
         -SPOLEČNOST, a.s. Manager location not on page. Date is fund act
         -ivity date 28. 4. 2026."                                       
      12 -j-t-ventures,https://www.jtventures.cz,CZ,vc,yes,https://www.jt
         -ventures.cz,page,"Pre-seed až Series A",,high,"Office in Prague
         - (Karlin) in J&T Banka building. Focus CEE and SEE. Only copyri
         -ght 2024 on page."                                             
      13 -jafam-holding,,DE,unknown,unknown,https://lei.bloomberg.com/lei
         -s/view/875500IXO6D2T7TPKN04,snippet,,,low,"Bloomberg LEI record
         - (snippet): active German GmbH, registered address Herrsching, 
         -Bavaria. No business description found."                       
      14 -jaro-capital,,unknown,angel,yes,https://cc.cz/bicykly-jedou-jar
         -oslav-beck-a-robert-kyncl-posilaji-pres-10-milionu-do-ceskeho-p
         -rojektu-outfindo/,page,"JARO Capital, za nímž stojí Jaroslav Be
         -ck a Robert Kyncl",2021-07-14,low,"Vehicle of two individuals d
         -oing pre-seed deals; borderline angel vs private_holding. Team 
         -country not stated in article."                                
      15 -jet-investment,https://www.jetinvestment.cz,CZ,pe,yes,https://w
         -ww.jetinvestment.cz/en,page,"Pisárecká 271/13, 634 00 Brno-stře
         -d, Pisárky",,medium,"Quote is office address (Brno). Page lists
         - Private Equity, Real Estate and Venture Capital; calls itself 
         -a leading Central European investment company. pe per triage; r
         -eviewer should check venture arm. Redirect from jetinvestment.e
         -u."                                                            
      16 -jic-ventures,https://www.jic.cz/ventures/,CZ,vc,yes,https://www
         -.jic.cz/ventures/,page,"a Brno-born VC fund",,high,"Pre-seed an
         -d seed, tickets up to EUR 1M; managing partners Radim Kocourek 
         -and Miloš Sochor; office Purkynova 127, Brno."                 
      17 -jinej-fond,,unknown,unknown,unknown,,snippet,,,low,"Snippets on
         -ly: Jinej fond among HTG Medical pre-seed investors (Jul 2026 r
         -ound). No HQ, website or type found."                          
      18 -jsk-investments,https://www.jskinvestments.cz,CZ,private_holdin
         -g,yes,https://www.jskinvestments.cz,page,"projekty private equi
         -ty, growth equity a venture kapitálu",,medium,"Prague 1 (Klimen
         -tská 1216/46). Investment fund of the Kijonková couple; page do
         -es not call itself a family office, so private_holding by rule.
         - Reviewer may prefer family_office."                           
      19 -kaya-vc,https://www.kaya.vc,unknown,vc,yes,https://www.kaya.vc,
         -page,"We invest in ambitious & gritty founders from CEE",,mediu
         -m,"Page lists offices Warszawa, Prague, San Francisco, London; 
         -no HQ named, so team country unknown. Pre+Seed focus, USD 1-3M 
         -tickets. Prague 8 from triage not on page."                    
      20 -keiretsu-forum-prague,,CZ,angel,yes,https://www.czechinvest.gov
         -.cz/en/Homepage/News/April-2017/On-global-trends-in-angel-inves
         -ting-with-Randy-Williams,page,"a global investment community of
         - accredited angel investors, venture capitalists and corporate 
         -investors",2017-04-07,medium,"Prague branch active since autumn
         - 2015 per 2017 article. Old source; no current branch page foun
         -d."                                                            
      21 -kendaxa-group,,unknown,unknown,unknown,,snippet,,,low,"Search f
         -ound nothing on Kendaxa Group. Seedtable ranking is the only le
         -ad."                                                           
      22 -kinnevik,https://www.kinnevik.com,SE,vc,yes,https://www.kinnevi
         -k.com,page,"patient capital to challenger technology-enabled bu
         -sinesses in Europe and the US",,medium,"Stockholm office listed
         - first, London second; HQ not stated explicitly. Page does not 
         -use the label VC; vc per triage (Mews)."                       
      23 -kkcg,https://kkcg.com,CZ,private_holding,yes,https://kkcg.com,p
         -age,"an investment and innovation group operating a diverse ran
         -ge of companies",2026-10-09,high,"HQ building Evropská 866/71, 
         -Prague 6. Founder Karel Komárek. Invests own resources; page do
         -es not say family office. Date is page last modified."         
      24 -koopeo-ventures,https://www.koopeoventures.com,CZ,vc,yes,https:
         -//www.koopeoventures.com,page,"Investujeme do inovativních fire
         -m",,high,"HQ Solniční 243/17, Brno; offices Prague and Bratisla
         -va. Input said Prague, page says Brno. Early-stage venture; imp
         -act claim not on page. Copyright 2024 only."                   
      25 -kpn-ventures,https://www.kpnventures.com,NL,cvc,yes,https://www
         -.kpnventures.com,page,"Focus on early growth stage investments 
         -with relevance for KPN",,medium,"Offices Rotterdam and Amsterda
         -m, both NL; team location not stated. Page does not say corpora
         -te venture capital; cvc is an inference from the KPN link."    
      26 -lead-ventures,,HU,vc,yes,https://ceelm.com/czech-republic/25532
         --havel-partners-advises-lead-ventures-on-cloudtalk-investment,s
         -nippet,,,low,"Search summary: Budapest-based VC and PE firm tha
         -t co-led CloudTalk Series B (Jan 2024). ceelm page failed to fe
         -tch (certificate). Verify Budapest."                           
  ⎿  Deleted data/candidates/triage/batch_07.csv (+0 -26)
       1 -candidate_id,website,hq_country,investor_type,equity_investor,e
         -vidence_url,evidence_kind,evidence_quote,evidence_date,confiden
         -ce,note                                                        
       2 -orbit-capital,https://orbitcapital.com,CZ,vc,yes,https://vestbe
         -e.com/insights/articles/interview-with-orbit-capital,page,"Base
         -d in Prague and Warsaw, the fund offers both growth equity and 
         -debt financing",2024-08-20,medium,"Vestbee interview (Aug 2024)
         - fetched; own site shows only nav labels Growth Equity and Grow
         -th Debt, no location. Mixed equity plus venture debt: vc chosen
         - for scale-up equity, debt side may need lender treatment downs
         -tream. Warsaw office also named."                              
       3 -orizon-systems,,JP,not_an_investor,unknown,https://elioplus.com
         -/profiles/channel-partners/21585/orizon-systems,snippet,,,low,"
         -Search snippets only: Tokyo-based IT services firm, Kemp partne
         -r. Logmanager stake not found in any result. Website not identi
         -fied."                                                         
       4 -pale-fire-capital,https://palefirecapital.com,CZ,pe,yes,https:/
         -/palefirecapital.com,page,"Investujeme vlastní dlouhodobý kapit
         -ál, podnikatelskou zkušenost a technologické know-how.",,high,"
         -Footer address Žatecká 55/14, Praha 1. Invests own capital in e
         -stablished companies (stakes, hundreds of millions CZK). Not a 
         -seed VC."                                                      
       5 -partech,https://partechpartners.com,unknown,unknown,unknown,htt
         -ps://partechpartners.com,page,"Partech harnesses broad expertis
         -e from a collective of experts to deliver the best support for 
         -founders across the globe.",,low,"Homepage fetched: no fund typ
         -e, team location or office list. Paris datelines appear only on
         - news items and are not treated as team location. Own about pag
         -e returned 404."                                               
       6 -patero,,unknown,unknown,unknown,https://www.cbinsights.com/comp
         -any/patero/financials,snippet,,,low,"Only CB Insights snippet (
         -one investor, 5G Open Innovation Lab, incubator round Sep 2025)
         -. No website, entity nature unknown. Aggregator snippet is a le
         -ad only."                                                      
       7 -pilulka-lab,,CZ,unknown,unknown,https://www.cbinsights.com/inve
         -stor/pilulka-lab,snippet,,,low,"CB Insights snippet calls it a 
         -Prague-based venture firm (e-health); Carebot seed deal 2024 pe
         -r snippet. Own page www.pilulka.cz/lab returned 404. Type unres
         -olved (triage said cvc, page not seen)."                       
       8 -plug-and-play,,US,vc,yes,https://en.wikipedia.org/wiki/Plug_and
         -_Play_Tech_Center,page,"Plug and Play Tech Center (PNP) is an A
         -merican venture capital firm headquartered in Sunnyvale, Califo
         -rnia.",,medium,"Wikipedia fetched; brand homepage gave title on
         -ly. Also works as an accelerator (CB Insights ranking). Equity 
         -not stated, inferred from VC type. Other directory lists Umea, 
         -Sweden, judged an error."                                      
       9 -point-nine,https://www.pointnine.com,unknown,vc,yes,https://www
         -.pointnine.com,page,"a thesis-driven early-stage venture capita
         -l firm",,high,"Homepage says team is 'based in Europe', no city
         -. Berlin appears only in search snippets. DE guess from triage 
         -not evidenced on page."                                        
      10 -presto-ventures,https://www.techhorizons.eu,unknown,vc,yes,http
         -s://www.techhorizons.eu,page,"a venture capital fund backing de
         -fense, security, and resilience technology",,medium,"Tech Horiz
         -ons page fetched: only the fund vehicle's registered office (Te
         -ch Horizons GP S.a r.l., Capellen, Luxembourg) is shown, not th
         -e team. Presto Ventures team location not on fetched page; pres
         -toventures.com not fetched. POSSIBLE CZ VC: triage and Lupa sug
         -gest Prague, needs team page."                                 
      11 -proxy-finance,,CZ,unknown,unknown,https://seedtable.com/ranking
         -s/investors/country/Czech%20Republic,snippet,,,low,"Seedtable r
         -anking snippet lists Proxy-Finance A.S. with type PE and Prague
         - location. Aggregator lead only; no own site, deal history or d
         -escription found."                                             
      12 -purple-ventures,https://www.purple-ventures.com,CZ,vc,yes,https
         -://www.purple-ventures.com,page,"We are a venture capital fund 
         -investing into CEE+ tech-enabled innovations in pre-seed and se
         -ed stages.",,high,"Footer registered address Masarykova 26, 602
         - 00 Brno. Minority equity stakes, initial tickets EUR 250k-400k
         -. Page footer copyright 2025 only."                            
      13 -purposetech,,CZ,vc,unknown,https://siliconcanals.com/purposetec
         -h-closes-fund-to-support-cee-founders/,page,"PurposeTech is a p
         -re-seed venture capital fund that was launched in 2023 to suppo
         -rt founders",2024-10-04,high,"Silicon Canals article (Oct 2024)
         - fetched; location Prague per article. Equity not stated. Own w
         -ebsite not identified (impacthub.cz page returned 403). Pale Fi
         -re 'Purpose Ventures' link not verified."                      
      14 -qi-investicni-spolecnost,https://www.conseq.cz,unknown,unknown,
         -unknown,https://www.conseq.cz,page,,,low,"Fetched conseq.cz is 
         -about Conseq Investment Management, a.s. (Praha 1), not QI. QI 
         -not found on the page, so website not confirmed, type and team 
         -location unknown. CVCA profile not opened."                    
      15 -qq-capital,,CZ,family_office,yes,https://shizune.co/investors/p
         -rofile/qq-capital,page,"QQ Capital is a family venture office i
         -n Prague, Czech republic, that backs bold entrepreneurs",,low,"
         -Only an aggregator profile (Shizune) fetched, which is a lead a
         -nd not evidence; own site needed. Profile labels it VC Fund but
         - calls it family venture office, so family_office vs vc is a ju
         -dgment call. Michal Stencl link not found in sources."         
      16 -reflex-capital,https://www.reflexcapital.com,CZ,vc,yes,https://
         -www.reflexcapital.com,page,"Reflex Capital SE, Rašínovo Nábřeží
         - 2000/78, 120 00 Praha 2, Czech Republic",,medium,"Prague is th
         -e European seat; a San Francisco office is also listed. Page st
         -ates no fund type: vc inferred from startup portfolio and EUR 1
         -50M invested. Copyright 2026 only."                            
      17 -riverside-acceleration-capital,,unknown,lender,unknown,https://
         -www.pei-privatecredit.com/riverside-acceleration-capital-raisin
         -g-second-venture-debt-vehicle,page,"The strategy focuses on len
         -ding to growing tech companies with more than $3m in ARR.",2019
         --02-19,medium,"2019 article: venture debt only. Newer snippets 
         -say RAC also does growth equity (Fund III 2026), so type may ch
         -ange. Team location not on fetched page; parent Riverside is US
         - per snippets only. Input's ThreatMark equity deal conflicts." 
      18 -rockaway-capital,https://www.rockawaycapital.com,CZ,private_hol
         -ding,yes,https://www.rockawaycapital.com,page,"Rockaway Capital
         - je investiční skupina s více než desetiletou historií a působn
         -ostí napříč Evropou.",,medium,"Operator Rockaway GP a.s., Gener
         -ála Píky 430/26, Praha 6 (address shown; team location not stat
         -ed). Calls itself an investment group, not a family office. Lis
         -ts PE, VC and blockchain funds; new CZK 2.5bn fund per Lupa Jun
         - 2026 (lead, not fetched)."                                    
      19 -rockaway-ventures,,CZ,vc,yes,https://cc.cz/jakub-havrlant-prich
         -azi-s-novym-investicnim-fondem-rockaway-s-nim-chce-do-startupu-
         -poslat-25-miliardy-korun/,page,"Rockaway Ventures Fund",2021-09
         --23,low,"Article (Sep 2021) fetched: fund target EUR 100m, seat
         - Luxembourg, team location not stated; Rockaway group in Prague
         - per rockawaycapital.com. Equity implied by co-investing in rou
         -nds, not stated. Fund name later changed in sources: check curr
         -ent vehicle."                                                  
      20 -rockawayx,https://www.rockawayx.com,unknown,vc,unknown,https://
         -www.rockawayx.com,page,"We run blockchains and provide liquidit
         -y to fuel protocols.",,low,"Homepage fetched: offices in London
         -, Prague and Dubai, no HQ named; legal entity Blockad s.r.o. De
         -scribes early-stage investing plus yield and liquidity business
         -es, so mixed. Equity not stated. Prague link alone does not fix
         - team HQ."                                                     
      21 -rsj-investments,https://www.rsj.com,unknown,pe,yes,https://www.
         -rsj.com,page,"RSJ Investments obhospodařuje portfolia investic 
         -v oblasti nemovitostí a private equity.",,low,"Homepage fetched
         -: manages investment portfolios in real estate and private equi
         -ty; no city or country on page, Czech-language site only. Lupa 
         -names Václav Dejčmar as Spinoffy backer (lead, not checked). No
         -t clearly a family office or VC."                              
      22 -rtp-global,,unknown,vc,unknown,https://www.vcbacked.co/director
         -y/investors/rtp-global?page=2,snippet,,,low,"Snippets only, no 
         -page fetched. Described as VC investing Seed to Series B; sourc
         -es disagree on HQ (New York, or offices in London, New York, Pa
         -ris, Bangalore, Dubai). PangeAI round seen only via CB Insights
         - snippet."                                                     
      23 -safar-and-partners,,unknown,unknown,unknown,,snippet,,,low,"No 
         -search result for Safar & Partners at all. Seedtable ranking na
         -me is the only lead; CZ guess not supported by any source."    
      24 -sandberg-capital,https://sandbergcapital.com,SK,pe,yes,https://
         -sandbergcapital.com,page,"vykonáva správu alternatívnych invest
         -ičných fondov, ktoré sú zamerané na investovanie do private equ
         -ity",,medium,"Offices in Bratislava (Dvořákovo nábrežie 8) and 
         -Prague (Italská 2581/67); Slovak seat listed first, so SK mediu
         -m. Quote is from the regulatory disclaimer. PE manager of AIFs;
         - J&T Arch II stake sale per input not checked."                
      25 -seed-starter,https://www.seedstarter.cz,CZ,cvc,yes,https://www.
         -seedstarter.cz,page,"Corporate Venture Capital of Česká spořite
         -lna",,high,"Operator ČS Seed Starter, a.s., Olbrachtova 1929/62
         -, Praha 4. Minority shareholder or CLA/equity, tickets EUR 200k
         --1M. Page says it is not an accelerator. Bank-owned: borderline
         - per PLAN, decide downstream."                                 
      26 -seed-starter-ceske-sporitelny,https://www.seedstarter.cz,CZ,cvc
         -,yes,https://www.seedstarter.cz,page,"Corporate Venture Capital
         - of Česká spořitelna",,high,"Same operator as seed-starter (ČS 
         -Seed Starter a.s., Praha 4): likely duplicate, dedupe downstrea
         -m. Website here is the programme's own site, not given in input
         -. Slovak programme and LP stakes not checked."                 
  ⎿  Created data/candidates/triage/rerun_first/batch_05.csv (+26 -0)
       1 +candidate_id,website,hq_country,investor_type,equity_investor,e
         +vidence_url,evidence_kind,evidence_quote,evidence_date,confiden
         +ce,note                                                        
       2 +integral-capital-group,https://integralcapgroup.com,unknown,pe,
         +yes,https://integralcapgroup.com,page,"the leading mid-market p
         +rivate equity platform in Central and Eastern Europe",2026-08-2
         +0,medium,"Team hubs London, Budapest, Belgrade; GP office Luxem
         +bourg; no single team HQ on page. Integral Venture Partners (VC
         + arm) not checked."                                            
       3 +inven-capital,https://www.invencapital.cz,CZ,vc,yes,https://www
         +.invencapital.cz,page,"As a venture capital fund we invest EUR 
         +500m from institutional investors and global corporates",,mediu
         +m,"Office Pod Krizkem 1773/2, Praha 4. CEZ name only in footer;
         + no explicit corporate VC wording on page, so vc not cvc."     
       4 +invera,,HR,pe,yes,https://www.tportal.hr/biznis/clanak/invera-e
         +quity-partners-prikupio-160-milijuna-eura-za-fond-ii-20260427,p
         +age,"upravitelj alternativnih investicijskih fondova iz Zagreba
         +",2026-04-27,high,"Candidate is Invera PE fund; manager Invera 
         +Equity Partners, Zagreb. Page: private equity manager for SE Eu
         +rope, controlling stakes. Quote is Croatian from WebFetch outpu
         +t. inveraep.com not reachable."                                
       5 +investown,https://www.investown.cz,CZ,platform,no,https://www.i
         +nvestown.cz,page,"Investown je online platforma s investičními 
         +úvěry do nemovitostí.",,medium,"Real-estate loan platform (lend
         +ing/crowd). CZ inferred from CZK, ČNB licence line and Investow
         +n Technologies s.r.o.; no address seen. Future blog dates ignor
         +ed."                                                           
       6 +ip-lab-ventures,,unknown,vc,yes,https://www.businessinfo.cz/cla
         +nky/prvni-cesky-fond-na-transfer-technologii-zamereny-na-aplika
         +ce-ai-a-dalsi-pokrocile-technologie-investuje-do-komercionaliza
         +ce-vyzkumu-temer-miliardu/,snippet,,,low,"businessinfo.cz retur
         +ned 403; type from search summary (pre-seed to Series A, Czech 
         +technology-transfer fund). e15 page fetched but gives no team l
         +ocation or stage. Likely Czech, unconfirmed."                  
       7 +ipm,,CZ,unknown,yes,https://globalprivatecapital.org/?p=34494,s
         +nippet,,,low,"Snippet: IPM Group, a Prague-based asset manager,
         + led Photoneo USD 21m Series B (Dec 2021). Investor type not st
         +ated; short name ambiguous."                                   
       8 +irregular-expressions,,US,vc,yes,https://f4.fund/firms/irregula
         +r-expressions,snippet,,,low,"f4.fund returned 403; snippet: New
         + York-based pre-seed/seed fund. Example: TopK seed Jul 2025 wit
         +h Earlybird and KAYA."                                         
       9 +itaca-business-incubator,,unknown,unknown,unknown,,snippet,,,lo
         +w,"No search result for an ITACA incubator; Vestbee link not co
         +nfirmed. Triage type other is not a valid value, so unknown."  
      10 +ivbf,,unknown,unknown,no,https://www.e15.cz/kryptomeny/do-sveta
         +-kryptomen-vstupuje-dalsi-cesky-miliardar-ondrej-tomek-rozjizdi
         +-novy-fond-1411749,page,"smartkontraktové blockchainy",2023-11-
         +22,low,"Crypto-asset fund (smart-contract blockchains, staked e
         +ther), not a startup investor, so not vc. Team location not sta
         +ted. Article dated 2023-11-22."                                
      11 +j-t-arch,https://www.jtis.cz/fond/A2PCA,unknown,pe,yes,https://
         +www.jtis.cz/fond/A2PCA,page,"především z oblasti private equity
         +",2026-04-28,medium,"Qualified-investor fund of J&T INVESTIČNÍ 
         +SPOLEČNOST, a.s. Manager location not on page. Date is fund act
         +ivity date 28. 4. 2026."                                       
      12 +j-t-ventures,https://www.jtventures.cz,CZ,vc,yes,https://www.jt
         +ventures.cz,page,"Pre-seed až Series A",,high,"Office in Prague
         + (Karlin) in J&T Banka building. Focus CEE and SEE. Only copyri
         +ght 2024 on page."                                             
      13 +jafam-holding,,DE,unknown,unknown,https://lei.bloomberg.com/lei
         +s/view/875500IXO6D2T7TPKN04,snippet,,,low,"Bloomberg LEI record
         + (snippet): active German GmbH, registered address Herrsching, 
         +Bavaria. No business description found."                       
      14 +jaro-capital,,unknown,angel,yes,https://cc.cz/bicykly-jedou-jar
         +oslav-beck-a-robert-kyncl-posilaji-pres-10-milionu-do-ceskeho-p
         +rojektu-outfindo/,page,"JARO Capital, za nímž stojí Jaroslav Be
         +ck a Robert Kyncl",2021-07-14,low,"Vehicle of two individuals d
         +oing pre-seed deals; borderline angel vs private_holding. Team 
         +country not stated in article."                                
      15 +jet-investment,https://www.jetinvestment.cz,CZ,pe,yes,https://w
         +ww.jetinvestment.cz/en,page,"Pisárecká 271/13, 634 00 Brno-stře
         +d, Pisárky",,medium,"Quote is office address (Brno). Page lists
         + Private Equity, Real Estate and Venture Capital; calls itself 
         +a leading Central European investment company. pe per triage; r
         +eviewer should check venture arm. Redirect from jetinvestment.e
         +u."                                                            
      16 +jic-ventures,https://www.jic.cz/ventures/,CZ,vc,yes,https://www
         +.jic.cz/ventures/,page,"a Brno-born VC fund",,high,"Pre-seed an
         +d seed, tickets up to EUR 1M; managing partners Radim Kocourek 
         +and Miloš Sochor; office Purkynova 127, Brno."                 
      17 +jinej-fond,,unknown,unknown,unknown,,snippet,,,low,"Snippets on
         +ly: Jinej fond among HTG Medical pre-seed investors (Jul 2026 r
         +ound). No HQ, website or type found."                          
      18 +jsk-investments,https://www.jskinvestments.cz,CZ,private_holdin
         +g,yes,https://www.jskinvestments.cz,page,"projekty private equi
         +ty, growth equity a venture kapitálu",,medium,"Prague 1 (Klimen
         +tská 1216/46). Investment fund of the Kijonková couple; page do
         +es not call itself a family office, so private_holding by rule.
         + Reviewer may prefer family_office."                           
      19 +kaya-vc,https://www.kaya.vc,unknown,vc,yes,https://www.kaya.vc,
         +page,"We invest in ambitious & gritty founders from CEE",,mediu
         +m,"Page lists offices Warszawa, Prague, San Francisco, London; 
         +no HQ named, so team country unknown. Pre+Seed focus, USD 1-3M 
         +tickets. Prague 8 from triage not on page."                    
      20 +keiretsu-forum-prague,,CZ,angel,yes,https://www.czechinvest.gov
         +.cz/en/Homepage/News/April-2017/On-global-trends-in-angel-inves
         +ting-with-Randy-Williams,page,"a global investment community of
         + accredited angel investors, venture capitalists and corporate 
         +investors",2017-04-07,medium,"Prague branch active since autumn
         + 2015 per 2017 article. Old source; no current branch page foun
         +d."                                                            
      21 +kendaxa-group,,unknown,unknown,unknown,,snippet,,,low,"Search f
         +ound nothing on Kendaxa Group. Seedtable ranking is the only le
         +ad."                                                           
      22 +kinnevik,https://www.kinnevik.com,SE,vc,yes,https://www.kinnevi
         +k.com,page,"patient capital to challenger technology-enabled bu
         +sinesses in Europe and the US",,medium,"Stockholm office listed
         + first, London second; HQ not stated explicitly. Page does not 
         +use the label VC; vc per triage (Mews)."                       
      23 +kkcg,https://kkcg.com,CZ,private_holding,yes,https://kkcg.com,p
         +age,"an investment and innovation group operating a diverse ran
         +ge of companies",2026-10-09,high,"HQ building Evropská 866/71, 
         +Prague 6. Founder Karel Komárek. Invests own resources; page do
         +es not say family office. Date is page last modified."         
      24 +koopeo-ventures,https://www.koopeoventures.com,CZ,vc,yes,https:
         +//www.koopeoventures.com,page,"Investujeme do inovativních fire
         +m",,high,"HQ Solniční 243/17, Brno; offices Prague and Bratisla
         +va. Input said Prague, page says Brno. Early-stage venture; imp
         +act claim not on page. Copyright 2024 only."                   
      25 +kpn-ventures,https://www.kpnventures.com,NL,cvc,yes,https://www
         +.kpnventures.com,page,"Focus on early growth stage investments 
         +with relevance for KPN",,medium,"Offices Rotterdam and Amsterda
         +m, both NL; team location not stated. Page does not say corpora
         +te venture capital; cvc is an inference from the KPN link."    
      26 +lead-ventures,,HU,vc,yes,https://ceelm.com/czech-republic/25532
         +-havel-partners-advises-lead-ventures-on-cloudtalk-investment,s
         +nippet,,,low,"Search summary: Budapest-based VC and PE firm tha
         +t co-led CloudTalk Series B (Jan 2024). ceelm page failed to fe
         +tch (certificate). Verify Budapest."                           
  ⎿  Created data/candidates/triage/rerun_first/batch_07.csv (+26 -0)
       1 +candidate_id,website,hq_country,investor_type,equity_investor,e
         +vidence_url,evidence_kind,evidence_quote,evidence_date,confiden
         +ce,note                                                        
       2 +orbit-capital,https://orbitcapital.com,CZ,vc,yes,https://vestbe
         +e.com/insights/articles/interview-with-orbit-capital,page,"Base
         +d in Prague and Warsaw, the fund offers both growth equity and 
         +debt financing",2024-08-20,medium,"Vestbee interview (Aug 2024)
         + fetched; own site shows only nav labels Growth Equity and Grow
         +th Debt, no location. Mixed equity plus venture debt: vc chosen
         + for scale-up equity, debt side may need lender treatment downs
         +tream. Warsaw office also named."                              
       3 +orizon-systems,,JP,not_an_investor,unknown,https://elioplus.com
         +/profiles/channel-partners/21585/orizon-systems,snippet,,,low,"
         +Search snippets only: Tokyo-based IT services firm, Kemp partne
         +r. Logmanager stake not found in any result. Website not identi
         +fied."                                                         
       4 +pale-fire-capital,https://palefirecapital.com,CZ,pe,yes,https:/
         +/palefirecapital.com,page,"Investujeme vlastní dlouhodobý kapit
         +ál, podnikatelskou zkušenost a technologické know-how.",,high,"
         +Footer address Žatecká 55/14, Praha 1. Invests own capital in e
         +stablished companies (stakes, hundreds of millions CZK). Not a 
         +seed VC."                                                      
       5 +partech,https://partechpartners.com,unknown,unknown,unknown,htt
         +ps://partechpartners.com,page,"Partech harnesses broad expertis
         +e from a collective of experts to deliver the best support for 
         +founders across the globe.",,low,"Homepage fetched: no fund typ
         +e, team location or office list. Paris datelines appear only on
         + news items and are not treated as team location. Own about pag
         +e returned 404."                                               
       6 +patero,,unknown,unknown,unknown,https://www.cbinsights.com/comp
         +any/patero/financials,snippet,,,low,"Only CB Insights snippet (
         +one investor, 5G Open Innovation Lab, incubator round Sep 2025)
         +. No website, entity nature unknown. Aggregator snippet is a le
         +ad only."                                                      
       7 +pilulka-lab,,CZ,unknown,unknown,https://www.cbinsights.com/inve
         +stor/pilulka-lab,snippet,,,low,"CB Insights snippet calls it a 
         +Prague-based venture firm (e-health); Carebot seed deal 2024 pe
         +r snippet. Own page www.pilulka.cz/lab returned 404. Type unres
         +olved (triage said cvc, page not seen)."                       
       8 +plug-and-play,,US,vc,yes,https://en.wikipedia.org/wiki/Plug_and
         +_Play_Tech_Center,page,"Plug and Play Tech Center (PNP) is an A
         +merican venture capital firm headquartered in Sunnyvale, Califo
         +rnia.",,medium,"Wikipedia fetched; brand homepage gave title on
         +ly. Also works as an accelerator (CB Insights ranking). Equity 
         +not stated, inferred from VC type. Other directory lists Umea, 
         +Sweden, judged an error."                                      
       9 +point-nine,https://www.pointnine.com,unknown,vc,yes,https://www
         +.pointnine.com,page,"a thesis-driven early-stage venture capita
         +l firm",,high,"Homepage says team is 'based in Europe', no city
         +. Berlin appears only in search snippets. DE guess from triage 
         +not evidenced on page."                                        
      10 +presto-ventures,https://www.techhorizons.eu,unknown,vc,yes,http
         +s://www.techhorizons.eu,page,"a venture capital fund backing de
         +fense, security, and resilience technology",,medium,"Tech Horiz
         +ons page fetched: only the fund vehicle's registered office (Te
         +ch Horizons GP S.a r.l., Capellen, Luxembourg) is shown, not th
         +e team. Presto Ventures team location not on fetched page; pres
         +toventures.com not fetched. POSSIBLE CZ VC: triage and Lupa sug
         +gest Prague, needs team page."                                 
      11 +proxy-finance,,CZ,unknown,unknown,https://seedtable.com/ranking
         +s/investors/country/Czech%20Republic,snippet,,,low,"Seedtable r
         +anking snippet lists Proxy-Finance A.S. with type PE and Prague
         + location. Aggregator lead only; no own site, deal history or d
         +escription found."                                             
      12 +purple-ventures,https://www.purple-ventures.com,CZ,vc,yes,https
         +://www.purple-ventures.com,page,"We are a venture capital fund 
         +investing into CEE+ tech-enabled innovations in pre-seed and se
         +ed stages.",,high,"Footer registered address Masarykova 26, 602
         + 00 Brno. Minority equity stakes, initial tickets EUR 250k-400k
         +. Page footer copyright 2025 only."                            
      13 +purposetech,,CZ,vc,unknown,https://siliconcanals.com/purposetec
         +h-closes-fund-to-support-cee-founders/,page,"PurposeTech is a p
         +re-seed venture capital fund that was launched in 2023 to suppo
         +rt founders",2024-10-04,high,"Silicon Canals article (Oct 2024)
         + fetched; location Prague per article. Equity not stated. Own w
         +ebsite not identified (impacthub.cz page returned 403). Pale Fi
         +re 'Purpose Ventures' link not verified."                      
      14 +qi-investicni-spolecnost,https://www.conseq.cz,unknown,unknown,
         +unknown,https://www.conseq.cz,page,,,low,"Fetched conseq.cz is 
         +about Conseq Investment Management, a.s. (Praha 1), not QI. QI 
         +not found on the page, so website not confirmed, type and team 
         +location unknown. CVCA profile not opened."                    
      15 +qq-capital,,CZ,family_office,yes,https://shizune.co/investors/p
         +rofile/qq-capital,page,"QQ Capital is a family venture office i
         +n Prague, Czech republic, that backs bold entrepreneurs",,low,"
         +Only an aggregator profile (Shizune) fetched, which is a lead a
         +nd not evidence; own site needed. Profile labels it VC Fund but
         + calls it family venture office, so family_office vs vc is a ju
         +dgment call. Michal Stencl link not found in sources."         
      16 +reflex-capital,https://www.reflexcapital.com,CZ,vc,yes,https://
         +www.reflexcapital.com,page,"Reflex Capital SE, Rašínovo Nábřeží
         + 2000/78, 120 00 Praha 2, Czech Republic",,medium,"Prague is th
         +e European seat; a San Francisco office is also listed. Page st
         +ates no fund type: vc inferred from startup portfolio and EUR 1
         +50M invested. Copyright 2026 only."                            
      17 +riverside-acceleration-capital,,unknown,lender,unknown,https://
         +www.pei-privatecredit.com/riverside-acceleration-capital-raisin
         +g-second-venture-debt-vehicle,page,"The strategy focuses on len
         +ding to growing tech companies with more than $3m in ARR.",2019
         +-02-19,medium,"2019 article: venture debt only. Newer snippets 
         +say RAC also does growth equity (Fund III 2026), so type may ch
         +ange. Team location not on fetched page; parent Riverside is US
         + per snippets only. Input's ThreatMark equity deal conflicts." 
      18 +rockaway-capital,https://www.rockawaycapital.com,CZ,private_hol
         +ding,yes,https://www.rockawaycapital.com,page,"Rockaway Capital
         + je investiční skupina s více než desetiletou historií a působn
         +ostí napříč Evropou.",,medium,"Operator Rockaway GP a.s., Gener
         +ála Píky 430/26, Praha 6 (address shown; team location not stat
         +ed). Calls itself an investment group, not a family office. Lis
         +ts PE, VC and blockchain funds; new CZK 2.5bn fund per Lupa Jun
         + 2026 (lead, not fetched)."                                    
      19 +rockaway-ventures,,CZ,vc,yes,https://cc.cz/jakub-havrlant-prich
         +azi-s-novym-investicnim-fondem-rockaway-s-nim-chce-do-startupu-
         +poslat-25-miliardy-korun/,page,"Rockaway Ventures Fund",2021-09
         +-23,low,"Article (Sep 2021) fetched: fund target EUR 100m, seat
         + Luxembourg, team location not stated; Rockaway group in Prague
         + per rockawaycapital.com. Equity implied by co-investing in rou
         +nds, not stated. Fund name later changed in sources: check curr
         +ent vehicle."                                                  
      20 +rockawayx,https://www.rockawayx.com,unknown,vc,unknown,https://
         +www.rockawayx.com,page,"We run blockchains and provide liquidit
         +y to fuel protocols.",,low,"Homepage fetched: offices in London
         +, Prague and Dubai, no HQ named; legal entity Blockad s.r.o. De
         +scribes early-stage investing plus yield and liquidity business
         +es, so mixed. Equity not stated. Prague link alone does not fix
         + team HQ."                                                     
      21 +rsj-investments,https://www.rsj.com,unknown,pe,yes,https://www.
         +rsj.com,page,"RSJ Investments obhospodařuje portfolia investic 
         +v oblasti nemovitostí a private equity.",,low,"Homepage fetched
         +: manages investment portfolios in real estate and private equi
         +ty; no city or country on page, Czech-language site only. Lupa 
         +names Václav Dejčmar as Spinoffy backer (lead, not checked). No
         +t clearly a family office or VC."                              
      22 +rtp-global,,unknown,vc,unknown,https://www.vcbacked.co/director
         +y/investors/rtp-global?page=2,snippet,,,low,"Snippets only, no 
         +page fetched. Described as VC investing Seed to Series B; sourc
         +es disagree on HQ (New York, or offices in London, New York, Pa
         +ris, Bangalore, Dubai). PangeAI round seen only via CB Insights
         + snippet."                                                     
      23 +safar-and-partners,,unknown,unknown,unknown,,snippet,,,low,"No 
         +search result for Safar & Partners at all. Seedtable ranking na
         +me is the only lead; CZ guess not supported by any source."    
      24 +sandberg-capital,https://sandbergcapital.com,SK,pe,yes,https://
         +sandbergcapital.com,page,"vykonáva správu alternatívnych invest
         +ičných fondov, ktoré sú zamerané na investovanie do private equ
         +ity",,medium,"Offices in Bratislava (Dvořákovo nábrežie 8) and 
         +Prague (Italská 2581/67); Slovak seat listed first, so SK mediu
         +m. Quote is from the regulatory disclaimer. PE manager of AIFs;
         + J&T Arch II stake sale per input not checked."                
      25 +seed-starter,https://www.seedstarter.cz,CZ,cvc,yes,https://www.
         +seedstarter.cz,page,"Corporate Venture Capital of Česká spořite
         +lna",,high,"Operator ČS Seed Starter, a.s., Olbrachtova 1929/62
         +, Praha 4. Minority shareholder or CLA/equity, tickets EUR 200k
         +-1M. Page says it is not an accelerator. Bank-owned: borderline
         + per PLAN, decide downstream."                                 
      26 +seed-starter-ceske-sporitelny,https://www.seedstarter.cz,CZ,cvc
         +,yes,https://www.seedstarter.cz,page,"Corporate Venture Capital
         + of Česká spořitelna",,high,"Same operator as seed-starter (ČS 
         +Seed Starter a.s., Praha 4): likely duplicate, dedupe downstrea
         +m. Website here is the programme's own site, not given in input
         +. Slovak programme and LP stakes not checked."                 
  ⎿  Updated data/runs/run_log.csv (+21 -20)
       1 -date,agent,model,id,tokens,tool_uses,duration_s,outcome        
       2 -2026-10-11,candidate-scout,sonnet,scout_cvca,175501,107,1489.6,
         -ok                                                             
       3 -2026-10-11,candidate-scout,sonnet,scout_deals,76062,219,3709.2,
         -ok                                                             
       4 -2026-10-11,candidate-scout,sonnet,scout_programmes,284471,172,1
         -857.5,ok                                                       
       5 -2026-10-11,candidate-triage,haiku,attempt1/batch_01,137285,51,7
         -80.2,failed                                                    
       6 -2026-10-11,candidate-triage,haiku,attempt1/batch_02,195463,66,9
         -89.7,failed                                                    
       7 -2026-10-11,candidate-triage,haiku,attempt1/batch_03,123532,40,4
         -43.2,failed                                                    
       8 -2026-10-11,candidate-triage,haiku,attempt1/batch_04,107022,19,7
         -06.6,failed                                                    
       9 -2026-10-11,candidate-triage,haiku,attempt1/batch_05,108607,21,7
         -11.1,failed                                                    
      10 -2026-10-11,candidate-triage,haiku,attempt1/batch_06,121427,37,4
         -41.3,failed                                                    
      11 -2026-10-11,candidate-triage,haiku,attempt1/batch_07,108698,20,7
         -11.6,failed                                                    
      12 -2026-10-11,candidate-triage,haiku,attempt1/batch_08,114325,30,7
         -18.5,failed                                                    
      13 -2026-10-11,candidate-triage,haiku,attempt1/batch_09,110833,22,7
         -12.3,failed                                                    
      14 -2026-10-12,candidate-triage,haiku,batch_02,60054,37,114.3,ok   
      15 -2026-10-12,candidate-triage,haiku,batch_03,67124,44,161.4,ok   
      16 -2026-10-12,candidate-triage,haiku,batch_01,66963,46,173.8,rerun
      17 -2026-10-12,candidate-triage,haiku,batch_04,73436,49,207.3,rerun
      18 -2026-10-12,candidate-triage,haiku,batch_05,69225,41,157.7,ok   
      19 -2026-10-12,candidate-triage,haiku,batch_01_rerun,75977,57,170.0
         -,ok                                                            
      20 -2026-10-12,candidate-triage,haiku,batch_06,61319,40,134.9,ok   
       1 +date,agent,model,id,tokens,tool_uses,duration_s,outcome        
       2 +2026-10-11,candidate-scout,sonnet,scout_cvca,175501,107,1489.6,
         +ok                                                             
       3 +2026-10-11,candidate-scout,sonnet,scout_deals,76062,219,3709.2,
         +ok                                                             
       4 +2026-10-11,candidate-scout,sonnet,scout_programmes,284471,172,1
         +857.5,ok                                                       
       5 +2026-10-11,candidate-triage,haiku,attempt1/batch_01,137285,51,7
         +80.2,failed                                                    
       6 +2026-10-11,candidate-triage,haiku,attempt1/batch_02,195463,66,9
         +89.7,failed                                                    
       7 +2026-10-11,candidate-triage,haiku,attempt1/batch_03,123532,40,4
         +43.2,failed                                                    
       8 +2026-10-11,candidate-triage,haiku,attempt1/batch_04,107022,19,7
         +06.6,failed                                                    
       9 +2026-10-11,candidate-triage,haiku,attempt1/batch_05,108607,21,7
         +11.1,failed                                                    
      10 +2026-10-11,candidate-triage,haiku,attempt1/batch_06,121427,37,4
         +41.3,failed                                                    
      11 +2026-10-11,candidate-triage,haiku,attempt1/batch_07,108698,20,7
         +11.6,failed                                                    
      12 +2026-10-11,candidate-triage,haiku,attempt1/batch_08,114325,30,7
         +18.5,failed                                                    
      13 +2026-10-11,candidate-triage,haiku,attempt1/batch_09,110833,22,7
         +12.3,failed                                                    
      14 +2026-10-12,candidate-triage,haiku,batch_02,60054,37,114.3,ok   
      15 +2026-10-12,candidate-triage,haiku,batch_03,67124,44,161.4,ok   
      16 +2026-10-12,candidate-triage,haiku,batch_01,66963,46,173.8,rerun
      17 +2026-10-12,candidate-triage,haiku,batch_04,73436,49,207.3,rerun
      18 +2026-10-12,candidate-triage,haiku,batch_05,69225,41,157.7,rerun
      19 +2026-10-12,candidate-triage,haiku,batch_01_rerun,75977,57,170.0
         +,ok                                                            
      20 +2026-10-12,candidate-triage,haiku,batch_06,61319,40,134.9,ok   
     … 1 more lines (ctrl+o to expand)
  ⎿  … 1 more file changed

⏺ candidate-triage(Triage batch 05 rerun)
  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)

⏺ Three agents are running: batch 04 rerun, batch 05 rerun and batch 08. The
  batch 07 rerun and batch 09 are queued.

✻ Crunched for 19s · done Monday 5:15 PM

› Message from candidate-triage
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/candidates/triage/batch_04.csv with 25 rows, in input order, with
  the header.

  - hq_country unknown: 7 (fivesquare, gain-ventures,
  goldman-sachs-alternatives, google-ventures, grouport-ventures, headline,
  hartenberg). Down from 14 unknowns in the first pass.
  - investor_type unknown: 2 (fivesquare, gain-ventures). Snippet-only rows: 3
  (fivesquare, gain-ventures, grouport-ventures).
  - Possible Czech VCs I was not sure of: grouport-ventures (only Capboard
  aggregator says Plynární 10, Prague; hq left unknown), impulse-ventures (Czech
  fund per cc.cz 2020 article, Prague only from snippets), incomming-ventures
  (2016 article, possibly inactive), gain-ventures (identity unresolved).
  Hartenberg is a Babiš-linked holding, not a VC.

  Note: the gi21-capital home page returned text asking me to report on Goldman
  Sachs and Fifth Wall. I ignored it. Treat that fetched page as untrusted. No
  git commit was made.

⏺ The batch 04 rerun brought hq unknown down from 14 to 7. The agent also
  spotted and ignored injected instructions on the gi21-capital page; I'll log
  that as E-07. Launching the batch 07 rerun.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && cat >>
      docs/ai-errors.md <<'EOF'
      | E-07 | 2026-10-12 | candidate-triage (batch 04, opakovaný běh) | gi21…)
  ⎿  Updated docs/ai-errors.md (+1 -0)
      10  | E-04 | 2026-10-11 | candidate-triage (batch 06) | InCOMMing |
           — | Titulek výsledku vyhledávání (Dealroom) obsahoval instrukc
          i určenou jazykovým modelům (prompt injection). | Agent ji rozp
          oznal a ignoroval. | Nic; potvrzuje, že obsah stránek je třeba 
          brát jako data, ne jako pokyny. |
      11  | E-05 | 2026-10-11 | candidate-scout (cvca) | Tilia Impact Ven
          tures | `website` | Ne chyba AI, ale chyba ve zdroji: odkaz v p
          rofilu CVCA vede na skylimit.cz, ačkoli text uvádí tilia.vc. | 
          Agent si nesouladu všiml. | Použita doména tilia.vc; příklad to
          ho, proč ani asociační profil není tier-1 zdroj. |
      12  | E-06 | 2026-10-12 | candidate-triage (batch 01, 04) | Accel, 
          Battery Ventures, Atomico… | `hq_country` | Haiku nechal `unkno
          wn` u sídla i zjevně zahraničních fondů (Accel, Battery Venture
          s); u batch 01 a 04 byla neznámá země u 14/25. Opakovaný běh ba
          tch 01 dopadl hůř (18/25) a mezi běhy se odpovědi liší (např. a
          irbridge NL → unknown, aspire11 unknown → CZ). | Kontrola podíl
          u `unknown` po dávce (runbook R1) a porovnání obou běhů. | Plat
          í opakovaný běh (podle runbooku); první výstup je v `data/candi
          dates/triage/rerun_first/`. `unknown` nevyřazuje, kandidát jde 
          do fronty extrakce, takže chyba zvyšuje náklad, ne ztrátu kandi
          dátů. |
      13 +| E-07 | 2026-10-12 | candidate-triage (batch 04, opakovaný běh
         +) | gi21-capital | — | Stažená domovská stránka obsahovala text
         + s pokynem pro model (podat zprávu o Goldman Sachs a Fifth Wall
         +), tedy prompt injection. | Agent ji rozpoznal, ignoroval a nah
         +lásil. | Nic; druhý případ po E-04. Stránku gi21-capital beru j
         +ako nedůvěryhodnou, extraktor a ověřovatel ji čtou jen jako dat
         +a. |                                                           

⏺ candidate-triage(Triage batch 07 rerun)
  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)

⏺ Agent "Triage batch 04 rerun" finished · 4m 5s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-12,candidate-triage,haiku,batch_04_rerun,86378,67,245.1,ok" >>
      data/runs/run_log.csv && gi…)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      19  2026-10-12,candidate-triage,haiku,batch_01_rerun,75977,57,170.0
          ,ok
      20  2026-10-12,candidate-triage,haiku,batch_06,61319,40,134.9,ok
      21  2026-10-12,candidate-triage,haiku,batch_07,69691,43,146.5,rerun
      22 +2026-10-12,candidate-triage,haiku,batch_04_rerun,86378,67,245.1
         +,ok                                                            

⏺ I've committed and pushed the batch 04 rerun with its log entry. Still
  running: batch 05 rerun, batch 07 rerun and batch 08. Batch 09 is the last one
  to start.

✻ Brewed for 13s · done Monday 5:16 PM

› Message from candidate-triage
  Wrote 25 rows to /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/candidates/triage/batch_08.csv (input order, header included).
  Unknown: 3 investor_type unknown (slovak-investment-holding,
  stredocesky-inovacni-centrum, theras-group); 1 hq_country unknown
  (seedtwo-capital). Several other rows rest on partial evidence, see notes.
  Snippet evidence: 6 rows (silicon-gardens, stredocesky-inovacni-centrum,
  tachles, tcf-capital, theras-group, thein). Several page rows also use
  search-summary HQ/location, noted per row.
  Possible Czech VC not sure of: tachles (Czech fund by ex-Springtide partners,
  register and fund only seen in snippets, no website); spinoffy (Czech fund,
  page fetched, type vc, website missing). Also springtide-ventures (KKCG fund)
  is a Czech candidate I typed private_holding, not vc; please check.
  Quotes for Polish/Slovak/Czech pages come from WebFetch output and may be
  paraphrased, so run check_quotes on them.

⏺ Batch 08 is fine (1 hq unknown). The agent itself flags springtide-ventures as
  possibly mistyped, so I'll check what triage would do with it.

  Ran 1 shell command (ctrl+o to expand)

⏺ candidate-triage(Triage batch 09)
  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)

⏺ Agent "Triage batch 08" finished · 3m 36s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-12,candidate-triage,haiku,batch_08,92924,64,215.8,ok" >>
      data/runs/run_log.csv)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      20  2026-10-12,candidate-triage,haiku,batch_06,61319,40,134.9,ok
      21  2026-10-12,candidate-triage,haiku,batch_07,69691,43,146.5,rerun
      22  2026-10-12,candidate-triage,haiku,batch_04_rerun,86378,67,245.1
          ,ok
      23 +2026-10-12,candidate-triage,haiku,batch_08,92924,64,215.8,ok   

⏺ Springtide Ventures is a KKCG venture fund based in Prague, but triage typed
  it private_holding, and decide.py would exclude it without extraction. Once
  all batches are in, I'll check how many Czech candidates would be excluded on
  this kind of weak type evidence before running R2.

  Still running: batch 05 rerun, batch 07 rerun and batch 09.

✻ Worked for 13s · done Monday 5:18 PM

› Message from candidate-triage
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/candidates/triage/batch_05.csv: 25 rows, input order, same header
  as rerun_first/batch_04.csv.

  - hq_country unknown: 10 (integral-capital-group, ip-lab-ventures, ipm,
  itaca-business-incubator, ivbf, jafam-holding, jaro-capital, jinej-fond,
  kaya-vc, kendaxa-group). Only 10 remain unknown after the re-run, down from 9
  in the first pass plus the rows I could now resolve.
  - investor_type unknown: 6 (ipm, itaca-business-incubator, ivbf,
  jafam-holding, jinej-fond, kendaxa-group). Snippet evidence_kind: 0.
  Aggregator pages (Nordic9, Shizune, Seedtable, Dealroom, CB Insights,
  AroundDeal) were used only as leads.
  - Corrections from the re-run: invera is HR (Globalscope page says "Country
  Croatia"; the scout's SI was wrong), irregular-expressions US (irregex.vc
  footer "New York - San Francisco"), lead-ventures HU (Vestbee article),
  kpn-ventures NL, kinnevik SE, koopeo-ventures CZ (registered in Brno).
  - Possible Czech VCs I am unsure of: ip-lab-ventures (team location not on any
  fetched page; e15 page dated 2026-03-23 conflicts with the Sept 2026 EIF date
  in snippets), kaya-vc (Prague office listed but no team location; KAYA
  Advisory s.r.o. only a lead), and jinej-fond (CB Insights says Prague, Shizune
  and AltSS say Brno).
  - Quotes come from WebFetch output, so they still need check_quotes.py before
  use. Two sites failed: itaca.cz (certificate), and ipmgroup.com and kendaxa.cz
  (did not resolve).

⏺ The batch 05 rerun is in: 10 hq unknown, but no snippet-only evidence, and it
  corrected a few countries. Per D-014 this rerun output stands. I'll log it
  when the usage figures arrive.

✻ Brewed for 2s · done Monday 5:19 PM

⏺ Agent "Triage batch 05 rerun" finished · 3m 19s

› Message from candidate-triage
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/candidates/triage/batch_07.csv: 25 rows, input order, header
  included.
  10 hq_country unknown (orizon-systems, partech, plug-and-play, point-nine,
  proxy-finance, qi-investicni-spolecnost, riverside-acceleration-capital,
  rsj-investments, rtp-global, safar-and-partners). Investor_type unknown for 6
  of them.
  0 rows with evidence_kind=snippet. All evidence comes from fetched pages.
  Patero, QQ Capital, Presto Ventures, PurposeTech, Reflex, Seed Starter and
  Rockaway were found this run.
  Possible Czech VCs I am not sure of: orbit-capital (team in Prague and Warsaw,
  recorded CZ low); qq-capital (family_office vs vc); rockaway-ventures and
  rockawayx (location inferred from operator seat, low); pale-fire-capital (pe
  rests on earlier notes, homepage does not say so).
  Budget note: the WebSearch budget ran out mid-run, so Safar, Proxy-Finance,
  Orizon, Plug and Play and RTP Global got no further searches. Sandberg Capital
  has offices in both Bratislava and Prague; I recorded SK medium.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-12,candidate-triage,haiku,batch_05_rerun,88189,61,199.4,ok" >>
      data/runs/run_log.csv)  ⎿  Updated data/runs/run_log.csv (+1 -0)
      21  2026-10-12,candidate-triage,haiku,batch_07,69691,43,146.5,rerun
      22  2026-10-12,candidate-triage,haiku,batch_04_rerun,86378,67,245.1
          ,ok
      23  2026-10-12,candidate-triage,haiku,batch_08,92924,64,215.8,ok
      24 +2026-10-12,candidate-triage,haiku,batch_05_rerun,88189,61,199.4
         +,ok                                                            

⏺ Agent "Triage batch 07 rerun" finished · 3m 11s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-12,candidate-triage,haiku,batch_07_rerun,73353,54,190.6,ok" >>
      data/runs/run_log.csv && gi…)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      22  2026-10-12,candidate-triage,haiku,batch_04_rerun,86378,67,245.1
          ,ok
      23  2026-10-12,candidate-triage,haiku,batch_08,92924,64,215.8,ok
      24  2026-10-12,candidate-triage,haiku,batch_05_rerun,88189,61,199.4
          ,ok
      25 +2026-10-12,candidate-triage,haiku,batch_07_rerun,73353,54,190.6
         +,ok                                                            

⏺ Batch 07 rerun is logged and committed. Only batch 09 is still running. Once
  it finishes, I'll check the type-exclusion risk for Czech candidates and then
  run R2.

✻ Worked for 9s · done Monday 5:19 PM

› Message from candidate-triage
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/candidates/triage/batch_09.csv: 25 rows, header, input order.

  - 19 of 25 have hq_country=unknown (no team location on fetched pages). 12
  have investor_type=unknown.
  - 0 rows use evidence_kind=snippet. Rows with no fetched page have empty
  evidence fields.
  - The WebSearch budget ran out after about 8 searches, so most of the unknown
  rows were not verified. Several quotes come from WebFetch output, not verbatim
  page text, so check_quotes must confirm them. The notes flag which ones.
  - Possible CZ VC not sure of: united-founders (Lupa says founded in Prague,
  E15 says team spread across 26 countries, left unknown). Also zaka-vc (Prague
  in footer list, no HQ stated).
  - Resolved: tilia-impact-ventures (CZ, vc, high), versute-investments (CZ, pe,
  high), venture-to-future-fund (SK, vc, high).

⏺ Batch 09 has 19/25 hq unknown, so it needs a rerun. But two agents reported
  the WebSearch budget running out, which also matters for R3, so I'll check
  whether search works now first.

⏺ Agent "Triage batch 09" finished · 1m 44s

⏺ Web Search("Springtide Ventures KKCG")
  ⎿  Did 1 search in 5s

⏺ Search works again, so the budget limit looks temporary. Launching the batch
  09 rerun.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-12,candidate-triage,haiku,batch_09,39415,28,104.4,rerun" >>
      data/runs/run_log.csv && mv da…)
  ⎿  Deleted data/candidates/triage/batch_09.csv (+0 -26)
       1 -candidate_id,website,hq_country,investor_type,equity_investor,e
         -vidence_url,evidence_kind,evidence_quote,evidence_date,confiden
         -ce,note                                                        
       2 -tibiq,,unknown,unknown,unknown,,,,,low,"No page fetched; only s
         -cout lead (Lupa). Identity, HQ and type not verified."         
       3 -tiger-global,https://www.tigerglobal.com,US,vc,yes,https://www.
         -tigerglobal.com,page,"9 West 57th St., New York, NY 10019",,med
         -ium,"Address from fetched page. Type vc is from scout lead and 
         -firm's growth/venture activity; page calls itself a research-dr
         -iven investment firm and SEC-registered adviser. Quote is WebFe
         -tch output, verify verbatim."                                  
       4 -tilia-impact-ventures,https://tilia.vc,CZ,vc,yes,https://tilia.
         -vc,page,"Drtinova 557/10, 150 00 Prague",,high,"Fetched page: T
         -ilia Impact Ventures backs Czech and CEE region founders. Team 
         -listed on page (partners, investment committee). Scout CVCA lin
         -k wrong, not used."                                            
       5 -token-ventures,,unknown,unknown,unknown,,,,,low,"No page fetche
         -d; named only in CzechCrunch newsletter lead. Identity and HQ n
         -ot verified."                                                  
       6 -tomenterprise,,unknown,unknown,unknown,,,,,low,"No page fetched
         -; identity not verified; may be an individual vehicle."        
       7 -triplebee,,unknown,unknown,unknown,,,,,low,"No page fetched; on
         -ly CzechCrunch newsletter lead (family vehicle, unverified)."  
       8 -uk-innovations-prague,,unknown,unknown,unknown,,,,,low,"No page
         - fetched; Charles University subsidiary, role as investor unver
         -ified."                                                        
       9 -unbound,,unknown,unknown,unknown,,,,,low,"No page fetched; Lond
         -on fund per Lupa lead only. Search budget exhausted before veri
         -fication."                                                     
      10 -underground-ventures,,unknown,unknown,unknown,,,,,low,"No page 
         -fetched; GA Drilling investor lead only. Identity and HQ not ve
         -rified."                                                       
      11 -united-founders,,unknown,vc,yes,https://www.lupa.cz/aktuality/h
         -avrlant-spoluzaklada-united-founders-novy-fond-chce-do-evropsky
         -ch-technologii-investovat-2-miliardy/,page,"V Praze vznikl nový
         - „panevropský“ venture fond",,low,"Lupa says fund founded in Pr
         -ague. E15 page says Luxembourg-law fund, managing partner in Pa
         -ris, team in 26 countries, no team HQ stated. HQ left unknown; 
         -possible CZ VC, check team location. Quote is WebFetch output, 
         -verify verbatim."                                              
      12 -university2ventures,https://u2v.vc,unknown,vc,yes,https://u2v.v
         -c,page,"capital, strategic support, industry connections, and o
         -perational guidance.",,medium,"Fetched page describes investing
         - in early-stage technology companies; no team location on page.
         - US HQ is prior knowledge, not from source, so left unknown."  
      13 -up21,,unknown,unknown,unknown,,,,,low,"up21.com redirects to a 
         -parked domain page; no content fetched. Accelerator lead from V
         -estbee only, equity terms not stated."                         
      14 -value4capital,https://www.value4capital.com,unknown,pe,yes,http
         -s://www.value4capital.com,page,"We build market leaders.",,medi
         -um,"Fetched page: private equity firm focused on Central Europe
         -, buyout and growth deals. Three offices listed (Luxembourg GP,
         - Warsaw, Bucharest) but team base not stated; Warsaw guess not 
         -used. Type sentence is WebFetch summary, verify."              
      15 -venture-to-future-fund,https://vff.sk,SK,vc,yes,https://vff.sk,
         -page,"Sme slovenský venture kapitálový fond so zameraním na pod
         -poru inovatívnych lokálnych podnikov.",,high,"Fetched page: off
         -ice and correspondence address Karadzicova 8/A, 821 08 Bratisla
         -va. Invests from late-seed to Series B."                       
      16 -versute-investments,https://versute.cz,CZ,pe,yes,https://versut
         -e.cz,page,"Investujeme do malých a středních podniků prostředni
         -ctvím Private Equity fondů.",,high,"Fetched page: office Vodick
         -ova 33, 110 00 Praha 1. Also presents advisory services; type p
         -e based on PE fund manager statement."                         
      17 -viking-global-investors,,unknown,unknown,yes,https://www.viking
         -global.com,page,"a global investment firm managing $56+ billion
         - of capital.",,low,"Fetched page: public equity, private equity
         - and credit business; offices in Stamford, Hong Kong, London, N
         -ew York, San Francisco, no HQ named. Crossover/hedge profile fi
         -ts no investor_type cleanly, so unknown."                      
      18 -vocal-vc,,unknown,unknown,unknown,,,,,low,"No page fetched; Pan
         -geAI seed lead only. HQ and website not identified."           
      19 -westly-group,,unknown,unknown,unknown,,,,,low,"No page fetched;
         - Woltair investor lead only. Search budget exhausted before ver
         -ification."                                                    
      20 -white-star-capital,https://www.whitestarcapital.com,unknown,vc,
         -yes,https://www.whitestarcapital.com,page,"A global multi-stage
         - technology investment platform.",,medium,"Fetched page: runs V
         -enture, Digital Asset and Seed funds. Team location not stated;
         - map lists Toronto, Montreal, New York, Lisbon, London, Paris t
         -ied to founders/companies, not team offices."                  
      21 -wing-venture-capital,https://www.wing.vc,US,vc,yes,https://www.
         -wing.vc,page,"Palo Alto CA",,medium,"Footer of fetched page lis
         -ts Palo Alto CA as the only location; team page not fetched. Pa
         -ge: early-stage venture for AI founders. Identity match to scou
         -t's Wing Venture Capital assumed from domain, not separately co
         -nfirmed."                                                      
      22 -y-combinator,https://www.ycombinator.com,unknown,accelerator,ye
         -s,https://www.ycombinator.com,page,"invests ""$500k"" in each s
         -elected company",,medium,"Accelerator per fetched page. Page sa
         -ys YC invests $500k per company and links SAFE; equity terms no
         -t spelled out. Founders move to San Francisco; team HQ not stat
         -ed, so unknown."                                               
      23 -y-soft-ventures,,unknown,cvc,unknown,https://www.ysoft.com,page
         -,"YSoft Labs and Y Soft Ventures provide new streams of innovat
         -ion into our teams and processes.",,low,"Fetched parent site ys
         -oft.com names Y Soft Ventures as innovation stream; page does n
         -ot say it invests in companies or where it is based. cvc from s
         -cout lead (corporate arm). Parent HQ not stated on page."      
      24 -zaka-vc,https://zaka.vc,unknown,vc,yes,https://zaka.vc,page,"a 
         -seed & pre-seed VC fund, investing mainly in the US and Europe.
         -",,medium,"Fetched page lists Silicon Valley / London / Prague 
         -/ Bratislava in footer without naming an HQ. Prague from scout 
         -lead, not used as HQ."                                         
      25 -zero-gravity-capital,,unknown,unknown,unknown,,,,,low,"No page 
         -fetched; named as investor in Patron Go and Powerful Medical le
         -ads only. Identity unverified."                                
      26 -zero-one-hundred,https://www.0100.vc,SK,vc,yes,https://www.0100
         -.vc,page,"General Partner Michal Csonga is based in Slovakia",,
         -medium,"Fetched page: VC backing startups from Emerging Europe 
         -and Middle East; offices in Czechia, Slovakia, Cyprus, UAE; reg
         -istered in Nicosia (RAIF). Managing Partner based between Slova
         -kia and Cyprus. HQ SK is judgement from individual bases. Quote
         - is WebFetch summary, verify."                                 
  ⎿  Created data/candidates/triage/rerun_first/batch_09.csv (+26 -0)
       1 +candidate_id,website,hq_country,investor_type,equity_investor,e
         +vidence_url,evidence_kind,evidence_quote,evidence_date,confiden
         +ce,note                                                        
       2 +tibiq,,unknown,unknown,unknown,,,,,low,"No page fetched; only s
         +cout lead (Lupa). Identity, HQ and type not verified."         
       3 +tiger-global,https://www.tigerglobal.com,US,vc,yes,https://www.
         +tigerglobal.com,page,"9 West 57th St., New York, NY 10019",,med
         +ium,"Address from fetched page. Type vc is from scout lead and 
         +firm's growth/venture activity; page calls itself a research-dr
         +iven investment firm and SEC-registered adviser. Quote is WebFe
         +tch output, verify verbatim."                                  
       4 +tilia-impact-ventures,https://tilia.vc,CZ,vc,yes,https://tilia.
         +vc,page,"Drtinova 557/10, 150 00 Prague",,high,"Fetched page: T
         +ilia Impact Ventures backs Czech and CEE region founders. Team 
         +listed on page (partners, investment committee). Scout CVCA lin
         +k wrong, not used."                                            
       5 +token-ventures,,unknown,unknown,unknown,,,,,low,"No page fetche
         +d; named only in CzechCrunch newsletter lead. Identity and HQ n
         +ot verified."                                                  
       6 +tomenterprise,,unknown,unknown,unknown,,,,,low,"No page fetched
         +; identity not verified; may be an individual vehicle."        
       7 +triplebee,,unknown,unknown,unknown,,,,,low,"No page fetched; on
         +ly CzechCrunch newsletter lead (family vehicle, unverified)."  
       8 +uk-innovations-prague,,unknown,unknown,unknown,,,,,low,"No page
         + fetched; Charles University subsidiary, role as investor unver
         +ified."                                                        
       9 +unbound,,unknown,unknown,unknown,,,,,low,"No page fetched; Lond
         +on fund per Lupa lead only. Search budget exhausted before veri
         +fication."                                                     
      10 +underground-ventures,,unknown,unknown,unknown,,,,,low,"No page 
         +fetched; GA Drilling investor lead only. Identity and HQ not ve
         +rified."                                                       
      11 +united-founders,,unknown,vc,yes,https://www.lupa.cz/aktuality/h
         +avrlant-spoluzaklada-united-founders-novy-fond-chce-do-evropsky
         +ch-technologii-investovat-2-miliardy/,page,"V Praze vznikl nový
         + „panevropský“ venture fond",,low,"Lupa says fund founded in Pr
         +ague. E15 page says Luxembourg-law fund, managing partner in Pa
         +ris, team in 26 countries, no team HQ stated. HQ left unknown; 
         +possible CZ VC, check team location. Quote is WebFetch output, 
         +verify verbatim."                                              
      12 +university2ventures,https://u2v.vc,unknown,vc,yes,https://u2v.v
         +c,page,"capital, strategic support, industry connections, and o
         +perational guidance.",,medium,"Fetched page describes investing
         + in early-stage technology companies; no team location on page.
         + US HQ is prior knowledge, not from source, so left unknown."  
      13 +up21,,unknown,unknown,unknown,,,,,low,"up21.com redirects to a 
         +parked domain page; no content fetched. Accelerator lead from V
         +estbee only, equity terms not stated."                         
      14 +value4capital,https://www.value4capital.com,unknown,pe,yes,http
         +s://www.value4capital.com,page,"We build market leaders.",,medi
         +um,"Fetched page: private equity firm focused on Central Europe
         +, buyout and growth deals. Three offices listed (Luxembourg GP,
         + Warsaw, Bucharest) but team base not stated; Warsaw guess not 
         +used. Type sentence is WebFetch summary, verify."              
      15 +venture-to-future-fund,https://vff.sk,SK,vc,yes,https://vff.sk,
         +page,"Sme slovenský venture kapitálový fond so zameraním na pod
         +poru inovatívnych lokálnych podnikov.",,high,"Fetched page: off
         +ice and correspondence address Karadzicova 8/A, 821 08 Bratisla
         +va. Invests from late-seed to Series B."                       
      16 +versute-investments,https://versute.cz,CZ,pe,yes,https://versut
         +e.cz,page,"Investujeme do malých a středních podniků prostředni
         +ctvím Private Equity fondů.",,high,"Fetched page: office Vodick
         +ova 33, 110 00 Praha 1. Also presents advisory services; type p
         +e based on PE fund manager statement."                         
      17 +viking-global-investors,,unknown,unknown,yes,https://www.viking
         +global.com,page,"a global investment firm managing $56+ billion
         + of capital.",,low,"Fetched page: public equity, private equity
         + and credit business; offices in Stamford, Hong Kong, London, N
         +ew York, San Francisco, no HQ named. Crossover/hedge profile fi
         +ts no investor_type cleanly, so unknown."                      
      18 +vocal-vc,,unknown,unknown,unknown,,,,,low,"No page fetched; Pan
         +geAI seed lead only. HQ and website not identified."           
      19 +westly-group,,unknown,unknown,unknown,,,,,low,"No page fetched;
         + Woltair investor lead only. Search budget exhausted before ver
         +ification."                                                    
      20 +white-star-capital,https://www.whitestarcapital.com,unknown,vc,
         +yes,https://www.whitestarcapital.com,page,"A global multi-stage
         + technology investment platform.",,medium,"Fetched page: runs V
         +enture, Digital Asset and Seed funds. Team location not stated;
         + map lists Toronto, Montreal, New York, Lisbon, London, Paris t
         +ied to founders/companies, not team offices."                  
      21 +wing-venture-capital,https://www.wing.vc,US,vc,yes,https://www.
         +wing.vc,page,"Palo Alto CA",,medium,"Footer of fetched page lis
         +ts Palo Alto CA as the only location; team page not fetched. Pa
         +ge: early-stage venture for AI founders. Identity match to scou
         +t's Wing Venture Capital assumed from domain, not separately co
         +nfirmed."                                                      
      22 +y-combinator,https://www.ycombinator.com,unknown,accelerator,ye
         +s,https://www.ycombinator.com,page,"invests ""$500k"" in each s
         +elected company",,medium,"Accelerator per fetched page. Page sa
         +ys YC invests $500k per company and links SAFE; equity terms no
         +t spelled out. Founders move to San Francisco; team HQ not stat
         +ed, so unknown."                                               
      23 +y-soft-ventures,,unknown,cvc,unknown,https://www.ysoft.com,page
         +,"YSoft Labs and Y Soft Ventures provide new streams of innovat
         +ion into our teams and processes.",,low,"Fetched parent site ys
         +oft.com names Y Soft Ventures as innovation stream; page does n
         +ot say it invests in companies or where it is based. cvc from s
         +cout lead (corporate arm). Parent HQ not stated on page."      
      24 +zaka-vc,https://zaka.vc,unknown,vc,yes,https://zaka.vc,page,"a 
         +seed & pre-seed VC fund, investing mainly in the US and Europe.
         +",,medium,"Fetched page lists Silicon Valley / London / Prague 
         +/ Bratislava in footer without naming an HQ. Prague from scout 
         +lead, not used as HQ."                                         
      25 +zero-gravity-capital,,unknown,unknown,unknown,,,,,low,"No page 
         +fetched; named as investor in Patron Go and Powerful Medical le
         +ads only. Identity unverified."                                
      26 +zero-one-hundred,https://www.0100.vc,SK,vc,yes,https://www.0100
         +.vc,page,"General Partner Michal Csonga is based in Slovakia",,
         +medium,"Fetched page: VC backing startups from Emerging Europe 
         +and Middle East; offices in Czechia, Slovakia, Cyprus, UAE; reg
         +istered in Nicosia (RAIF). Managing Partner based between Slova
         +kia and Cyprus. HQ SK is judgement from individual bases. Quote
         + is WebFetch summary, verify."                                 
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      23  2026-10-12,candidate-triage,haiku,batch_08,92924,64,215.8,ok
      24  2026-10-12,candidate-triage,haiku,batch_05_rerun,88189,61,199.4
          ,ok
      25  2026-10-12,candidate-triage,haiku,batch_07_rerun,73353,54,190.6
          ,ok
      26 +2026-10-12,candidate-triage,haiku,batch_09,39415,28,104.4,rerun

⏺ candidate-triage(Triage batch 09 rerun)
  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)

⏺ Meanwhile, I'll look at the Czech candidates that triage would exclude by
  type.

  Ran 1 shell command (ctrl+o to expand)

⏺ About 30 Czech candidates would get excluded by type alone, but several—like
  Springtide Ventures, Rockaway Capital, and Pale Fire Capital—look plausibly in
  scope, and wrong exclusions directly hurt the recall this pilot measures. I'm
  tightening the rule so type-only exclusion requires page evidence plus high
  confidence, and will document that decision before updating the code.

  Ran 2 shell commands (ctrl+o to expand)

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && .venv/bin/python
      - <<'EOF'
      from pathlib import Path…)
  ⎿  ...................................................
        [100%]
     51 passed in 0.23s
  ⎿  Updated docs/ai-errors.md (+1 -0)
      11  | E-05 | 2026-10-11 | candidate-scout (cvca) | Tilia Impact Ven
          tures | `website` | Ne chyba AI, ale chyba ve zdroji: odkaz v p
          rofilu CVCA vede na skylimit.cz, ačkoli text uvádí tilia.vc. | 
          Agent si nesouladu všiml. | Použita doména tilia.vc; příklad to
          ho, proč ani asociační profil není tier-1 zdroj. |
      12  | E-06 | 2026-10-12 | candidate-triage (batch 01, 04) | Accel, 
          Battery Ventures, Atomico… | `hq_country` | Haiku nechal `unkno
          wn` u sídla i zjevně zahraničních fondů (Accel, Battery Venture
          s); u batch 01 a 04 byla neznámá země u 14/25. Opakovaný běh ba
          tch 01 dopadl hůř (18/25) a mezi běhy se odpovědi liší (např. a
          irbridge NL → unknown, aspire11 unknown → CZ). | Kontrola podíl
          u `unknown` po dávce (runbook R1) a porovnání obou běhů. | Plat
          í opakovaný běh (podle runbooku); první výstup je v `data/candi
          dates/triage/rerun_first/`. `unknown` nevyřazuje, kandidát jde 
          do fronty extrakce, takže chyba zvyšuje náklad, ne ztrátu kandi
          dátů. |
      13  | E-07 | 2026-10-12 | candidate-triage (batch 04, opakovaný běh
          ) | gi21-capital | — | Stažená domovská stránka obsahovala text
           s pokynem pro model (podat zprávu o Goldman Sachs a Fifth Wall
          ), tedy prompt injection. | Agent ji rozpoznal, ignoroval a nah
          lásil. | Nic; druhý případ po E-04. Stránku gi21-capital beru j
          ako nedůvěryhodnou, extraktor a ověřovatel ji čtou jen jako dat
          a. |
      14 +| E-08 | 2026-10-12 | candidate-triage (batch 08) | springtide-
         +ventures | `investor_type` | Fond Springtide Ventures (VC ramen
         +o KKCG, Praha) označen `private_holding`, protože skupinu vlast
         +ní jedna osoba. Podle pravidel by byl vyřazen bez extrakce. | A
         +gent to sám označil k revizi; orchestrátor prošel všechna česká
         + vyřazení podle typu. | Pravidlo triáže v `decide.py` (D-015): 
         +typ vyřazuje jen se stránkou a vysokou jistotou. |             
  ⎿  Updated docs/decisions.md (+4 -0)
      54  ## D-014 · 2026-10-12 · Pravidlo pro opakování triáže: neznámé 
          sídlo u víc než třetiny dávky
      55  - Alternativy: počítat řádky s jakýmkoli `unknown` (sídlo nebo 
          typ); počítat jen typ.
      56  - Proč: runbook říká „víc než třetina dávky je `unknown`“, ale 
          neříká, které pole. Beru `hq_country`, protože právě sídlo vyřa
          zuje nejvíc kandidátů levně (zahraniční fondy). Opakují se tedy
           dávky s > 8/25 neznámými sídly (01, 04, 05, 07), každá jen jed
          nou. Platí výstup opakovaného běhu, i když je horší (u batch 01
           18/25 místo 14/25). První výstupy jsou v `data/candidates/tria
          ge/rerun_first/`. Kandidát s neznámým sídlem nebo typem se nevy
          řazuje, jde do fronty extrakce.
      57 +                                                               
      58 +## D-015 · 2026-10-12 · Triáž smí vyřadit podle typu jen se sil
         +ným důkazem                                                    
      59 +- Alternativy: vyřadit podle typu vždy (původní pravidlo); nevy
         +řazovat podle typu vůbec (dražší extrakce).                    
      60 +- Proč: po triáži by ~30 kandidátů s týmem v ČR vypadlo jen pod
         +le typu od Haiku, často ze snippetu nebo se střední či nízkou j
         +istotou. Mezi nimi jsou subjekty, které do segmentu patřit moho
         +u (Springtide Ventures je VC fond skupiny KKCG, ale triáž ho oz
         +načila `private_holding`; dále Rockaway Capital, Pale Fire Capi
         +tal, QQ Capital, TCF Capital). Chybné vyřazení českého kandidát
         +a je přesně ztráta úplnosti, kterou pilot měří. Nové pravidlo v
         + `decide.triage_decision`: vyřazení podle typu jen při `evidenc
         +e_kind=page` a `confidence=high`, jinak jde kandidát do extrakc
         +e. Vyřazení podle zahraničního sídla zůstává beze změny (sídlo 
         +se určuje snáz a cizích fondů je ve frontě nejvíc).            
  ⎿  Updated src/decide.py (+5 -0)
      247      itype = (row.get("investor_type") or "").strip()
      248      if hq and hq != "UNKNOWN" and hq != SEGMENT_COUNTRY:
      249          return "excluded", "out_of_scope_geography"
      250 +    # Type alone excludes a possibly in-segment candidate only
          + on strong evidence (D-015).                                  
      251 +    strong = ((row.get("evidence_kind") or "").strip() == "pag
          +e"                                                            
      252 +              and (row.get("confidence") or "").strip() == "hi
          +gh")                                                          
      253 +    if not strong:                                            
      254 +        return "extract", None                                
      255      if itype in TRIAGE_TYPE_EXCLUSION:
      256          return "excluded", TRIAGE_TYPE_EXCLUSION[itype]
      257      if itype == "accelerator" and (row.get("equity_investor") 
           or "").strip() == "no":
  ⎿  Updated tests/test_decide.py (+15 -6)
      173      assert validate_record(out["record"], load_validator(), st
           aging=False) == []
      174  
      175  
      176 +STRONG = {"evidence_kind": "page", "confidence": "high"}      
      177 +                                                              
      178 +                                                              
      179  @pytest.mark.parametrize("row,expected", [
      180      ({"hq_country": "US", "investor_type": "vc"}, ("excluded",
            "out_of_scope_geography")),
      178 -    ({"hq_country": "CZ", "investor_type": "pe"}, ("excluded",
          - "out_of_scope_type")),                                       
      179 -    ({"hq_country": "CZ", "investor_type": "lender"}, ("exclud
          -ed", "debt_only")),                                           
      180 -    ({"hq_country": "CZ", "investor_type": "lp_only"}, ("exclu
          -ded", "fund_of_funds_or_lp_only")),                           
      181 -    ({"hq_country": "CZ", "investor_type": "accelerator", "equ
          -ity_investor": "no"}, ("excluded", "grant_or_program_only")), 
      182 -    ({"hq_country": "CZ", "investor_type": "accelerator", "equ
          -ity_investor": "yes"}, ("extract", None)),                    
      183 -    ({"hq_country": "CZ", "investor_type": "vc"}, ("extract", 
          -None)),                                                       
      181 +    ({"hq_country": "CZ", "investor_type": "pe", **STRONG}, ("
          +excluded", "out_of_scope_type")),                             
      182 +    ({"hq_country": "CZ", "investor_type": "lender", **STRONG}
          +, ("excluded", "debt_only")),                                 
      183 +    ({"hq_country": "CZ", "investor_type": "lp_only", **STRONG
          +}, ("excluded", "fund_of_funds_or_lp_only")),                 
      184 +    ({"hq_country": "CZ", "investor_type": "accelerator", "equ
          +ity_investor": "no", **STRONG},                               
      185 +     ("excluded", "grant_or_program_only")),                  
      186 +    ({"hq_country": "CZ", "investor_type": "accelerator", "equ
          +ity_investor": "yes", **STRONG}, ("extract", None)),          
      187 +    ({"hq_country": "CZ", "investor_type": "vc", **STRONG}, ("
          +extract", None)),                                             
      188      ({"hq_country": "unknown", "investor_type": "unknown"}, ("
           extract", None)),
      189 +    # D-015: weak type evidence never excludes a candidate tha
          +t may be in the segment                                       
      190 +    ({"hq_country": "CZ", "investor_type": "private_holding", 
          +"evidence_kind": "page", "confidence": "medium"},             
      191 +     ("extract", None)),                                      
      192 +    ({"hq_country": "unknown", "investor_type": "pe", "evidenc
          +e_kind": "snippet", "confidence": "high"},                    
      193 +     ("extract", None)),                                      
      194  ])
      195  def test_triage_rules(row, expected):
      196      assert triage_decision(row) == expected

  Ran 1 shell command (ctrl+o to expand)

⏺ The new triage rule is in place: Czech or unknown-country candidates can only
  be excluded by type when the evidence is a fetched page with high confidence.
  All 51 tests pass, and it's committed and pushed. Only the batch 09 rerun is
  still running; R2 (building the extraction queue) follows once it finishes.

✻ Baked for 1m 1s · done Monday 5:21 PM

› Message from candidate-triage
  Rows written: 25 to /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/candidates/triage/batch_09.csv (input order). WebSearch budget
  ran out after 6 searches, so most finds came from fetching candidate sites
  directly, plus a few fetched pages that were reached through earlier search
  leads.
  Unknown: hq_country unknown for 16 of 25; investor_type unknown for 11 of 25.
  Ten rows have no fetched page (evidence_kind=snippet, no quote, no URL):
  tibiq, token-ventures, tomenterprise, triplebee, uk-innovations-prague,
  unbound, underground-ventures, up21, vocal-vc, zero-gravity-capital.
  Possible Czech VCs I am unsure of: ZAKA VC (zaka-vc, CZ, Prague team page,
  medium); United Founders (CZ per PEI profile "Headquarters: Prague", medium,
  team spread across cities); Tilia Impact Ventures (CZ, high, Prague address).
  Y Soft Ventures (cvc) is a CZ parent-company guess, unverified.

⏺ The batch 09 rerun is done (16 hq unknown). Search ran out again after 6
  queries, so the unknowns go to extraction. That completes R1, and I'm running
  R2 now.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && .venv/bin/python
      -m src.decide --triage && .venv/bin/python - <<'EOF'
      import csv,collections…)
  ⎿  225 candidates, 225 triaged, 158 queued for extraction -> /Users/david
     koktavy/Desktop/Investor DB Starter/data/candidates/extract_queue.csv
     [(('unknown', 'unknown'), 40), (('CZ', 'vc'), 35), (('unknown', 'vc'),
     … +8 lines (ctrl+o to expand)
  ⎿  Created data/candidates/extract_queue.csv (+159 -0)
        1 +candidate_id,name,website,triage_type,triage_hq,hint          
        2 +3ts-capital-partners,3TS Capital Partners,https://3tscapital.c
          +om,vc,unknown,TCEE Fund III and Technology in Central and East
          +ern Europe SICAR (EIF) and TCEE Fund IV (CEFoF); EIF names man
          +ager as 3TS Capital Partners Oy. Historic Czech activity (Lupa
          + 2014 mentions 3TS Cisco Growth); current investment team loca
          +tion not checked. Website not identified.                     
        3 +500-emerging-europe,500 Emerging Europe,https://e2.vc,vc,unkno
          +wn,The Village Network investor (Awards 2023 impact). Fund sta
          +tus and HQ not checked.                                       
        4 +abris-capital,Abris Capital,https://www.abris-capital.com,pe,u
          +nknown,"Abris Capital Partners. Warsaw office on CVCA profile.
          + Buyout and expansion capital in CEE, 1 CZ deal listed."      
        5 +accel,Accel,https://www.accel.com,unknown,unknown,"Example dea
          +l: Viktor USD 75M (May 2026, lead). HQ from prior knowledge. W
          +ebsite from Lupa link."                                       
        6 +accolade,Accolade,https://accolade.eu,not_an_investor,unknown,
          +"Prague 8. Owns industrial parks and Brno airport and runs a p
          +roperty fund (Accolade Fund SICAV). PLAN 2.4 cites it as the a
          +ssociate member that is a park owner, so likely real_estate_on
          +ly. Added as a borderline test case."                         
        7 +ai-startup-incubator,AI Startup Incubator,,unknown,unknown,"Li
          +sted by Vestbee with USD 150K-1.5M investment; suincubator.ai 
          +(single source, not used)."                                   
        8 +air-ventures,Air Ventures,https://airventures.eu,unknown,unkno
          +wn,Listed by Papermark and Vestbee with airventures.eu; HQ not
          + stated in either.                                            
        9 +airbridge,Airbridge,,unknown,unknown,"Smartlook exit investor 
          +(Awards 2024). Identity, HQ and type not verified; name is amb
          +iguous."                                                      
       10 +akcelerator-vsem,Akcelerátor VŠEM,,unknown,unknown,Accelerator
          + listed by Vestbee; equity terms not stated.                  
       11 +alfa8,alfa8,https://www.alfa8.com,unknown,unknown,GA Drilling 
          +investor (Awards 2025). Identity and HQ not verified.         
       12 +alpha-intelligence-capital,Alpha Intelligence Capital,,vc,unkn
          +own,Photoneo investor (Awards 2024). HQ not verified.         
       13 +angelinvest,Angelinvest,https://www.angelinvest.com,angel,unkn
          +own,Example deal: Modeinspect (Jan 2026). German fund per Lupa
          +. Website from Lupa link.                                     
       14 +arctern-ventures,ArcTern Ventures,,vc,unknown,"Woltair investo
          +r (Awards 2024). Canada is a guess from knowledge, not verifie
          +d."                                                           
       15 +arieli-capital,Arieli Capital,,unknown,unknown,Named as Powerf
          +ul Medical investor in Newstream's 2023 winners article. HQ Is
          +rael is a guess from the name; not verified.                  
       16 +arx-equity-partners,ARX Equity Partners,https://www.arxequity.
          +com,unknown,unknown,"Prague 1 office. MBO/MBI and expansion ca
          +pital per CVCA profile. | ARX CE V Cooperatief U.A., manager A
          +RX Equity Partners B.V., Czech team (EIF Czechia list); Arx CE
          +E III/IV also EIF-backed. Private equity, likely outside VC sc
          +ope. Awards 2023 PE Fund Manager finalist. Website per scout_c
          +vca.csv (CV"                                                  
       17 +aspire11,Aspire11,https://www.aspire11cap.com,vc,CZ,"Example d
          +eal: Revolut (Dec 2025, first direct investment, hundreds of m
          +illions CZK per Lupa); Vinted (Jun 2026). Late-stage platform 
          +of Pavel Mucha (Kaya) and Petr Borkovec targeting EUR 500M; bo
          +rderline growth/PE rather than VC. Website from Lupa link. | C
          +zech investment platform with EUR 500m inau"                  
       18 +aternus-family-office,Aternus Family Office,https://www.aternu
          +s.cz,family_office,CZ,"In Seedtable Czech ranking (aggregator 
          +lead, name only, not verified)."                              
       19 +badideas-fund,BADideas.fund,https://badideas.fund,vc,unknown,"
          +Named in CzechCrunch deal newsletter. Identity, HQ not verifie
          +d."                                                           
       20 +bakala-capital,Bakala Capital,https://www.bakalacapital.com,pr
          +ivate_holding,unknown,"In Seedtable Czech ranking (aggregator 
          +lead, name only, not verified)."                              
       21 +battery-ventures,Battery Ventures,https://www.battery.com,vc,u
          +nknown,"Example deal: Mews USD 300M (Jan 2026, returning inves
          +tor); also Mar 2025 round per Vestbee. HQ from prior knowledge
          +. Website not identified."                                    
       22 +bd-partners,BD Partners,https://bdpartners.cz,unknown,CZ,"Exam
          +ple deal: WanderWallet pre-seed (Mar 2026). Also Myriad AI (Se
          +p 2025). CzechCrunch Oct 2023 described it as investment vehic
          +le of two individuals, so may be private holding. Website per 
          +the Lupa article's link (domain taken from fetch summary)."   
       23 +bohemia-venture-capital,Bohemia Venture Capital,,unknown,unkno
          +wn,"Fund of the BMH group, Feedyou investor per CzechCrunch. W
          +ebsite not identified."                                       
       24 +bolt-accelerator,BOLT,,unknown,unknown,Accelerator listed by V
          +estbee; equity terms and HQ not stated.                       
       25 +bond-ventures,Bond Ventures,,unknown,unknown,"Example deal: El
          +redo (Oct 2026, new investor). Swedish investor per Lupa. Webs
          +ite not identified."                                          
       26 +borovicka-capital,Borovicka Capital,https://www.borovickacapit
          +al.com,vc,unknown,Example deal: Outfindo late-seed (Jan 2025).
          + Listed in tech.eu top investors for Czech Republic H1 2025 (2
          + deals). HQ not stated in sources seen. Website from Lupa arti
          +cle link.                                                     
       27 +bpd-partners,BPD Partners,,family_office,CZ,Powerful Medical i
          +nvestor (Awards 2023). Identity unverified.                   
       28 +braiins,Braiins,,unknown,CZ,"Listed in tech.eu top investors f
          +or Czech Republic H1 2025 (1 deal); deal not shown. Appears to
          + be an operating company (bitcoin mining software) rather than
          + a fund, so may be a corporate investor; HQ from prior knowled
          +ge, not a source. Website not identified."                    
       29 +brightcap-ventures,BrightCap Ventures,https://brightcap.vc,vc,
          +unknown,Example deal: RobosizeME (Feb 2026). Also in tech.eu t
          +op investors for Czech Republic 2024. Lupa 2022 called a Brigh
          +tcap fund Bulgarian. Website not identified.                  
       30 +btcz-ventures,BTCZ Ventures,,vc,CZ,"Example deal: Taveren Ther
          +apeutics (Dec 2025, undisclosed). HQ and nature not stated. We
          +bsite not identified."                                        
       31 +budeto,Budeto,,unknown,CZ,"Example deal: Vetstor seed EUR 1M (
          +Dec 2025, with JSK, Zaka VC, Purple). Nature of the entity (fu
          +nd, angel vehicle, company) unknown. Website not identified." 
       32 +chilli-ventures,Chilli Ventures,,unknown,CZ,"Listed in tech.eu
          + top investors for Czech Republic H1 2025 (1 deal); the specif
          +ic deal was not shown on the page, so no example deal. Aggrega
          +tor lead only. Website and HQ not identified."                
       33 +credo-ventures,Credo Ventures,https://www.credoventures.com,vc
          +,CZ,"Prague (Karlovo namesti 10). Start-up and growth VC in IT
          +/internet per CVCA profile. | Example deal: Delta Green (Oct 2
          +025, with Tilia and Purple). Also Picogrid (US, Jun 2026) and 
          +Duvo.ai (Dec 2025). Website: homepage fetched, lists offices i
          +n Prague and Krakow. | EIF-backed active funds: Credo Sta"    
       34 +crescendo-ventures,Crescendo Ventures,,vc,unknown,"Example dea
          +l: Aiviro EUR 450k (Dec 2025, with Danube Angels and JIC Ventu
          +res). Romanian fund per Lupa. Website not identified. | Romani
          +an fund in the Aiviro round (Lupa 2025-12-12)."               
       35 +czech-business-angels-association,Czech Business Angels Associ
          +ation (CBAA),,angel,CZ,"Association of angel clubs; ellty list
          +s cbaa.cz (single source, not used). Probably not an investor 
          +itself."                                                      
       36 +czech-founders-vc,Czech Founders VC,https://czechfounders.vc,v
          +c,CZ,"Example deal: Merchantee (Jun 2026, participated). Named
          + most active investor of 2024 (9 deals) in CzechCrunch review 
          +(Jan 2025). Fund of the Czech Founders community. Website not 
          +found without guessing. | Founders-backed alternative investme
          +nt fund (45 founders, about EUR 10m; CzechCrunch 2022). Aw"   
       37 +czechinvest,CzechInvest,https://czechinvest.gov.cz,public_agen
          +cy,CZ,"Government agency; ellty.com says CZK 646M committed to
          + about 260 startups in 2025 (grants / incubation). Expected ex
          +clusion as grant program. Domain confirmed by a czechinvest.go
          +v.cz URL in search results. | State agency running startup pro
          +grammes (CzechAccelerator, CzechStartups, ESA BIC). Expecte"  
       38 +decibel,Decibel,https://decibel.vc,vc,unknown,"Example deal: E
          +2B seed USD 11.5M (Oct 2024, lead, with KAYA VC and Sunflower 
          +Capital). HQ from prior knowledge. Website not identified."   
       39 +decibel-vc,Decibel VC,https://decibel.vc,vc,unknown,E2B invest
          +or (Awards 2025).                                             
       40 +dendis-capital,Dendis Capital,https://www.dendiscapital.com,fa
          +mily_office,CZ,"Example deal: Carebot EUR 400k (Jan 2026). Als
          +o HTG Medical (Jul 2026, Vestbee). Led by the Dendis couple pe
          +r Lupa. Website from Lupa link."                              
     … 119 more lines (ctrl+o to expand)

⏺ Agent "Triage batch 09 rerun" finished · 5m 3s

⏺ R2 queued 158 candidates for extraction. That's over the 70 cap, so I'll rank
  them deterministically and take the top 70.

  Ran 1 shell command (ctrl+o to expand)

⏺ The cut falls inside a tie, so I'll demote candidates the scouts put abroad
  and break any remaining ties alphabetically.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && mkdir -p scripts
      2>/dev/null; cat > src/select_queue.py <<'EOF'
      """Pick the extraction batch when the qu…)
  ⎿  158 queued, top 70 -> /Users/davidkoktavy/Desktop/Investor DB Starter/
     data/candidates/extract_selected.csv; cut-off score 3/1/0
     rank,score,candidate_id,name,website,triage_type
     … +18 lines (ctrl+o to expand)
  ⎿  Created data/candidates/extract_selected.csv (+71 -0)
       1 +rank,score,candidate_id,name,website,triage_type,triage_hq,hint
       2 +1,4/2/1,aspire11,Aspire11,https://www.aspire11cap.com,vc,CZ,"Ex
         +ample deal: Revolut (Dec 2025, first direct investment, hundred
         +s of millions CZK per Lupa); Vinted (Jun 2026). Late-stage plat
         +form of Pavel Mucha (Kaya) and Petr Borkovec targeting EUR 500M
         +; borderline growth/PE rather than VC. Website from Lupa link. 
         +| Czech investment platform with EUR 500m inau"                
       3 +2,4/2/1,credo-ventures,Credo Ventures,https://www.credoventures
         +.com,vc,CZ,"Prague (Karlovo namesti 10). Start-up and growth VC
         + in IT/internet per CVCA profile. | Example deal: Delta Green (
         +Oct 2025, with Tilia and Purple). Also Picogrid (US, Jun 2026) 
         +and Duvo.ai (Dec 2025). Website: homepage fetched, lists office
         +s in Prague and Krakow. | EIF-backed active funds: Credo Sta"  
       4 +3,4/2/1,czech-founders-vc,Czech Founders VC,https://czechfounde
         +rs.vc,vc,CZ,"Example deal: Merchantee (Jun 2026, participated).
         + Named most active investor of 2024 (9 deals) in CzechCrunch re
         +view (Jan 2025). Fund of the Czech Founders community. Website 
         +not found without guessing. | Founders-backed alternative inves
         +tment fund (45 founders, about EUR 10m; CzechCrunch 2022). Aw" 
       5 +4,4/2/1,depo-ventures,DEPO Ventures,https://depoventures.com,vc
         +,CZ,"Prague 7. CVCA profile shows no website; domain found via 
         +search of its own news/portfolio pages (angel fund and syndicat
         +e deals). Tickets EUR 50-300k per profile. | Example deal: Wand
         +erWallet pre-seed USD 500k (Mar 2026, with BD Partners). Also R
         +eadmio (Feb 2026), ArcSpace (France, Aug 2026); new U"         
       6 +5,4/2/1,fazole-ventures,Fazole Ventures,https://www.fazole.vc,v
         +c,CZ,"Example deal: Everbot (Sep 2025, 12.2% stake). Run by Pav
         +el Bouska, Lubos Cerny, Pavel Prikryl per Lupa. HQ is a guess f
         +rom the Czech context. Website from Lupa link. | Named as CBAA 
         +founding member by ellty. Not verified."                       
       7 +6,4/2/1,founder-institute-prague,Founder Institute Prague,https
         +://fi.co,accelerator,CZ,Accelerator chapter listed by Vestbee; 
         +equity terms not stated in fetched pages.                      
       8 +7,4/2/1,gi21-capital,Gi21 Capital,https://www.gi21capital.com,v
         +c,CZ,"Example deal: FaceUp (May 2026). Also Hermetiq (US, Aug 2
         +026) and Zerops (May 2026, Lupa teaser). Fund of Damir Spoljari
         +c per Lupa. Website from Lupa link. | Prague fund of Damir Špol
         +jarič; lead investor in Zerops seed round of EUR 1.7m (Lupa 202
         +6-05-18). Website not identified."                             
       9 +8,4/2/1,i-and-i-biotech,i&i Biotech Fund (i&i Bio),https://www.
         +inibio.eu,vc,CZ,"Brand i&i Bio (i&i Biotech Fund). Prague 8. Ea
         +rly-stage biotech VC per own site title. | Example deal: Antive
         +rse (Mar 2026, led by Soulmates Ventures). Czech link from Czec
         +hCrunch Jan 2024 (CasInvent Pharma, with i&i Prague), outside w
         +indow. Website not identified. | EUR 50m biomedical tech-transf
         +er"                                                            
      10 +9,4/2/1,i-and-i-prague,i&i Prague,https://www.iniprague.com,acc
         +elerator,CZ,"Biotech incubator at IOCB; co-created i&i Biotech 
         +Fund with EIF; Vestbee lists iniprague.com (single source, not 
         +used)."                                                        
      11 +10,4/2/1,impulse-ventures,Impulse Ventures,,vc,CZ,"Wikipedia li
         +st and AIN rank 14 (H1 2022); Lupa names Ondřej Tomek (Impulse 
         +Ventures) as a Spinoffy backer. Vestbee lists impulseventures.c
         +om (single source, not used)."                                 
      12 +11,4/2/1,incomming-ventures,InCOMMing Ventures,,vc,CZ,"In Seedt
         +able Czech ranking (aggregator lead, name only, not verified)."
      13 +12,4/2/1,inven-capital,Inven Capital,https://www.invencapital.c
         +z,cvc,CZ,"Prague 4. Corporate fund of CEZ Group, later-stage cl
         +eantech growth investments. | Corporate VC of CEZ Group. Awards
         + 2024 VC Fund Manager finalist; Woltair investor. Website per P
         +apermark, Failory and scout_cvca.csv."                         
      14 +13,4/2/1,j-t-ventures,J&T Ventures,https://www.jtventures.cz,vc
         +,CZ,"Example deal: Definic seed (Jun 2026, lead). Also Wultra S
         +eries A (Jun 2026, existing investor) and Oddin.gg (Jun 2025, m
         +ain investor). Website from Lupa article links. | Daytrip inves
         +tor (Awards 2024); linked to J&T group per Lupa. Website per Pa
         +permark, ellty, Vestbee, Failory."                             
      15 +14,4/2/1,jic-ventures,JIC Ventures,https://www.jic.cz/ventures/
         +,vc,CZ,"Example deal: FaceUp (May 2026, fund's first investment
         +; Fil Rouge Capital led). Also Elredo lead (Oct 2026), Aiviro (
         +Dec 2025), Groundcom (Jun 2025). Brno; fund still raising (E15 
         +Apr 2026: about 40 LPs); parent JIC agency invested from own mo
         +ney earlier. Website fetched. | Brno, CZK 400m pre-seed/"      
      16 +15,4/2/1,koopeo-ventures,Koopeo Ventures,https://koopeoventures
         +.com,vc,CZ,"Prague impact investor; Vestbee lists koopeoventure
         +s.com (single source, not used). Deafcom investor in Awards 202
         +2 (outside 2023-2025 window)."                                 
      17 +16,4/2/1,lighthouse-ventures,Lighthouse Ventures,https://lhv.vc
         +,vc,CZ,"Example deal: Outfindo late-seed EUR 1.2M (Jan 2025). A
         +lso Merchantee (Jun 2026), Hermetiq (US, Aug 2026), Patron Go (
         +earlier investor). Website from Lupa article link. | Lighthouse
         + Seed Fund and Lighthouse Seed Fund (Prague), manager Lighthous
         +e Ventures GP s.r.o. (EIF signed 2023-12-28). Awards 202"      
      18 +17,4/2/1,longevitytech-fund,Longevitytech.fund,,vc,CZ,Prague; A
         +IN rank 11 H1 2022 with 40+ investments. Website not listed by 
         +Vestbee.                                                       
      19 +18,4/2/1,look-ai-ventures,Look AI Ventures,https://lookai.vc,vc
         +,CZ,"Example deal: Lucida AI seed extension (Jun 2026). Also So
         +dex Innovations (Austria, Jul 2026), Embodied AI (Switzerland, 
         +Sep 2026), Digicust (Austria, Dec 2025). Called a Prague fund b
         +y Lupa. Website from Lupa links."                              
      20 +19,4/2/1,miton,Miton,https://miton.cz,vc,CZ,"Example deal: ACE 
         +padel app (Oct 2026, CZK millions). Also Whisper (Feb 2026), Ba
         +ndits (Nov 2025), DeepScout (Jan 2025); seller of Driveto (Apr 
         +2025). Described by Lupa as an investment group, so type may be
         + holding rather than VC. Domain seen in a search-result URL (mi
         +ton.cz/podcast); homepage not "                                
      21 +20,4/2/1,nation1,N1 Ventures (formerly Nation 1),https://n1.roc
         +ks,vc,CZ,"Prague 1. Pre-seed/seed fund of about EUR 35m, also r
         +uns acceleration batches per own site. | Example deal: Human Ar
         +chive seed (Jun 2026, USD 8.2M led by Wing VC and NVP Capital).
         + Also Flick (US, May 2026), Myriad AI (Sep 2025). Website n1.ro
         +cks from Lupa links; legacy domain nation1.vc fetched OK ("    
      22 +21,4/2/1,novira-capital,Novira Capital,,vc,CZ,Smartlook exit in
         +vestor alongside Reflex (Awards 2024; CzechCrunch headline name
         +s Reflex and Novira). HQ guessed CZ. Website not identified.   
      23 +22,4/2/1,orbit-capital,Orbit Capital,https://orbitcapital.com,v
         +c,CZ,"Prague 4. Growth equity (EUR 6-15m) plus venture debt (EU
         +R 2-6m): mixed-portfolio edge case from PLAN 2.4; type could be
         + vc. | Example deal: IAG EUR 6M (Jun 2026, equity plus venture 
         +debt, new investor); also Sloneek (Jun 2026). Raised EUR 107M g
         +rowth-debt fund with PFR Ventures (Poland) as LP (Vest"        
      24 +23,4/2/1,patero,Patero,https://www.patero.cz,vc,CZ,"Earlier inv
         +estor in Outfindo (named in Jan 2025 article, not in that round
         +). Nature of entity unknown. Website not identified. | Named as
         + Carebot / Flowpay investor in CzechCrunch article. Identity no
         +t verified."                                                   
      25 +24,4/2/1,presto-ventures,Presto Tech Horizons (Tech Horizons),h
         +ttps://prestoventures.com,vc,CZ,"Example deal: Tech Horizons fu
         +nd (CSG + Presto Ventures) first three investments Vidar System
         +s, Bavovna, Tur.ai (Oct 2024); also listed on Ready Player Me e
         +xit to Netflix (Dec 2025, CzechCrunch). Lupa headline 11 Mar 20
         +26: police detained a Presto Ventures founder (headline only, n
         +ot opened). Websit"                                            
      26 +25,4/2/1,purple-ventures,Purple Ventures,https://www.purple-ven
         +tures.com,vc,CZ,"Example deal: Flae Robotics (Oct 2026, with Ga
         +rage Angels). Also Fether Labs (UK, May 2026), Delta Green (Oct
         + 2025). Brno per CzechCrunch Apr 2024 fund report. Website from
         + Lupa article links. | Brno; Delta Green investor (Awards 2025 
         +impact); second fund targeting EUR 40m per CzechCrunch. Website
         + n"                                                            
      27 +26,4/2/1,purposetech,PurposeTech,,vc,CZ,"Prague, first pre-seed
         + fund EUR 2.3m (Vestbee Q4 2024). Pale Fire news mentions a rel
         +ated seed fund (Purpose Ventures) per scout_cvca.csv. Website n
         +ot identified."                                                
      28 +27,4/2/1,reflex-capital,Reflex Capital,https://www.reflexcapita
         +l.com,vc,CZ,"Example deal: Merchantee (Jun 2026, lead). Also Gr
         +id.online (Jun 2026) and Choice (Mar 2026). Website from Lupa a
         +rticle links. | Investor in Keboola and Smartlook exit (Awards 
         +2024) and FaceUp (Awards 2025 impact); third fund about CZK 0.5
         +bn per CzechCrunch. Website per Papermark, ellty, Vestbee, Fa" 
      29 +28,4/2/1,rockaway-ventures,Rockaway Ventures,https://www.rockaw
         +ayventures.com,vc,CZ,"Example deal: Vermeer Series A (USD 10M, 
         +Oct 2025, with Draper Associates). Also Remix (Bulgaria, Dec 20
         +25, CzechCrunch). Related to rockaway-capital and rockawayx (se
         +parate rows, dedupe downstream). Website empty: rockawaycapital
         +.com appears only in ellty.com list and fetch was blocked. | Se
         +cond fu"                                                       
      30 +29,4/2/1,rockawayx,RockawayX,,vc,CZ,"Named in Lupa Dec 2025 (Ro
         +ckawayX to join Solmate, USD 2B under management). No startup i
         +nvestment seen in window, so activity unclear. Rockaway group c
         +rypto/blockchain arm. Website not identified without guessing. 
         +| Listed by Papermark with rockawayx.com (single source, not us
         +ed). Scope and HQ not "                                        
      31 +30,4/2/1,seed-starter,Seed Starter (Ceska sporitelna),https://w
         +ww.seedstarter.cz,cvc,CZ,"Example deal: Definic seed (Jun 2026)
         +. Also Repsense (Lithuania, Dec 2025). Corporate accelerator / 
         +investment vehicle of Ceska sporitelna. Website from Lupa artic
         +le link. | Bank. Example deal: PalmApp (2025; CzechCrunch Jan 2
         +026 says the bank is withdrawing). Also LP in JIC Ventures (E15
         + Apr 2026) "                                                   
      32 +31,4/2/1,seed-starter-ceske-sporitelny,Seed Starter České spoři
         +telny,https://www.seedstarter.cz,cvc,CZ,"Bank-run startup inves
         +tment programme; a Slovak version (Seed Starter Slovenskej spor
         +itelne) is also named. Česká spořitelna is also an LP in Tilia,
         + i&i Bio and JIC Ventures. Website not identified."            
      33 +32,4/2/1,soulmates-ventures,Soulmates Ventures,https://www.soul
         +matesventures.com,vc,CZ,"Example deal: Antiverse (Mar 2026, led
         + USD 9.3M). Also Rightcharge (UK, Oct 2025 and Sep 2026). Lupa 
         +Mar 2025: plans EUR 50M for green startups. Website from Lupa l
         +ink. | Prague, EUR 50m sustainable-startup fund (Vestbee Q1 202
         +5). Failory lists soulmatesventures.com (single source, not use
         +d). Also n"                                                    
      34 +33,4/2/1,spinoffy,Spinoffy,,vc,CZ,"Fund launched Mar 2026 for u
         +niversity spin-offs (Lupa); backers named include Jan Barta (Pa
         +le Fire) and Ondrej Tomek; no portfolio deal seen. Structure vi
         +a J&T Banka and Amista. Website not found. | Proof-of-concept f
         +und for university tech spin-offs (Lupa 2026-03-02); founded by
         + Jana Soukupová, Ale"                                          
      35 +34,4/2/1,startguide-vc,Startguide VC,https://startguide.cz,vc,C
         +Z,"Earlier investor in Carebot (named in Jan 2026 article, not 
         +in the new round). Printed as VC StartGuide. HQ and website not
         + identified. | Prague per Failory (lists startguide.cz, single 
         +source, not used). Also Carebot / Flowpay investor in CzechCrun
         +ch article."                                                   
      36 +35,4/2/1,startupyard,StartupYard,https://startupyard.com,accele
         +rator,CZ,"Accelerator that provides a first cheque; ellty.com l
         +ists 2025 cohorts incl. Ydoca and Personeo.ai but gives no inve
         +stment. Aggregator lead only, no in-window deal seen in news. W
         +ebsite empty: startupyard.com appears only in ellty.com list. |
         + Prague accelerator, EUR 40K investment per Vestbee; Credo"    
      37 +36,4/2/1,tachles,Tachles VC,,vc,CZ,"Named in Lupa Nov 2025 for 
         +a US partner helping portfolio firms ThreatMark and ShieldIOT; 
         +no investment in window seen. CzechCrunch Apr 2024 described a 
         +new fund by ex-Springtide partners. Website not identified. | N
         +ew fund targeting over CZK 1bn, launched by Karel Tušek and Dav
         +id Marek, ex-Springti"                                         
      38 +37,4/2/1,tensor-ventures,Tensor Ventures,https://tensor.venture
         +s,vc,CZ,"Prague 1. Deeptech VC. CVCA profile shows no website; 
         +tensor.ventures inferred from its official blog subdomain blog.
         +tensor.ventures (apex page not opened). | Example deal: Edmund 
         +(Apr 2026, with Forward.one lead). Also Cnuic (UK, Apr 2026), P
         +angeAI (2026). Lupa May 2024 links it to EIF / National R"     
      39 +38,4/2/1,tilia-impact-ventures,Tilia Impact Ventures,https://ti
         +lia.vc,vc,CZ,"Listed as honorary member among full members. Pra
         +gue 5. Impact VC, CZK 1-5m tickets. CVCA profile hyperlink wron
         +gly points to skylimit.cz; displayed text tilia.vc confirmed by
         + search. | Example deal: FaceUp (May 2026, existing investor). 
         +Also Delta Green (Oct 2025). Website from Lupa link. | Tilia I"
      40 +39,4/2/1,united-founders,United Founders,,vc,CZ,"Example deal: 
         +first investments Wonderful.ai and EveryHealth (Nov 2025); also
         + quantum-chip and drone plant-nutrition startups (Apr 2026, Lup
         +a). Co-founded by Jakub Havrlant and Vit Horky; offices in many
         + European cities incl. Prague, so location of the investment te
         +am needs checking. Website not fou"                            
     … 31 more lines (ctrl+o to expand)
  ⎿  Created src/select_queue.py (+50 -0)
       1 +"""Pick the extraction batch when the queue is longer than the 
         +pilot budget (runbook R3, D-016).                              
       2 +                                                               
       3 +    python -m src.select_queue [N]   (default 70)              
       4 +                                                               
       5 +Ranks data/candidates/extract_queue.csv by how strongly triage 
         +and the scouts hint at a Czech VC                              
       6 +and writes the top N, with rank and score, to data/candidates/e
         +xtract_selected.csv.                                           
       7 +"""                                                            
       8 +                                                               
       9 +import csv                                                     
      10 +import sys                                                     
      11 +                                                               
      12 +from src.config import DATA                                    
      13 +                                                               
      14 +CAND = DATA / "candidates"                                     
      15 +QUEUE = CAND / "extract_queue.csv"                             
      16 +SELECTED = CAND / "extract_selected.csv"                       
      17 +VC_LIKE = ("vc", "cvc", "accelerator")                         
      18 +UNCLEAR = ("", "unknown", "private_holding", "family_office")  
      19 +                                                               
      20 +                                                               
      21 +def score(row: dict, hq_guess: str) -> tuple[int, int, int]:   
      22 +    hq = {"CZ": 2, "UNKNOWN": 1, "": 1}.get(row["triage_hq"].st
         +rip().upper(), 0)                                              
      23 +    kind = 2 if row["triage_type"] in VC_LIKE else 1 if row["tr
         +iage_type"] in UNCLEAR else 0                                  
      24 +    guess = hq_guess.strip().upper()                           
      25 +    scout = 1 if guess == "CZ" else 0 if not guess else -1     
      26 +    return hq + kind, hq, scout                                
      27 +                                                               
      28 +                                                               
      29 +def main(argv: list[str]) -> int:                              
      30 +    n = int(argv[0]) if argv else 70                           
      31 +    guesses = {r["candidate_id"]: r.get("hq_guess") or ""      
      32 +               for r in csv.DictReader(open(CAND / "cz_vc.csv",
         + encoding="utf-8"))}                                           
      33 +    queue = list(csv.DictReader(open(QUEUE, encoding="utf-8")))
      34 +    for r in queue:                                            
      35 +        r["score"] = score(r, guesses.get(r["candidate_id"], ""
         +))                                                             
      36 +    queue.sort(key=lambda r: r["candidate_id"])                
      37 +    queue.sort(key=lambda r: r["score"], reverse=True)         
      38 +    fields = ["rank", "score"] + [k for k in queue[0] if k not 
         +in ("score",)]                                                 
      39 +    with open(SELECTED, "w", newline="", encoding="utf-8") as f
         +:                                                              
      40 +        w = csv.DictWriter(f, fieldnames=fields)               
     … 10 more lines (ctrl+o to expand)

⏺ The selection is deterministic, except the final 7 slots which break ties
  alphabetically—an arbitrary but documented choice. Next, I'll write a small
  test, record the decision with the unprocessed candidates list, and commit.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && cat >
      tests/test_select_queue.py <<'EOF'
      from src.select_queue import score…)
  ⎿  52 passed in 0.24s
     - Alternativy: extrahovat všech 158 (zhruba dvojnásobný čas a tokeny,
     většina zbytku jsou zahraniční fondy nebo PE); vybrat ručně.
     … +12 lines (ctrl+o to expand)
  ⎿  Updated docs/decisions.md (+5 -0)
      58  ## D-015 · 2026-10-12 · Triáž smí vyřadit podle typu jen se sil
          ným důkazem
      59  - Alternativy: vyřadit podle typu vždy (původní pravidlo); nevy
          řazovat podle typu vůbec (dražší extrakce).
      60  - Proč: po triáži by ~30 kandidátů s týmem v ČR vypadlo jen pod
          le typu od Haiku, často ze snippetu nebo se střední či nízkou j
          istotou. Mezi nimi jsou subjekty, které do segmentu patřit moho
          u (Springtide Ventures je VC fond skupiny KKCG, ale triáž ho oz
          načila `private_holding`; dále Rockaway Capital, Pale Fire Capi
          tal, QQ Capital, TCF Capital). Chybné vyřazení českého kandidát
          a je přesně ztráta úplnosti, kterou pilot měří. Nové pravidlo v
           `decide.triage_decision`: vyřazení podle typu jen při `evidenc
          e_kind=page` a `confidence=high`, jinak jde kandidát do extrakc
          e. Vyřazení podle zahraničního sídla zůstává beze změny (sídlo 
          se určuje snáz a cizích fondů je ve frontě nejvíc).
      61 +                                                               
      62 +## D-016 · 2026-10-12 · Fronta extrakce: 158 kandidátů, zpracov
         +áno 70 s nejsilnější nápovědou českého VC                      
      63 +- Alternativy: extrahovat všech 158 (zhruba dvojnásobný čas a t
         +okeny, většina zbytku jsou zahraniční fondy nebo PE); vybrat ru
         +čně.                                                           
      64 +- Proč: runbook (R3) omezuje pilot na 70. Pořadí počítá kód (`s
         +rc/select_queue.py` → `data/candidates/extract_selected.csv`): 
         +skóre = sídlo z triáže (CZ 2, neznámé 1, cizí 0) + typ z triáže
         + (vc/cvc/akcelerátor 2, neznámý/holding/FO 1, jiný 0); při shod
         +ě rozhoduje sídlo, pak tip scouta (`hq_guess` CZ > prázdný > ci
         +zí), nakonec abecedně. Hranice vyšla uvnitř skupiny 3/1/0 (nezn
         +ámé sídlo, typ VC, bez tipu scouta), posledních 7 míst v ní je 
         +tedy dáno abecedou.                                            
      65 +- Nezpracováno (88, v `cz_vc_decisions.csv` zůstanou `pending` 
         +s příznakem): abris-capital, accel, accolade, ai-startup-incuba
         +tor, air-ventures, airbridge, akcelerator-vsem, alfa8, angelinv
         +est, arctern-ventures, arieli-capital, arx-equity-partners, bak
         +ala-capital, battery-ventures, bohemia-venture-capital, bolt-ac
         +celerator, bond-ventures, brightcap-ventures, crescendo-venture
         +s, czech-business-angels-association, czechinvest, decibel, dec
         +ibel-vc, electron-capital-partners, esa-bic-czech-republic, eur
         +opean-investment-fund, evolving-europe, experian, fivesquare, f
         +tmo, gain-ventures, garage-angels, genesis-capital, goldman-sac
         +hs-alternatives, google-ventures, hartenberg, headline, integra
         +l-capital-group, investown, ipm, itaca-business-incubator, ivbf
         +, j-t-arch, jafam-holding, jaro-capital, jet-investment, jinej-
         +fond, keiretsu-forum-prague, kendaxa-group, longevity-fellows, 
         +lumus-investment-collective, mam-private-equity, mid-europa-par
         +tners, narodni-rozvojova-investicni, nato-diana, new-vision-3, 
         +northzone, np-investments, orizon-systems, pale-fire-capital, p
         +artech, plug-and-play, point-nine, proxy-finance, qi-investicni
         +-spolecnost, riverside-acceleration-capital, rsj-investments, r
         +tp-global, safar-and-partners, seedtwo-capital, skylimit-invest
         +ments, stratum-partners, tarpan-partners, tibiq, token-ventures
         +, tomenterprise, triplebee, uk-innovations-prague, unbound, und
         +erground-ventures, university2ventures, up21, value4capital, vi
         +king-global-investors, vocal-vc, white-star-capital, y-combinat
         +or, zero-gravity-capital.                                      
  ⎿  Created tests/test_select_queue.py (+10 -0)
       1 +from src.select_queue import score                             
       2 +                                                               
       3 +                                                               
       4 +def test_czech_vc_ranks_above_unknown_and_foreign_hints():     
       5 +    cz_vc = score({"triage_hq": "CZ", "triage_type": "vc"}, "CZ
         +")                                                             
       6 +    unknown_vc = score({"triage_hq": "unknown", "triage_type": 
         +"vc"}, "")                                                     
       7 +    unknown_vc_foreign_guess = score({"triage_hq": "unknown", "
         +triage_type": "vc"}, "US")                                     
       8 +    cz_pe = score({"triage_hq": "CZ", "triage_type": "pe"}, "CZ
         +")                                                             
       9 +    assert cz_vc > unknown_vc > unknown_vc_foreign_guess       
      10 +    assert unknown_vc > cz_pe                                  

⏺ The push was rejected because the remote has commits I don't have. I'll see
  what they are before integrating.
  Ran 1 shell command (ctrl+o to expand)

⏺ These are documentation commits (README, ai-log) that touch none of my files,
  so a merge is safe.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && git pull -q
      --no-rebase --no-edit && git push -q 2>&1|tail -2; git log --oneline -4)
  ⎿  7dcb2e4 Merge branch 'main' of https://github.com/DavidKoktavy/investo
     r-db
     d49d1b3 src: select_queue ranks the extraction queue by Czech-VC hints
     … +6 lines (ctrl+o to expand)
  ⎿  Updated README.md (+116 -25)
  ⎿  Created ai-log/README.md (+11 -0)
  ⎿  … 1 more file changed
  ⎿  (a git step in this command can move the working tree, so these may be
     its changes, not edits) (ctrl+o to expand)

⏺ I'll add the missing run-log row for the batch 09 rerun, then start the R3
  trial on the first 4 selected candidates.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-12,candidate-triage,haiku,batch_09_rerun,58189,45,303.2,ok" >>
      data/runs/run_log.csv && se…)
  ⎿  rank,score,candidate_id,name,website,triage_type,triage_hq,hint
     1,4/2/1,aspire11,Aspire11,https://www.aspire11cap.com,vc,CZ,"Example d
     eal: Revolut (Dec 2025, first direct investment, hundreds of millions
     … +20 lines (ctrl+o to expand)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      24  2026-10-12,candidate-triage,haiku,batch_05_rerun,88189,61,199.4
          ,ok
      25  2026-10-12,candidate-triage,haiku,batch_07_rerun,73353,54,190.6
          ,ok
      26  2026-10-12,candidate-triage,haiku,batch_09,39415,28,104.4,rerun
      27 +2026-10-12,candidate-triage,haiku,batch_09_rerun,58189,45,303.2
         +,ok                                                            

  Ran 1 shell command (ctrl+o to expand)

⏺ 4 background agents launched (↓ to manage)
   ├ Extract aspire11
   ├ Extract credo-ventures
   ├ Extract czech-founders-vc
   └ Extract depo-ventures

⏺ The R3 trial is running: 4 extractions (Aspire11, Credo Ventures, Czech
  Founders VC, DEPO Ventures). When they finish, I'll read each record against
  its sources before releasing the rest of the queue.

✻ Churned for 1m 17s · done Monday 5:26 PM

› Message from investor-extractor
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/credo-ventures.json and `src.validate` passed.
  - 1 evidence item within 24 months, the newest dated 2026-05-29: Picogrid
  Series A, which is a tier-3 Raise Track newsletter listing.
  - `capital` is null (not_published). Nothing else is null. Fund IV size (EUR
  75m) comes from a 2022 interview and the fund's name is unconfirmed.
  - Borderline: the web search budget ran out. The Delta Green and Duvo.ai deals
  from the hint were not verified. The Picogrid role is "unknown" and there is
  no primary press release. Homepage quotes were obtained via WebFetch, so
  check_quotes should confirm them. The ticket currency is USD, taken from the
  "$" sign, and the legal entity (Credo Ventures a.s., IČO 28538137) is sourced
  from a tier-3 podnikatel.cz mirror.

⏺ The extractor also hit the WebSearch limit, which is now the main blocker for
  the pilot. I'll check whether search works from this session right now.

⏺ Web Search("Credo Ventures Delta Green investice")
  ⎿  Did 1 search in 5s

⏺ Agent "Extract credo-ventures" finished · 1m 3s

› Message from investor-extractor
  - Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/aspire11.json. `src.validate` passed.
  - 2 evidence items are within 24 months (Vinted and Revolut, both from
  Lupa.cz). The newest is Vinted, 2026-06-23.
  - Fields left null: `legal_entities` (empty list), `sectors`, `ticket` (all
  `not_published`), and `capital.as_of`/fund `vintage`.
  - Borderline: Aspire11 is a late-stage growth platform that is part
  direct-investor and part fund-of-funds (the Tribes strategy), so I typed it
  `vc` with a growth subtype. The legal entity is unconfirmed, because ASP11
  Services s.r.o. (IČO 17255384, Pavel Mucha as jednatel) is not provably
  Aspire11, so I left it out. The Czech HQ rests on Lupa calling it a "Český
  fond", not on the investor's own site. The Vinted and Revolut roles are weak:
  Vinted is `unknown`, and Revolut is `participant` on Lupa's reporting, with
  the Revolut amount not public. The €515M inaugural fund comes only from the
  website's "€515M" stat (check the quote matches, since the label "Inaugural
  fund" sits in a separate element), with no close date.
  - The quote check has not been run yet.

⏺ Agent "Extract aspire11" finished · 1m 3s

› Message from investor-extractor
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/czech-founders-vc.json; src.validate passed (1/1
  valid).
  Evidence dated within the last 24 months: 2 (Merchantee 2026-06-09, Maxfusion
  2026-01-14); newest is 2026-06-09. Counting the 2022 type, capital and fund
  sources as well, 4 further sourced items are older than that.
  Left null: sectors (not_published). Legal entity found: Czech Founders
  Ventures s.r.o., IČO 17051835, from the or.justice.cz search page.
  Borderline: the Czech Founders VC fund vehicle is not in the register entry,
  only the management company. Capital of EUR 10m (basis latest_fund_size) comes
  from a 2022 CzechCrunch article. The registry quote is the name field of the
  search result row, so check_quotes may flag it as weak. The Maxfusion EUR 350k
  is a combined figure, not a ticket. Flowlance (Nov 2024) was not fetched, so
  it is not cited.

⏺ Agent "Extract czech-founders-vc" finished · 1m 7s

⏺ Bash(cd /private/tmp/claude-502/-Users-davidkoktavy-Desktop-Investor-DB-Starte
      r/6238d8d8-ae85-4d21-9ac0-3145a465eb96/tasks/ && grep -oiE
      '.{0,120}(budget|limit|excee…)
  ⎿  ugrep: error: error at position 382
     4[\x80-\x8f][\x80-\xbf][\x80-\xbf]){0,160}
                  exceeds complexity limits___/
  ⎿  Shell cwd was reset to /Users/davidkoktavy/Desktop/Investor DB Starter
  ⎿  (another command ran in this repository at the same time; a change 
     made by either may show under either result)

⏺ Bash(cd /private/tmp/claude-502/-Users-davidkoktavy-Desktop-Investor-DB-Starte
      r/6238d8d8-ae85-4d21-9ac0-3145a465eb96/tasks/ && LC_ALL=C grep -oE
      '.{0,100}(max_uses|s…)
  ⎿  ugrep: error: error at position 396
     \x80-\xbf]|\xf4[\x80-\x8f][\x80-\xbf][\x80-\xbf]){0,120}
                                exceeds complexity limits___/
  ⎿  Shell cwd was reset to /Users/davidkoktavy/Desktop/Investor DB Starter
  ⎿  (another command ran in this repository at the same time; a change 
     made by either may show under either result)

⏺ Bash(cd /private/tmp/claude-502/-Users-davidkoktavy-Desktop-Investor-DB-Starte
      r/6238d8d8-ae85-4d21-9ac0-3145a465eb96/tasks/ && /usr/bin/python3 -c "
      import re,sys…)
  ⎿      \"candidate_source\": \"extract_queue.csv\",","+    \"notes\": \"W
     eb search budget ran out; Delta Green and Duvo.ai deals from hint not
     verified from a fetched page. Picogrid evidence is a newsletter li
     … +15 lines (ctrl+o to expand)
  ⎿  Shell cwd was reset to /Users/davidkoktavy/Desktop/Investor DB Starter
  ⎿  (another command ran in this repository at the same time; a change 
     made by either may show under either result)

⏺ Bash(cd /private/tmp/claude-502/-Users-davidkoktavy-Desktop-Investor-DB-Starte
      r/6238d8d8-ae85-4d21-9ac0-3145a465eb96/tasks/ && /usr/bin/python3 -c "
      import re…)
  ⎿  :"617cd1ea-df34-49ed-a16c-b7c2524ed286","isSidechain":true,"promptId":
     "a6451421-5711-4a28-8a86-0bdc8bca7c21","agentId":"a197787348b08fa73","
     type":"user","message":{"role":"user","content":[{"tool_use_id":"toolu
     … +10 lines (ctrl+o to expand)
  ⎿  Shell cwd was reset to /Users/davidkoktavy/Desktop/Investor DB Starter
  ⎿  (another command ran in this repository at the same time; a change 
     made by either may show under either result)

⏺ Subagents share one session-wide budget of 200 WebSearch calls (refilling
  ~100/hour), and triage used most of it — since extraction quality depends on
  search, I'll pace remaining extractions to the refill rate instead of running
  them degraded. First I'll review the trial records.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && .venv/bin/python
      - <<'EOF'
      import json…)
  ⎿  ===== credo-ventures
      hq_country: "CZ" | null:None | https://www.credoventures.com t2 sr:Tr
     ue pub:None
     … +92 lines (ctrl+o to expand)
  ⎿  (another command ran in this repository at the same time; a change 
     made by either may show under either result)

⏺ Triage and extraction queue are done; reviewing the 4 trial extractions before
  the remaining 66, I've spotted two issues—context-less quotes (e.g.
  Aspire11's "€515M", Credo's missing check-size stage) and search budget limits
  causing missed deals. I'll check the fourth (DEPO) record once it's in, then
  update the extractor prompt to fix both.

  Ran 1 shell command (ctrl+o to expand)

⏺ Waiting for DEPO before I edit, so all four trial records inform one prompt
  change.

✻ Churned for 49s · done Monday 5:28 PM

› Message from investor-extractor
  - Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/depo-ventures.json; src.validate passed.
  - Evidence items dated within the last 24 months: 0. Both deals (WanderWallet
  co-lead, Tapaya lead) are on depoventures.com posts that print no date, so
  announced_date is null. The only March 2026 date is on CB Insights, an
  aggregator I did not use.
  - Null fields: legal_entities is empty (the footer names DEPO VENTURES s.r.o.
  but no IČO or registry page was found), capital (not_published), funds is
  empty, and announced_date is null on both deals.
  - Borderline: the web search budget ran out, so no registry lookup and no
  external dated source. Readmio and ArcSpace are unconfirmed. The ticket is the
  homepage figure of EUR 250-500k, not the hint's EUR 50-300k. Sectors and
  stages are mapped from the homepage ("Defence, Space, FinTech, Industry 4.0,
  Energy"; "Inception & Pre-seed"). The Czech team is confirmed only by the
  Prague 7 address, so the record has no recent dated deal.

⏺ DEPO shows a third systematic issue. Both its deals come from its own undated
  posts, so the record has no dated activity and code would exclude an active
  fund as no_recent_investment. I'm updating the extractor prompt with all fixes
  in one commit, then deleting the 4 trial records per the runbook.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && .venv/bin/python
      - <<'EOF'
      from pathlib import Path…)
  ⎿   .claude/agents/investor-extractor.md | 6 +++++-
      data/runs/run_log.csv                | 1 +
      2 files changed, 6 insertions(+), 1 deletion(-)
  ⎿  Updated .claude/agents/investor-extractor.md (+5 -1)
      16  
      17  1. **Identity.** Open the website (about, team, contact, imprin
          t/legal notice, "Kontakt", "O nás"). Find the legal entity and 
          its registration number. For Czech companies the website imprin
          t usually names the company and its IČO; confirm it in a regist
          ry if you can (search `"<company name>" IČO` or `site:or.justic
          e.cz <name>`; `rejstrik-firem.kurzy.cz` and `firmy.cz` pages ar
          e acceptable tier-3 mirrors of the register). Regulated manager
          s are in the ČNB JERRS register. Record where the investment te
          am sits (`hq_country`).
      18  2. **Activity.** Find the most recent investments: the portfoli
          o page, the investor's news, portfolio-company press releases, 
          Czech and international tech/business media. Search in Czech an
          d English, e.g. `"<name>" investice`, `"<name>" investoval`, `"
          <name>" led round`, `"<name>" seed`. Record up to 3 of the most
           recent deals, preferring sources that state the announcement d
          ate. Always record the single most recent deal you found, even 
          if it is older than 24 months; code needs it to mark the invest
          or dormant.
      19 -3. **Profile.** `type`, `sectors` (map to the schema taxonomy a
         -nd keep the investor's own wording in `raw`), `stages`, typical
         - first `ticket`, `capital`, `funds`.                           
      19 +   An undated page (e.g. the investor's own portfolio entry or 
         +blog post with no printed date) cannot prove a recent deal: for
         + the newest deals, find a dated source (the portfolio company's
         + press release, a media article, a dated news post) and cite th
         +at instead.                                                    
      20 +3. **Profile.** `type`, `sectors` (map to the schema taxonomy a
         +nd keep the investor's own wording in `raw`), `stages` (every s
         +tage the source names, not just the first one), typical first `
         +ticket`, `capital`, `funds`.                                   
      21  4. **Exclusion signals.** If a source shows the candidate is so
          mething the database excludes (PLAN §2.4) — it only lends, is a
          n adviser or intermediary, a crowdfunding platform, a grant pro
          gramme or accelerator without equity, invests only into other f
          unds, only in real estate or only in listed shares — add an ite
          m to `exclusion_signals` with the code, a source and a one-line
           note. If the candidate cannot be found at all or has closed do
          wn, add `not_found_or_defunct` (source optional). Record the fa
          cts even when you also found investments: code weighs both.
      22  5. **Write** `data/records/staging/<candidate_id>.json` even wh
          en the candidate turns out not to be a venture investor, is for
          eign, or is defunct: a record with honest nulls and signals is 
          how the exclusion gets decided and measured. It must validate a
          gainst the schema: run `.venv/bin/python -m src.validate data/r
          ecords/staging/<candidate_id>.json` and fix every error it prin
          ts. Set `status` to `"pending"` and `exclusion_reason` to `null
          `.
      23  
      24  ## Evidence rules
      25  
      26  - **Quotes:** the exact text fragment from the page, ≤ 25 words
          . WebFetch answers through a small model, so always ask it for 
          verbatim text, e.g. "Return, verbatim and without paraphrasing,
           the exact sentences that mention <X>." Never quote a search-re
          sult snippet.
      27 +- **A quote must show what the value is**, not just the value: 
         +"Inaugural fund: €515M", not "€515M"; "Typical ticket EUR 250-5
         +00k", not "250-500k". If the label and the number are not in on
         +e passage on the page, the value is `null` (`not_published`) an
         +d you explain it in `meta.notes`.                              
      28  - **One source per value.** Pick the most reliable (tier 1 > 2 
          > 3) and, among equals, the most recent.
      29  - **Tier:** 1 = regulator/registry; 2 = the investor itself, th
          e portfolio company, or an LP (EIF, NRB); 3 = media, associatio
          ns, other third parties.
      30  - **Dates:** `published_date` = the date printed on the page, e
          lse `null`. `accessed_date` = today.
     ...
      46  
      47  About 15 tool calls is normally enough; stop at 30. A record wi
          th nulls is better than an endless search.
      48  
      49 +**Web search is scarce:** every agent in the session shares one
         + WebSearch budget. Use at most 6 WebSearch calls per candidate.
         + Fetch the candidate's own pages first (home, portfolio, news, 
         +team, contact, imprint) and spend searches on what they cannot 
         +give you: a dated source for the newest deals and the registry 
         +entry. If WebSearch replies that the budget is used up, do not 
         +retry and do not work around it; finish with what you have and 
         +start `meta.notes` with `SEARCH_BUDGET_EXHAUSTED`.             
      50 +                                                               
      51  ## Final message
      52  
      53  At most 5 short lines (the orchestrator collects dozens of thes
          e):
  ⎿  PostToolUse:Bash says: Tip: Run /ultrareview before you push to catch bugs 
     with a cloud-based multi-agent review — 3 free reviews left.
⏺ Agent "Extract depo-ventures" finished · 3m 15s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && cat >>
      data/runs/run_log.csv <<'EOF'
      2026-10-12,investor-extractor,sonnet,aspire11,40426,15,63.2,rerun…)
  ⎿  0
  ⎿  Deleted data/records/staging/aspire11.json (+0 -141)
        1 -{                                                             
        2 -  "schema_version": "1.0",                                    
        3 -  "id": "aspire11",                                           
        4 -  "name": "Aspire11",                                         
        5 -  "website": "https://www.aspire11cap.com",                   
        6 -  "hq_country": {                                             
        7 -    "value": "CZ",                                            
        8 -    "source": {                                               
        9 -      "url": "https://www.lupa.cz/aktuality/fond-aspire11-much
          -y-a-borkovce-poslal-skoro-pul-miliardy-do-platformy-vinted/", 
       10 -      "tier": 3,                                              
       11 -      "publisher": "Lupa.cz",                                 
       12 -      "published_date": "2026-06-23",                         
       13 -      "accessed_date": "2026-10-12",                          
       14 -      "quote": "Český fond Aspire11, který založil Pavel Mucha
          - (Kaya VC) a Petr Borkovec (Partners)",                       
       15 -      "self_reported": false                                  
       16 -    },                                                        
       17 -    "note": "Described as a Czech fund by media; team location
          - not stated on the investor's website."                       
       18 -  },                                                          
       19 -  "legal_entities": [],                                       
       20 -  "type": {                                                   
       21 -    "value": "vc",                                            
       22 -    "subtype": "late-stage growth / pension-capital platform",
       23 -    "source": {                                               
       24 -      "url": "https://www.aspire11cap.com",                   
       25 -      "tier": 2,                                              
       26 -      "publisher": "Aspire11",                                
       27 -      "published_date": null,                                 
       28 -      "accessed_date": "2026-10-12",                          
       29 -      "quote": "Direct investments in late-stage and pre-IPO t
          -echnology companies with enduring growth, market leadership, a
          -nd long-term compounding potential.",                         
       30 -      "self_reported": true                                   
       31 -    },                                                        
       32 -    "note": "Borderline growth/PE; also a Tribes strategy inve
          -sting in VC funds."                                           
       33 -  },                                                          
       34 -  "sectors": {                                                
       35 -    "value": null,                                            
       36 -    "raw": null,                                              
       37 -    "null_reason": "not_published"                            
       38 -  },                                                          
       39 -  "stages": {                                                 
       40 -    "value": [                                                
     … 101 more lines (ctrl+o to expand)
  ⎿  Deleted data/records/staging/credo-ventures.json (+0 -167)
        1 -{                                                             
        2 -  "schema_version": "1.0",                                    
        3 -  "id": "credo-ventures",                                     
        4 -  "name": "Credo Ventures",                                   
        5 -  "website": "https://www.credoventures.com",                 
        6 -  "hq_country": {                                             
        7 -    "value": "CZ",                                            
        8 -    "source": {                                               
        9 -      "url": "https://www.credoventures.com",                 
       10 -      "tier": 2,                                              
       11 -      "publisher": "Credo Ventures",                          
       12 -      "published_date": null,                                 
       13 -      "accessed_date": "2026-10-12",                          
       14 -      "quote": "Karlovo Náměstí 10, 120 00, Prague, Czech Repu
          -blic",                                                        
       15 -      "self_reported": true                                   
       16 -    },                                                        
       17 -    "note": "Offices in Prague and Kraków; Prague listed first
          -."                                                            
       18 -  },                                                          
       19 -  "legal_entities": [                                         
       20 -    {                                                         
       21 -      "name": "Credo Ventures a.s.",                          
       22 -      "registry": "CZ-OR",                                    
       23 -      "registry_id": "28538137",                              
       24 -      "role": "management_company",                           
       25 -      "source": {                                             
       26 -        "url": "https://www.podnikatel.cz/rejstrik/credo-ventu
          -res-a-s-28538137/",                                           
       27 -        "tier": 3,                                            
       28 -        "publisher": "podnikatel.cz (mirror of obchodní rejstř
          -ík)",                                                         
       29 -        "published_date": null,                               
       30 -        "accessed_date": "2026-10-12",                        
       31 -        "quote": "Credo Ventures a.s.",                       
       32 -        "self_reported": false                                
       33 -      }                                                       
       34 -    }                                                         
       35 -  ],                                                          
       36 -  "type": {                                                   
       37 -    "value": "vc",                                            
       38 -    "subtype": null,                                          
       39 -    "source": {                                               
       40 -      "url": "https://www.credoventures.com",                 
     … 127 more lines (ctrl+o to expand)
  ⎿  Deleted data/records/staging/czech-founders-vc.json (+0 -166)
        1 -{                                                             
        2 -  "schema_version": "1.0",                                    
        3 -  "id": "czech-founders-vc",                                  
        4 -  "name": "Czech Founders VC",                                
        5 -  "website": "https://czechfounders.vc",                      
        6 -  "hq_country": {                                             
        7 -    "value": "CZ",                                            
        8 -    "source": {                                               
        9 -      "url": "https://czechfounders.vc",                      
       10 -      "tier": 2,                                              
       11 -      "publisher": "Czech Founders VC",                       
       12 -      "published_date": null,                                 
       13 -      "accessed_date": "2026-10-12",                          
       14 -      "quote": "Worklounge, Gen. Píky 430/26, 160 00, Prague 6
          -, Czechia",                                                   
       15 -      "self_reported": true                                   
       16 -    }                                                         
       17 -  },                                                          
       18 -  "legal_entities": [                                         
       19 -    {                                                         
       20 -      "name": "Czech Founders Ventures s.r.o.",               
       21 -      "registry": "CZ-OR",                                    
       22 -      "registry_id": "17051835",                              
       23 -      "role": "management_company",                           
       24 -      "source": {                                             
       25 -        "url": "https://or.justice.cz/ias/ui/rejstrik-$firma?n
          -azev=Czech+Founders+Ventures",                                
       26 -        "tier": 1,                                            
       27 -        "publisher": "Obchodní rejstřík",                     
       28 -        "published_date": null,                               
       29 -        "accessed_date": "2026-10-12",                        
       30 -        "quote": "Czech Founders Ventures s.r.o., osoba riziko
          -vého kapitálu",                                               
       31 -        "self_reported": false                                
       32 -      }                                                       
       33 -    }                                                         
       34 -  ],                                                          
       35 -  "type": {                                                   
       36 -    "value": "vc",                                            
       37 -    "subtype": "founder-backed pre-seed fund",                
       38 -    "source": {                                               
       39 -      "url": "https://cc.cz/uspesni-cesti-startupiste-budou-po
          -mahat-novym-nadejim-vybrali-na-to-mezi-sebou-ctvrt-miliardy/",
       40 -      "tier": 3,                                              
     … 126 more lines (ctrl+o to expand)
  ⎿  Deleted data/records/staging/depo-ventures.json (+0 -132)
        1 -{                                                             
        2 -  "schema_version": "1.0",                                    
        3 -  "id": "depo-ventures",                                      
        4 -  "name": "DEPO Ventures",                                    
        5 -  "website": "https://depoventures.com",                      
        6 -  "hq_country": {                                             
        7 -    "value": "CZ",                                            
        8 -    "source": {                                               
        9 -      "url": "https://depoventures.com",                      
       10 -      "tier": 2,                                              
       11 -      "publisher": "DEPO Ventures",                           
       12 -      "published_date": null,                                 
       13 -      "accessed_date": "2026-10-12",                          
       14 -      "quote": "Plynární 10 street",                          
       15 -      "self_reported": true                                   
       16 -    }                                                         
       17 -  },                                                          
       18 -  "legal_entities": [],                                       
       19 -  "type": {                                                   
       20 -    "value": "vc",                                            
       21 -    "subtype": "early-stage, angel/syndicate",                
       22 -    "source": {                                               
       23 -      "url": "https://depoventures.com",                      
       24 -      "tier": 2,                                              
       25 -      "publisher": "DEPO Ventures",                           
       26 -      "published_date": null,                                 
       27 -      "accessed_date": "2026-10-12",                          
       28 -      "quote": "Backing early-stage founders since 2016",     
       29 -      "self_reported": true                                   
       30 -    }                                                         
       31 -  },                                                          
       32 -  "sectors": {                                                
       33 -    "value": [                                                
       34 -      "cybersecurity_defense",                                
       35 -      "fintech",                                              
       36 -      "industrial_manufacturing",                             
       37 -      "climate_energy",                                       
       38 -      "deeptech_hardware"                                     
       39 -    ],                                                        
       40 -    "raw": "Defence, Space,FinTech, Industry 4.0, Energy",    
     … 92 more lines (ctrl+o to expand)
  ⎿  Created data/records/trial_01/aspire11.json (+141 -0)
        1 +{                                                             
        2 +  "schema_version": "1.0",                                    
        3 +  "id": "aspire11",                                           
        4 +  "name": "Aspire11",                                         
        5 +  "website": "https://www.aspire11cap.com",                   
        6 +  "hq_country": {                                             
        7 +    "value": "CZ",                                            
        8 +    "source": {                                               
        9 +      "url": "https://www.lupa.cz/aktuality/fond-aspire11-much
          +y-a-borkovce-poslal-skoro-pul-miliardy-do-platformy-vinted/", 
       10 +      "tier": 3,                                              
       11 +      "publisher": "Lupa.cz",                                 
       12 +      "published_date": "2026-06-23",                         
       13 +      "accessed_date": "2026-10-12",                          
       14 +      "quote": "Český fond Aspire11, který založil Pavel Mucha
          + (Kaya VC) a Petr Borkovec (Partners)",                       
       15 +      "self_reported": false                                  
       16 +    },                                                        
       17 +    "note": "Described as a Czech fund by media; team location
          + not stated on the investor's website."                       
       18 +  },                                                          
       19 +  "legal_entities": [],                                       
       20 +  "type": {                                                   
       21 +    "value": "vc",                                            
       22 +    "subtype": "late-stage growth / pension-capital platform",
       23 +    "source": {                                               
       24 +      "url": "https://www.aspire11cap.com",                   
       25 +      "tier": 2,                                              
       26 +      "publisher": "Aspire11",                                
       27 +      "published_date": null,                                 
       28 +      "accessed_date": "2026-10-12",                          
       29 +      "quote": "Direct investments in late-stage and pre-IPO t
          +echnology companies with enduring growth, market leadership, a
          +nd long-term compounding potential.",                         
       30 +      "self_reported": true                                   
       31 +    },                                                        
       32 +    "note": "Borderline growth/PE; also a Tribes strategy inve
          +sting in VC funds."                                           
       33 +  },                                                          
       34 +  "sectors": {                                                
       35 +    "value": null,                                            
       36 +    "raw": null,                                              
       37 +    "null_reason": "not_published"                            
       38 +  },                                                          
       39 +  "stages": {                                                 
       40 +    "value": [                                                
     … 101 more lines (ctrl+o to expand)
  ⎿  … 6 more files changed

⏺ Trial records are archived and the prompt fix is committed separately. Since
  the search budget's likely drained, I'll wait about 20 minutes for it to
  refill before re-running the 4-record trial.

  Ran 1 shell command (ctrl+o to expand)

⏺ I'm waiting about 20 minutes for the search budget to refill, then I'll re-run
  the 4-record extraction trial with the updated prompt.

✻ Cooked for 24m 37s · done Monday 5:30 PM

※ recap: Running the pilot runbook R0–R8 for the Czech VC database: triage and the 70-candidate extraction queue are done, and I tightened the extractor prompt after a 4-record trial. Next, once the shared web-search limit refills (~20 min), I'll re-run that trial. (disable recaps in /config)

⏺ Background command "Wait 20 minutes for search budget refill" completed (exit
code 0)

⏺ Wait over. I'm re-running the 4-record trial with the updated prompt.

⏺ 4 background agents launched (↓ to manage)
   ├ Extract aspire11 (trial 2)
   ├ Extract credo-ventures (trial 2)
   ├ Extract czech-founders-vc (trial 2)
   └ Extract depo-ventures (trial 2)

⏺ The 4 trial extractions are running again with the updated prompt. When they
  finish, I'll review them against their sources before starting on the rest of
  the queue.

✻ Cooked for 15s · done Monday 5:51 PM

› Message from investor-extractor
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/credo-ventures.json. `src.validate` passed.
  - 2 evidence items dated within the last 24 months: Picogrid (2026-05-29,
  newest) and Duvo.ai (2025-12-03). The third, Delta Green, is 2024-05-27 and
  outside the window.
  - Null fields: sectors and capital (not_published). `funds` is an empty list
  because no fund size was published on the investor's own site.
  - Borderline: all three deals come from tier-3 sources, and the roles are
  `participant`. Credo's own pages carry no dates, so the Delta Green Oct 2025
  deal has no dated source and I cited the 2024 round instead. The legal entity
  (Credo Ventures a.s., IČO 28538137) comes from a podnikatel.cz mirror (tier
  3), not the registry. Stages hold only pre_seed, because the homepage says
  "Leading Pre-Seed rounds". The 2020 Silicon Canals article says seed and
  Series A, but I did not use it.

⏺ The Credo Ventures redo is better: 2 dated deals in the window, and only
  pre-seed in stages is backed by the current homepage. I'll log the usage once
  the notification arrives and wait for the other three.

✻ Crunched for 2s · done Monday 5:52 PM

⏺ Agent "Extract credo-ventures (trial 2)" finished · 1m 3s

⏺ Agent "Extract czech-founders-vc (trial 2)" finished · 1m 5s

› Message from investor-extractor
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/czech-founders-vc.json, and `src.validate`
  passed.
  - 2 evidence items are dated within the last 24 months: Merchantee
  (2026-06-03, Nordic9) and Maxfusion (2026-01-14, CzechCrunch). The newest date
  is 2026-06-03.
  - Left null or empty: sectors (not_published), capital (not_published),
  `funds` (empty), `legal_entities` (empty). The legal entity "Czech Founders
  Ventures s.r.o." appears in the site footer, but I found no IČO or registry
  page, so K1 will have nothing to check.
  - Borderline: the hq_country quote is the Prague office address from the site
  contact section, which I took from WebFetch output and did not check verbatim,
  so check_quotes may mark it weak. Maxfusion has role and instrument set to
  unknown (CzechCrunch only says EUR 350k "od Czech Founders VC"). The EUR 10m
  fund figure comes only from a 2022 CzechCrunch article with no label I could
  quote, so I left it out.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && cat >>
      data/runs/run_log.csv <<'EOF'
      2026-10-12,investor-extractor,sonnet,credo-ventures,33897,17,62.6,o…)
  ⎿  Updated data/runs/run_log.csv (+2 -0)
      29  2026-10-12,investor-extractor,sonnet,credo-ventures,31744,15,62
          .7,rerun
      30  2026-10-12,investor-extractor,sonnet,czech-founders-vc,31833,15
          ,66.9,rerun
      31  2026-10-12,investor-extractor,sonnet,depo-ventures,33926,22,195
          .5,rerun
      32 +2026-10-12,investor-extractor,sonnet,credo-ventures,33897,17,62
         +.6,ok                                                          
      33 +2026-10-12,investor-extractor,sonnet,czech-founders-vc,32256,13
         +,64.9,ok                                                       
  ⎿  (another command ran in this repository at the same time; a change 
     made by either may show under either result)

  Ran 1 shell command (ctrl+o to expand)

⏺ Czech Founders' Merchantee deal now cites a news page on Nordic9, a
  startup-data platform. The prompt already says aggregators are leads, not
  evidence, so that may be a borderline breach; the verifier and manual review
  will see it. Two trial records are still running.

✻ Cogitated for 10s · done Monday 5:52 PM

› Message from investor-extractor
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/aspire11.json. src.validate passed.
  Evidence: 2 items within 24 months (Vinted 2026-06-23, Revolut 2025-12-09,
  both Lupa.cz tier 3). Newest date is 2026-06-23. Role and instrument are
  "unknown" for both.
  Null fields: ticket (not_published). Capital and fund size are EUR 515M
  "inaugural fund" from the investor's homepage (basis latest_fund_size, vintage
  null). Legal entities, tier 2 from the investor's /legal page, are not
  confirmed in a registry: Aspire 11 Capital SICAV, a.s. (23620030) and Partners
  investiční společnost, a.s. (24716006).
  Borderline: late-stage/pre-IPO growth (stage "growth", type "vc" with a note),
  so it may be PE rather than VC. hq CZ rests on Lupa calling Aspire11 a "Česká
  investiční platforma"; no source gives a city, and Lupa mentions a London
  presence. Funding is Czech pension capital.

⏺ Aspire11's redo is better too: the capital quote now carries the "inaugural
  fund" label, and it found the legal entities on the investor's own legal page.
  Waiting on DEPO, the most important test of the dated-evidence fix.

✻ Churned for 2s · done Monday 5:52 PM

⏺ Agent "Extract aspire11 (trial 2)" finished · 1m 13s

› Message from investor-extractor
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/depo-ventures.json. src.validate passed.
  Evidence: 2 dated items within 24 months. The newest is Tapaya, 2026-04-29
  (Vestbee, co_lead). The other is WanderWallet, 2026-03-13 (cc.cz, role
  unknown).
  Nulls: capital (not_published), funds (empty), and legal_entities (empty; no
  IČO found on the site and no registry page located).
  Borderline:
  - Angel-fund and syndicate roots, with a "current fund" whose size is not
  published.
  - The WanderWallet quote is a short fragment ("a andělský fond Depo
  Ventures.").
  - The hint's Readmio and ArcSpace deals were not verified, so I left them out.
  - The ticket and stage values are self-reported on the home page.
  - Used 5 of 6 searches.

⏺ DEPO's redo now has 2 dated deals in the window, so the dated-source fix
  worked. All four trial records look sound, with no further systematic
  problems. I'll log the runs, commit, and start the rest of the queue in rounds
  of 4 paced to the search refill.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-12,investor-extractor,sonnet,aspire11,32604,14,73.1,ok" >>
      data/runs/run_log.csv && git ad…)
  ⎿  {
       "candidate_id": "fazole-ventures",
       "name": "Fazole Ventures",
     … +29 lines (ctrl+o to expand)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      31  2026-10-12,investor-extractor,sonnet,depo-ventures,33926,22,195
          .5,rerun
      32  2026-10-12,investor-extractor,sonnet,credo-ventures,33897,17,62
          .6,ok
      33  2026-10-12,investor-extractor,sonnet,czech-founders-vc,32256,13
          ,64.9,ok
      34 +2026-10-12,investor-extractor,sonnet,aspire11,32604,14,73.1,ok 

⏺ Agent "Extract depo-ventures (trial 2)" finished · 3m 19s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-12,investor-extractor,sonnet,depo-ventures,36545,19,199.0,ok" >>
      data/runs/run_log.csv)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      32  2026-10-12,investor-extractor,sonnet,credo-ventures,33897,17,62
          .6,ok
      33  2026-10-12,investor-extractor,sonnet,czech-founders-vc,32256,13
          ,64.9,ok
      34  2026-10-12,investor-extractor,sonnet,aspire11,32604,14,73.1,ok
      35 +2026-10-12,investor-extractor,sonnet,depo-ventures,36545,19,199
         +.0,ok                                                          

⏺ 4 background agents launched (↓ to manage)
   ├ Extract fazole-ventures
   ├ Extract founder-institute-prague
   ├ Extract gi21-capital
   └ Extract i-and-i-biotech

⏺ Round 1 of the main queue is running (ranks 5–8). Meanwhile I'll write a small
  helper that lists queue rows still lacking a staging record and fills in
  run-log rows.

  Read 1 file (ctrl+o to expand)

⏺ The helper is ready, and four extractions are running: Fazole Ventures,
  Founder Institute Prague, Gi21 Capital and i&i Biotech. When they're done I'll
  log them and start the next round once the search budget allows.

✻ Churned for 32s · done Monday 5:54 PM
› Message from investor-extractor
  - Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/founder-institute-prague.json. src.validate
  passed.
  - 0 evidence-of-activity items, so no dated evidence and no newest date.
  - Left null: hq_country, type, sectors, stages, ticket and capital.
  legal_entities and funds are empty.
  - Borderline: this is a paid accelerator run by Founder Institute, Inc. (US).
  I recorded `grant_or_program_only` as an exclusion signal, citing the
  fi.co/faq quote about the 2.5% equity warrant to the Equity Collective. I
  found no investments, no Czech registry entry, and no evidence of where the
  Prague team sits.
  - I did not fetch the fi.co Prague launch article that the search surfaced, so
  nothing is cited from it.

⏺ Founder Institute Prague is done: no investments found and an exclusion signal
  recorded, so it should drop out at the decide step. Three extractions are
  still running.

✻ Churned for 1s · done Monday 5:55 PM

⏺ Agent "Extract founder-institute-prague" finished · 42s

› Message from investor-extractor
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/fazole-ventures.json, and src.validate passed.
  Evidence dated within the last 24 months: 1 item (Everbot, Lupa.cz,
  2025-09-16, the newest). The other item is GoodAccess, 2023-02-03, which is
  older.
  Left null: sectors (only preferred sectors are listed, no clean taxonomy
  mapping), capital, and funds (empty, because no fund size is published).
  Borderline:
  - The Everbot role is recorded as "unknown". The cc.cz tag page says "Lídrem
  investičního kola se stal fond Fazole Ventures", but it doesn't name the
  startup. The Lupa article names Everbot and carries the same date.
  - The IČO (07491492) and hq_country come only from the kurzy.cz tier-3
  registry mirror. HQ is the registered Prague seat, not an explicit statement
  about where the team sits.
  - Ticket is EUR 50k to 800k from the English page. The Czech page says 1–20
  mil. CZK, which is roughly consistent.
  - No 2026 deal found.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo "2026-10-12,
      investor-extractor,sonnet,founder-institute-prague,26365,8,42.4,ok" >>
      data/runs/run_lo…)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      33  2026-10-12,investor-extractor,sonnet,czech-founders-vc,32256,13
          ,64.9,ok
      34  2026-10-12,investor-extractor,sonnet,aspire11,32604,14,73.1,ok
      35  2026-10-12,investor-extractor,sonnet,depo-ventures,36545,19,199
          .0,ok
      36 +2026-10-12,investor-extractor,sonnet,founder-institute-prague,2
         +6365,8,42.4,ok                                                 

⏺ Agent "Extract fazole-ventures" finished · 1m 10s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-12,investor-extractor,sonnet,fazole-ventures,33669,15,69.6,ok" >>
      data/runs/run_log.csv; s…)
  ⎿  62 remaining
     {
       "candidate_id": "i-and-i-prague",
     … +17 lines (ctrl+o to expand)
  ⎿  Created data/records/staging/gi21-capital.json (+141 -0)
        1 +{                                                             
        2 +  "schema_version": "1.0",                                    
        3 +  "id": "gi21-capital",                                       
        4 +  "name": "Gi21 Capital",                                     
        5 +  "website": "https://www.gi21capital.com",                   
        6 +  "hq_country": {                                             
        7 +    "value": "CZ",                                            
        8 +    "source": {                                               
        9 +      "url": "https://www.lupa.cz/aktuality/vyvojarsky-zerops-
          +ziskal-1-7-milionu-eur-chce-je-i-na-expanzi-mimo-evropu/",    
       10 +      "tier": 3,                                              
       11 +      "publisher": "Lupa.cz",                                 
       12 +      "published_date": "2026-05-18",                         
       13 +      "accessed_date": "2026-10-12",                          
       14 +      "quote": "Hlavním investorem je pražský fond Gi21 Capita
          +l Damira Špoljariče.",                                        
       15 +      "self_reported": false                                  
       16 +    }                                                         
       17 +  },                                                          
       18 +  "legal_entities": [                                         
       19 +    {                                                         
       20 +      "name": "Gi21 Capital a.s.",                            
       21 +      "registry": "CZ-OR",                                    
       22 +      "registry_id": "19584229",                              
       23 +      "role": "other",                                        
       24 +      "source": {                                             
       25 +        "url": "https://ares.gov.cz/ekonomicke-subjekty-v-be/r
          +est/ekonomicke-subjekty/19584229",                            
       26 +        "tier": 1,                                            
       27 +        "publisher": "ARES (Ministerstvo financí)",           
       28 +        "published_date": null,                               
       29 +        "accessed_date": "2026-10-12",                        
       30 +        "quote": "\"ico\":\"19584229\",\"obchodniJmeno\":\"Gi2
          +1 Capital a.s.\"",                                            
       31 +        "self_reported": false                                
       32 +      }                                                       
       33 +    }                                                         
       34 +  ],                                                          
       35 +  "type": {                                                   
       36 +    "value": "vc",                                            
       37 +    "subtype": "multi-stage investment group (also data centre
          +s, hospitality)",                                             
       38 +    "source": {                                               
       39 +      "url": "https://www.gi21capital.com",                   
       40 +      "tier": 2,                                              
     … 101 more lines (ctrl+o to expand)
  ⎿  Created data/records/staging/i-and-i-biotech.json (+167 -0)
        1 +{                                                             
        2 +  "schema_version": "1.0",                                    
        3 +  "id": "i-and-i-biotech",                                    
        4 +  "name": "i&i Biotech Fund (i&i Bio)",                       
        5 +  "website": "https://www.inibio.eu",                         
        6 +  "hq_country": {                                             
        7 +    "value": "CZ",                                            
        8 +    "source": {                                               
        9 +      "url": "https://rejstrik-firem.kurzy.cz/10885978/",     
       10 +      "tier": 3,                                              
       11 +      "publisher": "kurzy.cz (Obchodní rejstřík mirror)",     
       12 +      "published_date": null,                                 
       13 +      "accessed_date": "2026-10-12",                          
       14 +      "quote": "Sídlo firmy Biotech Investments s.r.o. je Pobř
          +ežní 394/12, Karlín, 186 00 Praha.",                          
       15 +      "self_reported": false                                  
       16 +    },                                                        
       17 +    "note": "Fund vehicle is Luxembourg SCSp; Prague-based inv
          +estment adviser Biotech Investments s.r.o. and Czech partners 
          +form the team."                                               
       18 +  },                                                          
       19 +  "legal_entities": [                                         
       20 +    {                                                         
       21 +      "name": "Biotech Investments s.r.o.",                   
       22 +      "registry": "CZ-OR",                                    
       23 +      "registry_id": "10885978",                              
       24 +      "role": "other",                                        
       25 +      "source": {                                             
       26 +        "url": "https://rejstrik-firem.kurzy.cz/10885978/",   
       27 +        "tier": 3,                                            
       28 +        "publisher": "kurzy.cz (Obchodní rejstřík mirror)",   
       29 +        "published_date": null,                               
       30 +        "accessed_date": "2026-10-12",                        
       31 +        "quote": "Biotech Investments s.r.o. , Praha IČO 10885
          +978 - Obchodní rejstřík firem",                               
       32 +        "self_reported": false                                
       33 +      }                                                       
       34 +    }                                                         
       35 +  ],                                                          
       36 +  "type": {                                                   
       37 +    "value": "vc",                                            
       38 +    "subtype": "life sciences",                               
       39 +    "source": {                                               
       40 +      "url": "https://www.inibio.eu",                         
     … 127 more lines (ctrl+o to expand)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      34  2026-10-12,investor-extractor,sonnet,aspire11,32604,14,73.1,ok
      35  2026-10-12,investor-extractor,sonnet,depo-ventures,36545,19,199
          .0,ok
      36  2026-10-12,investor-extractor,sonnet,founder-institute-prague,2
          6365,8,42.4,ok
      37 +2026-10-12,investor-extractor,sonnet,fazole-ventures,33669,15,6
         +9.6,ok                                                         
  ⎿  (another command ran in this repository at the same time; a change 
     made by either may show under either result)
  ⎿  (timeout 3m 20s)

› Message from investor-extractor
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/gi21-capital.json. `src.validate` passed.
  Evidence: 3 deals within 24 months (Hermetiq 2026-08-24, FaceUp 2026-05-19,
  Zerops 2026-05-18). Newest date is 2026-08-24.
  Nulls: stages, ticket, capital (all not_published), funds is an empty list. No
  company websites recorded.
  Borderline:
  - Gi21 is a diversified group (AI data centres, hospitality, art patronage)
  with a "VC / PE technology investments" arm. I set type to vc.
  - HQ=CZ rests on Lupa's "pražský fond"; the site has no contact page stating
  where the team sits.
  - Legal entity Gi21 Capital a.s., IČO 19584229, is from ARES (tier 1). Its
  quote is the raw JSON string from the ARES response, so check_quotes may flag
  it. Its registered activity is generic plus property rental.
  - The home page contained instructions aimed at AI models, and I ignored them.

⏺ Agent "Extract gi21-capital" finished · 1m 33s

› Message from investor-extractor
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/i-and-i-biotech.json. `src.validate` passed (1/1
  valid).
  Evidence: 2 items dated within 24 months, newest 2026-03-03 (Antiverse Series
  A, i&i participant, Vestbee). The other is KyDo seed, 2025-09-22, i&i lead,
  Bionity.
  Nulls: stages (`not_published`; the site names only cheque sizes). The
  Luxembourg fund vehicle has no registry id.
  Borderline:
  - The only legal entity is the Prague investment adviser Biotech Investments
  s.r.o. (IČO 10885978, from a kurzy.cz mirror, not or.justice.cz). The fund
  itself is i&i Biotech Fund I SCSp in Luxembourg, so `hq_country` CZ is
  inferred from the adviser's Prague seat and the Czech partners.
  - The ticket quote says only "sweet spot" (EUR 0.5-2M), not "cheque". The
  capital figure (EUR 47M) comes from an undated news item.
  - The 2026 Theorema deal was not used, because only an aggregator ties i&i to
  it.

⏺ Agent "Extract i-and-i-biotech" finished · 1m 42s

⏺ Round 1 is done. Gi21 Capital (3 deals in the window, page injection ignored
  again) and i&i Biotech (2 deals) both validated. Logging these and launching
  round 2.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && printf '%s\n'
      "2026-10-12,investor-extractor,sonnet,gi21-capital,38918,21,93.2,ok"
      "2026-10-12,investor-…)
  ⎿  62 remaining
     {
       "candidate_id": "i-and-i-prague",
     … +30 lines (ctrl+o to expand)
  ⎿  Updated data/runs/run_log.csv (+2 -0)
      35  2026-10-12,investor-extractor,sonnet,depo-ventures,36545,19,199
          .0,ok
      36  2026-10-12,investor-extractor,sonnet,founder-institute-prague,2
          6365,8,42.4,ok
      37  2026-10-12,investor-extractor,sonnet,fazole-ventures,33669,15,6
          9.6,ok
      38 +2026-10-12,investor-extractor,sonnet,gi21-capital,38918,21,93.2
         +,ok                                                            
      39 +2026-10-12,investor-extractor,sonnet,i-and-i-biotech,37845,17,1
         +01.8,ok                                                        

⏺ 4 background agents launched (↓ to manage)
   ├ Extract i-and-i-prague
   ├ Extract impulse-ventures
   ├ Extract incomming-ventures
   └ Extract inven-capital

⏺ Round 2 is running: i&i Prague, Impulse Ventures, InCOMMing Ventures and Inven
  Capital. That leaves 58 rows in the queue after this round.

✻ Sautéed for 3m 4s · done Monday 5:59 PM

› Message from investor-extractor
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/incomming-ventures.json. `src.validate` passed.
  - Evidence within the last 24 months: 0. The only deal found is CARZADA,
  announced 2016-05-18 (150sec byline).
  - Left null: website (incomming.net does not resolve), ticket, capital, funds,
  company_website, round, legal_entities.role.
  - The quotes were not run through `check_quotes`. The `altss.com` and
  `finmag.cz` quotes come from WebFetch summaries and may not be verbatim, so
  expect weak or missing matches there.
  - Borderline: likely dormant or defunct. I added a `not_found_or_defunct`
  signal (no live site, no deal after 2016). The entity INCOMMING ventures a.s.,
  IČO 04991087, was matched by name only through the finmag.cz register mirror
  (tier 3). `hq_country` CZ is based on the registered seat. All sources are
  tier 3, and the sector, stage and type values rest on Altss and 150sec. A
  Dealroom result title contained instructions aimed at AI models. I ignored it
  and did not use Dealroom as a source.

⏺ InCOMMing Ventures is done: no deal since 2016 and a defunct signal recorded,
  so it should be excluded at the decide step. Three extractions from this round
  are still running.

✻ Brewed for 1s · done Monday 5:59 PM

⏺ Agent "Extract incomming-ventures" finished · 50s

› Message from investor-extractor
  - Written: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/i-and-i-prague.json (src.validate passed).
  - Evidence within 24 months: 0. No dated deal found, so no newest date. The
  site shows only 11 unnamed, undated portfolio logos.
  - Null fields: type, stages, ticket and capital. funds[] and
  evidence_of_activity are empty. The exclusion_signals array is empty as well.
  - Set: hq_country CZ, from a tier-3 kurzy.cz search-results page (Pobřežní
  394/12, Praha), not a company page. Legal entity i&i Prague, s.r.o., IČO
  06058485, from the same page, so the IČO is unconfirmed in a primary registry.
  Sector health_biotech, from the investor's own site.
  - Borderline: it is an incubator and venture builder. The IOCB page says it
  provides pre-seed financing and co-created the i&i Biotech Fund with EIF in
  2021. I found no verbatim source saying it invests equity itself, so type is
  null. The record may point to an adviser or incubator role, or "no recent
  investment".
  - The kurzy.cz source URL is a search page, so the quote check may be fragile.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-12,investor-extractor,sonnet,incomming-ventures,22508,13,50.5,ok"
      >> data/runs/run_log.csv)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      37  2026-10-12,investor-extractor,sonnet,fazole-ventures,33669,15,6
          9.6,ok
      38  2026-10-12,investor-extractor,sonnet,gi21-capital,38918,21,93.2
          ,ok
      39  2026-10-12,investor-extractor,sonnet,i-and-i-biotech,37845,17,1
          01.8,ok
      40 +2026-10-12,investor-extractor,sonnet,incomming-ventures,22508,1
         +3,50.5,ok                                                      
  ⎿  (another command ran in this repository at the same time; a change 
     made by either may show under either result)

⏺ Agent "Extract i-and-i-prague" finished · 56s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-12,investor-extractor,sonnet,i-and-i-prague,33336,13,56.4,ok" >>
      data/runs/run_log.csv)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      38  2026-10-12,investor-extractor,sonnet,gi21-capital,38918,21,93.2
          ,ok
      39  2026-10-12,investor-extractor,sonnet,i-and-i-biotech,37845,17,1
          01.8,ok
      40  2026-10-12,investor-extractor,sonnet,incomming-ventures,22508,1
          3,50.5,ok
      41 +2026-10-12,investor-extractor,sonnet,i-and-i-prague,33336,13,56
         +.4,ok                                                          
  ⎿  (another command ran in this repository at the same time; a change 
     made by either may show under either result)

› Message from investor-extractor
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/impulse-ventures.json; src.validate passed.
  Evidence items dated within the last 24 months: 0. The only deal is Dataddo,
  announced 2023-12-20 (CzechCrunch), so it is outside the window.
  Fields left null: website, ticket, capital, and funds is empty. All of these
  are not_published. The "up to CZK 4 bn" figure (2020) is available capital,
  not AUM or a fund size.
  Borderline:
  - No 2024-2026 deal found, so the investor is likely dormant on the evidence.
  The 2025-08-05 CzechCrunch article only mentions a 2022 round.
  - The own website is unusable (impulseventures.com has a certificate for
  another host).
  - Legal entity is Impulse Ventures, a.s., IČO 08841471, Praha, taken from the
  tier-3 mesec.cz mirror. hq=CZ is inferred from that Prague seat.
  - Sectors are mapped to generalist because the source says only "technological
  startups in Central Europe".

⏺ Agent "Extract impulse-ventures" finished · 1m 2s

  Ran 1 shell command (ctrl+o to expand)

❯ pause                                                                         

⏺ Pausing. I won't launch any more extractions. The Inven Capital extraction
  already running will finish and write its own record. I'll commit what's there
  now.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && git add -A && git
      commit -qm "data: R3 records i-and-i-prague, impulse-ventures,
      incomming-ventures (pau…)
  ⎿  11
  ⎿  (another command ran in this repository at the same time; a change 
     made by either may show under either result)

⏺ I've paused at step R3 (extraction): 11 of the 70 queued candidates have
  staging records. Everything is committed and pushed. The Inven Capital
  extraction was already running and will finish on its own; I'm not starting
  any others, and the timer that would have started the next 4 just lists rows.

  Two problems changed the plan along the way:

  - Shared search limit. All agents in a Claude Code session share 200 web
    searches, and the budget refills at about 100 per hour. Triage used most of
    it, which hurt both triage and the first extractions. I now cap the
    extractor at 6 searches per candidate and pace rounds to the refill (E-12,
    D-017).
  - First extractor trial had systematic errors. A capital figure was quoted
    without its label, an active fund had only undated evidence, and stages were
    incomplete. I fixed the prompt in its own agents: commit (E-09 to E-11),
    kept the first 4 records in data/records/trial_01/, and the re-run came out
    clean.

  Judgment calls you should check, all written up in docs/decisions.md:

  - Triage re-runs (D-014). I re-ran batches where more than a third had an
    unknown country (01, 04, 05, 07, 09). Re-running didn't help much: batch 01
    got worse. That's logged as E-06, and the first outputs are kept.
  - Triage exclusion rule (D-015). I changed decide.py and its tests so triage
    can exclude a candidate by type only with page evidence and high confidence.
    Before this, Springtide Ventures, KKCG's venture fund, would have been
    dropped as a private holding (E-08).
  - Queue cut (D-016). 158 candidates qualified for extraction; a new script,
    src/select_queue.py, ranks them and keeps 70. The other 88 are listed as not
    processed.

  Of the 11 records, Founder Institute Prague, i&i Prague, Impulse Ventures and
  InCOMMing Ventures have no dated deal in the last 24 months, so code should
  exclude them. The other seven have recent dated deals. Two pages tried to give
  instructions to AI models; the agents ignored them (E-07).

  To continue, tell me to resume. I'll pick up from the 12th row (Inven
  Capital's record will exist by then), and the remaining 59 should take about 3
  hours at the refill rate. Then R4–R8 follow as written.

✻ Baked for 1m 32s · done Monday 6:01 PM

› Message from investor-extractor
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/inven-capital.json. `src.validate` passed.
  Evidence dated in the last 24 months: 2 items. Newest is 2026-09-11 (Wint
  Series D), taken from the article URL because the page prints no date. The
  other is Vytal, 2025-03-12.
  Fields left null: stages (not_published). `funds` is empty.
  Borderline:
  - Both activity quotes are weak. The Wint quote is a short fragment from a
  Spanish-language article, and the `co_lead` role comes from a search-result
  summary, not from the quote. The Vytal quote does not state a role, so it is
  `unknown`.
  - I set `type` to `vc`, not `cvc`. The site footer shows ČEZ, a. s., but I
  found no quote that says the fund is corporate.
  - The IČO 02059533 comes from the Hlídač státu mirror (tier 3). The annual
  report PDF is an unreadable scan, and I did not check or.justice.cz.
  - The 500m EUR in `capital` is the website's fund figure, labelled
  `latest_fund_size`. The ticket quote is "Ticket size 2-30m EUR", rebuilt from
  the page's label and value, so check it in `src.check_quotes`.
  - A possible July 2026 Vytal follow-on is unconfirmed.
⏺ The Inven Capital extraction finished. I'll log it and commit, then stay
  paused. Its record has three problems for the AI-error log:
  - The co_lead role came from a search-result summary, which breaks the rule
    that snippets are never evidence.
  - The ticket quote was assembled from a label and a value rather than copied
    verbatim.
  - The type is vc, although the fund belongs to ČEZ (cvc).

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-12,investor-extractor,sonnet,inven-capital,,,,ok" >>
      data/runs/run_log.csv && cat >> docs/…)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      40  2026-10-12,investor-extractor,sonnet,incomming-ventures,22508,1
          3,50.5,ok
      41  2026-10-12,investor-extractor,sonnet,i-and-i-prague,33336,13,56
          .4,ok
      42  2026-10-12,investor-extractor,sonnet,impulse-ventures,32282,14,
          61.6,ok
      43 +2026-10-12,investor-extractor,sonnet,inven-capital,,,,ok       
  ⎿  Updated docs/ai-errors.md (+1 -0)
      16  | E-10 | 2026-10-12 | investor-extractor (zkušební běh) | depo-
          ventures | `evidence_of_activity` | Obě investice doložené jen 
          nedatovanými příspěvky na webu fondu, takže záznam nemá žádnou 
          datovanou investici a kód by aktivní fond vyřadil jako `no_rece
          nt_investment`. | Orchestrátor (R3). | Prompt: k nejnovějším in
          vesticím hledat datovaný zdroj (tisková zpráva portfoliové firm
          y, média). |
      17  | E-11 | 2026-10-12 | investor-extractor (zkušební běh) | credo
          -ventures | `stages` | Uvedena jen fáze `pre_seed`, ačkoli web 
          uvádí víc fází. | Orchestrátor (R3). | Prompt: uvést všechny fá
          ze, které zdroj jmenuje. |
      18  | E-12 | 2026-10-12 | všichni agenti (infrastruktura) | credo-v
          entures, depo-ventures, triáž batch 07/09 | — | Ne chyba modelu
          : Claude Code má na jednu relaci 200 vyhledávání sdílených všem
          i agenty (doplňuje se ~100/h). Triáž je spotřebovala, extraktor
           pak nedohledal investice z nápovědy. | Text chyby nástroje ve 
          výstupu agenta. | Prompt: max. 6 vyhledávání na kandidáta, nejd
          řív vlastní stránky kandidáta, příznak `SEARCH_BUDGET_EXHAUSTED
          ` v `meta.notes`. Extrakce běží po 4 s odstupem podle doplňován
          í limitu (D-017). |
      19 +| E-13 | 2026-10-12 | investor-extractor | inven-capital | `evi
         +dence_of_activity[0].role`, `ticket`, `type` | Role `co_lead` u
         + investice Wint převzata ze shrnutí výsledku vyhledávání, ne z 
         +citace (porušuje pravidlo „snippet není důkaz“); citace ticketu
         + „Ticket size 2-30m EUR“ je poskládaná z popisku a hodnoty, ne 
         +doslovná; typ `vc`, ačkoli jde o fond skupiny ČEZ (`cvc`), prot
         +ože agent nenašel citaci. | Závěrečná zpráva agenta, kterou čet
         +l orchestrátor. | Zatím nic; zachytí to `check_quotes.py` a ově
         +řovatel. Pokud se vzor zopakuje, upravím prompt. |             

⏺ Agent "Extract inven-capital" finished · 3m 18s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && sed -i ''
      's/^2026-10-12,investor-extractor,sonnet,inven-capital,,,,ok$/2026-10-12,i
      nvestor-extractor,so…)
  ⎿  2026-10-12,investor-extractor,sonnet,inven-capital,34824,16,198.2,ok
  ⎿  Updated data/runs/run_log.csv (+1 -1)
      40  2026-10-12,investor-extractor,sonnet,incomming-ventures,22508,1
          3,50.5,ok
      41  2026-10-12,investor-extractor,sonnet,i-and-i-prague,33336,13,56
          .4,ok
      42  2026-10-12,investor-extractor,sonnet,impulse-ventures,32282,14,
          61.6,ok
      43 -2026-10-12,investor-extractor,sonnet,inven-capital,,,,ok       
      43 +2026-10-12,investor-extractor,sonnet,inven-capital,34824,16,198
         +.2,ok                                                          

⏺ Still paused. The Inven Capital extraction finished, so 12 of the 70 queued
  candidates now have records. Its run is logged, and everything is committed
  and pushed. No other agents are running.

  Inven Capital's record is flawed in three ways, logged as error E-13:
  - Deal role: "co_lead" on the Wint deal came from a search-result summary, not
    from the cited page.
  - Ticket quote: it was put together from a label and a number instead of being
    copied word for word.
  - Type: it's typed as a regular VC fund, although it belongs to ČEZ and should
    be a corporate fund. The agent found no quote saying so.

  The quote check (R5) and the verifier (R6) should catch the first two. If any
  recur in later records, I'll fix the extractor prompt.

  When you say resume, I'll continue from the 13th of the 70 queued candidates;
  the remaining 58 should take about 3 hours at the search-limit pace. Then I'll
  run steps R4–R8.

✻ Worked for 11m 47s · done Monday 6:02 PM

⏺ Background command "Log impulse, pace 4 min, list next rows" completed (exit
code 0)

⏺ The background pacing timer finished; all it did was list the next rows to
  extract. I didn't launch anything. We're still paused at R3, with 12 of the 70
  queued candidates extracted. Say resume when you want me to continue.

✻ Churned for 2s · done Monday 6:04 PM

※ recap: Running the pilot runbook R0–R8 to build the Czech VC investor database. It's paused at extraction (R3) with 12 of 70 candidates done; say "resume" and I'll continue with the remaining 58. (disable recaps in /config)

❯ continue                                                                      

  Ran 1 shell command (ctrl+o to expand)

⏺ Resuming R3 with the next 4 rows.

⏺ 4 background agents launched (↓ to manage)
   ├ Extract j-t-ventures
   ├ Extract jic-ventures
   ├ Extract koopeo-ventures
   └ Extract lighthouse-ventures

⏺ Extraction has resumed with four running in parallel: J&T Ventures, JIC
  Ventures, Koopeo Ventures and Lighthouse Ventures. That leaves 54 of the 70
  after these. I'll keep pacing rounds to the search-budget refill, then move on
  to R4–R8.

✻ Baked for 19s · done Monday 8:06 PM

› Message from investor-extractor
  Written: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/koopeo-ventures.json (src.validate passed).
  Evidence: 1 item within 24 months, newest 2025-07-17 (TRIFFT Loyalty pre-seed,
  participant, Tech.eu, tier 3).
  Null fields: sectors, stages, ticket, capital, funds[] (all not_published; the
  website names no stage, sector or amount). The instrument is "unknown".
  Borderline: the IČO 05269113 (KOOPEO Ventures SE, Brno) comes only from the
  investor's own site, with no registry confirmation found. Quotes for
  hq_country ("Solniční 243/17") and the IČ were taken from WebFetch output and
  may need a check_quotes run. The Deafcom 2022 deal from the hint is unverified
  and not recorded. The portfolio page has no dates.

⏺ Koopeo Ventures is done, with one dated deal in the window (July 2025). Three
  extractions from this round are still running.

✻ Sautéed for 1s · done Monday 8:07 PM

⏺ Agent "Extract koopeo-ventures" finished · 1m 4s

› Message from investor-extractor
  Written: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/j-t-ventures.json. `src.validate` passed (1/1
  valid).
  Evidence: 3 activity items, all within 24 months except AEOS (2024-10-07).
  Newest is Wultra, 2026-06-29. Definic, 2026-06-13, is the only item with lead
  role.
  Left null: `capital` (homepage shows EUR 120M next to "Výše aktiv" but never
  says AUM). `funds` is empty. `exclusion_signals` is empty.
  Borderline:
  - Legal entity is only the SICAV fund vehicle J&T Ventures CG SICAV a.s. (IČO
  08220867), from a tier-3 mirror (podnikatel.cz). No management company or ČNB
  entry confirmed.
  - All three deals and the `type` value come from tier-3 media or
  aggregator-style sources. No dated tier-2 source was found.
  - The Oddin.gg deal from the hint was not confirmed from any fetched page, so
  it is not in the record.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-12,investor-extractor,sonnet,koopeo-ventures,32335,13,64.3,ok" >>
      data/runs/run_log.csv)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      41  2026-10-12,investor-extractor,sonnet,i-and-i-prague,33336,13,56
          .4,ok
      42  2026-10-12,investor-extractor,sonnet,impulse-ventures,32282,14,
          61.6,ok
      43  2026-10-12,investor-extractor,sonnet,inven-capital,34824,16,198
          .2,ok
      44 +2026-10-12,investor-extractor,sonnet,koopeo-ventures,32335,13,6
         +4.3,ok                                                         
  ⎿  (another command ran in this repository at the same time; a change 
     made by either may show under either result)

⏺ Agent "Extract j-t-ventures" finished · 1m 24s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-12,investor-extractor,sonnet,j-t-ventures,33285,15,84.2,ok" >>
      data/runs/run_log.csv)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      42  2026-10-12,investor-extractor,sonnet,impulse-ventures,32282,14,
          61.6,ok
      43  2026-10-12,investor-extractor,sonnet,inven-capital,34824,16,198
          .2,ok
      44  2026-10-12,investor-extractor,sonnet,koopeo-ventures,32335,13,6
          4.3,ok
      45 +2026-10-12,investor-extractor,sonnet,j-t-ventures,33285,15,84.2
         +,ok                                                            
  ⎿  (another command ran in this repository at the same time; a change 
     made by either may show under either result)

⏺ J&T Ventures and Koopeo Ventures are done and logged. J&T has two dated deals
  in the 24-month window, the newest Wultra (June 2026). The extractor left
  capital empty even though the homepage lists EUR 120M as "Výše aktiv" (asset
  value), which is a conservative miss. JIC Ventures and Lighthouse Ventures are
  still running.

✻ Crunched for 8s · done Monday 8:08 PM

› Message from investor-extractor
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/jic-ventures.json. `src.validate` passed (1/1
  valid).
  Evidence: 3 deals, all within 24 months. Newest is Elredo, 2026-10-01 (lead,
  CzechCrunch). The others are FaceUp, 2026-05-19, from JIC's own release, and
  Aiviro, 2025-12-16, from CzechCrunch.
  Left null: no field is null. The ticket has `max` only (EUR 1,000,000,
  "Tickets up to €1M"). The funds entry has close "unknown". Capital is
  `latest_fund_size`, CZK 400m (CTP release, 2026-04-07).
  Borderline: no page links the new fund to a specific legal entity. I recorded
  JIC Ventures 2 a.s. (IČO 24320358, founded 2026-01-05) from the kurzy.cz
  mirror with role "other". The older JIC Ventures s.r.o. (IČO 04156293) and the
  parent agency JIC (IČO 71180478) are named in `meta.notes`. The role-in-deal
  for Elredo (lead) and Aiviro (participant) comes from tier-3 media only.
  I did not use a search snippet saying the typical ticket is about EUR 100k,
  because I never saw it on a fetched page.

⏺ JIC Ventures is done: three dated deals in the window, the newest Elredo on 1
  Oct 2026, and it correctly refused to use a search snippet as evidence.
  Lighthouse Ventures is still running. I'll log JIC once its usage figures
  arrive.

✻ Churned for 1s · done Monday 8:09 PM

⏺ Agent "Extract jic-ventures" finished · 2m 36s

⏺ Agent "Extract inven-capital" finished · 2h 10m 59s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && sed -i ''
      's/^2026-10-12,investor-extractor,sonnet,inven-capital,34824,16,198.2,ok$/
      2026-10-12,investor-…)
  ⎿  ?? data/records/staging/j-t-ventures.json
     ?? data/records/staging/jic-ventures.json
     ?? data/records/staging/koopeo-ventures.json
  ⎿  Updated data/runs/run_log.csv (+2 -1)
      40  2026-10-12,investor-extractor,sonnet,incomming-ventures,22508,1
          3,50.5,ok
      41  2026-10-12,investor-extractor,sonnet,i-and-i-prague,33336,13,56
          .4,ok
      42  2026-10-12,investor-extractor,sonnet,impulse-ventures,32282,14,
          61.6,ok
      43 -2026-10-12,investor-extractor,sonnet,inven-capital,34824,16,198
         -.2,ok                                                          
      43 +2026-10-12,investor-extractor,sonnet,inven-capital,36828,16,198
         +.2,ok                                                          
      44  2026-10-12,investor-extractor,sonnet,koopeo-ventures,32335,13,6
          4.3,ok
      45  2026-10-12,investor-extractor,sonnet,j-t-ventures,33285,15,84.2
          ,ok
      46 +2026-10-12,investor-extractor,sonnet,jic-ventures,50672,31,155.
         +6,ok                                                           

⏺ Agent "Extract depo-ventures (trial 2)" finished · 2h 18m 55s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && sed -i ''
      's/^2026-10-12,investor-extractor,sonnet,depo-ventures,36545,19,199.0,ok$/
      2026-10-12,investor-…)
  ⎿  2026-10-12,investor-extractor,sonnet,depo-ventures,33926,22,195.5,reru
     n
     2026-10-12,investor-extractor,sonnet,depo-ventures,38326,19,199.0,ok
     … +25 lines (ctrl+o to expand)
  ⎿  Updated data/runs/run_log.csv (+1 -1)
      32  2026-10-12,investor-extractor,sonnet,credo-ventures,33897,17,62
          .6,ok
      33  2026-10-12,investor-extractor,sonnet,czech-founders-vc,32256,13
          ,64.9,ok
      34  2026-10-12,investor-extractor,sonnet,aspire11,32604,14,73.1,ok
      35 -2026-10-12,investor-extractor,sonnet,depo-ventures,36545,19,199
         -.0,ok                                                          
      35 +2026-10-12,investor-extractor,sonnet,depo-ventures,38326,19,199
         +.0,ok                                                          
      36  2026-10-12,investor-extractor,sonnet,founder-institute-prague,2
          6365,8,42.4,ok
      37  2026-10-12,investor-extractor,sonnet,fazole-ventures,33669,15,6
          9.6,ok
      38  2026-10-12,investor-extractor,sonnet,gi21-capital,38918,21,93.2
          ,ok
  ⎿  (timeout 3m 20s)
› Message from investor-extractor
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/lighthouse-ventures.json and src.validate passed.
  Evidence items in the last 24 months: 1 (Hermetiq pre-seed, newest date
  2026-08-31, listing date on lhv.vc/news-and-events). The second item, Outfindo
  (2025-01-20, third-party page), is older than 24 months.
  Fields left null: capital (not_published) and funds (empty). Fund II was
  launched in 2024, but no size is published.
  Borderline: the Hermetiq post is itself undated, so I cited the dated news
  listing page. The Merchantee (Jun 2026), BeatPulse Labs, Prodeen and Deplace
  AI deals appear only on PitchBook and Caplight, so I did not use them. The
  legal-entity quote on the kurzy.cz page shows the company name only, not the
  IČO (07500912); lhv.vc/about-us also prints that IČO.

⏺ Agent "Extract lighthouse-ventures" finished · 3m 25s

⏺ Lighthouse finished—it mislabels Outfindo (Jan 2025) as "older than 24 months"
  in its summary text, but this is harmless since the actual window calculation
  uses the correct dates. I'll log this and launch the next 4 tasks.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo "2026-10-12,
      investor-extractor,sonnet,lighthouse-ventures,39729,20,205.1,ok" >>
      data/runs/run_log.c…)
  ⎿  {
       "candidate_id": "nation1",
       "name": "N1 Ventures (formerly Nation 1)",
     … +9 lines (ctrl+o to expand)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      44  2026-10-12,investor-extractor,sonnet,koopeo-ventures,32335,13,6
          4.3,ok
      45  2026-10-12,investor-extractor,sonnet,j-t-ventures,33285,15,84.2
          ,ok
      46  2026-10-12,investor-extractor,sonnet,jic-ventures,50672,31,155.
          6,ok
      47 +2026-10-12,investor-extractor,sonnet,lighthouse-ventures,39729,
         +20,205.1,ok                                                    

⏺ 4 background agents launched (↓ to manage)
   ├ Extract longevitytech-fund
   ├ Extract look-ai-ventures
   ├ Extract miton
   └ Extract nation1

⏺ The next four extractions are running: Longevitytech.fund, Look AI Ventures,
  Miton and N1 Ventures. After them, 50 of the 70 queued candidates remain.

✻ Churned for 2m 32s · done Monday 8:12 PM

› Message from investor-extractor
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/nation1.json and src.validate passed.
  Evidence dated in the last 24 months: 1 item (Flick seed, Lupa.cz,
  2026-05-15), which is also the newest date.
  Fields left null or empty: stages, ticket, legal_entities (empty list), funds
  (empty list).
  Borderline:
  - The team is split across SF, Prague and Luxembourg. hq_country=CZ rests on a
  tier-3 Lupa quote ("Český investiční fond N1 Ventures").
  - The only registered legal entities found are Luxembourg GPs, with no
  registry numbers. No Czech IČO was found.
  - The Human Archive seed article names Wing, NVP and YC but not N1, so I did
  not record it.
  - Myriad AI appeared only in search snippets, so I did not record it.

⏺ N1 Ventures is done, with one dated deal in the window (Flick, May 2026). The
  extractor also caught that the hint's Human Archive deal doesn't name N1 and
  left it out. Three extractions are still running.

✻ Cogitated for 1s · done Monday 8:13 PM

⏺ Agent "Extract nation1" finished · 1m 7s

› Message from investor-extractor
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/miton.json. `src.validate` passed.
  Evidence dated within 24 months: 1 item. It is the Ace padel app 50% stake,
  CzechCrunch (cc.cz), 2026-10-01. Role is `unknown`.
  Left `null`: capital (`not_published`; the homepage's EUR 450M is portfolio
  value, not AUM) and `funds` (empty). I found no dated non-aggregator source
  for Whisper, Bandits or DeepScout. Their only dates were the undated miton.cz
  portfolio page and PitchBook, so they are not recorded.
  Borderline:
  - Type is a judgment call. Miton says "VC, ale ne tak úplně" and invests its
  own money, so I set `vc`; `private_holding` is possible.
  - The legal entity MITON CZ, s.r.o. (IČO 25417967) comes from a finmag.cz
  mirror (tier 3), not confirmed in or.justice.cz. Miton has other vehicles
  (e.g. MITON C a.s.) that I did not record.
  - The `hq_country` address quote and the ticket quote ("300k-2M €" plus the
  label sentence on the next line) came from WebFetch summaries, so run
  `check_quotes` on them.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-12,investor-extractor,sonnet,nation1,33287,15,67.1,ok" >>
      data/runs/run_log.csv)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      45  2026-10-12,investor-extractor,sonnet,j-t-ventures,33285,15,84.2
          ,ok
      46  2026-10-12,investor-extractor,sonnet,jic-ventures,50672,31,155.
          6,ok
      47  2026-10-12,investor-extractor,sonnet,lighthouse-ventures,39729,
          20,205.1,ok
      48 +2026-10-12,investor-extractor,sonnet,nation1,33287,15,67.1,ok  

⏺ Agent "Extract miton" finished · 1m 16s

› Message from investor-extractor
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/look-ai-ventures.json. `src.validate` passed (1/1
  valid).
  Evidence items dated within the last 24 months: 3 (Sodex 2026-07-13, Lucida AI
  2026-06-30, Digicust 2025-12-03). Newest is 2026-07-13.
  Fields left null: capital (not_published). Ticket and fund size come only from
  a 2023 launch article (tier 3, targets: EUR 250k per startup, EUR 20M fund).
  The fund vintage is also null.
  Borderline:
  - Stages are mapped from "pre-Series A" to seed, which is my judgment call.
  - The Embodied AI (Sep 2026) deal is not in the record. No fetched source
  confirmed it.
  - Registry: the IČO 17604087 entry on or.justice.cz is cited with only the
  company name as the quote, so check_quotes may flag it.
  - Management company FTP Dimension is cited from the website; its IČO was not
  checked in a registry.

⏺ Agent "Extract look-ai-ventures" finished · 1m 18s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && printf '%s\n'
      "2026-10-12,investor-extractor,sonnet,miton,36088,17,76.2,ok"
      "2026-10-12,investor-extract…)
  ⎿  50 remaining
     {
       "candidate_id": "novira-capital",
     … +24 lines (ctrl+o to expand)
  ⎿  Updated data/runs/run_log.csv (+2 -0)
      46  2026-10-12,investor-extractor,sonnet,jic-ventures,50672,31,155.
          6,ok
      47  2026-10-12,investor-extractor,sonnet,lighthouse-ventures,39729,
          20,205.1,ok
      48  2026-10-12,investor-extractor,sonnet,nation1,33287,15,67.1,ok
      49 +2026-10-12,investor-extractor,sonnet,miton,36088,17,76.2,ok    
      50 +2026-10-12,investor-extractor,sonnet,look-ai-ventures,36649,18,
         +78.0,ok                                                        
  ⎿  (timeout 3m 20s)

› Message from investor-extractor
  Written: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/longevitytech-fund.json. src.validate passed.
  Evidence dated in the last 24 months: 1 (Klothea Bio seed, lead, 2024-11-25,
  from a BioSpace press release). The second item is Occuity (2021-09-27), which
  is older than 24 months.
  Null fields: website, hq_country (conflicting_sources), type, sectors, ticket,
  capital, and legal_entities and funds (empty lists).
  Borderline:
  - The team is probably US-based (Palo Alto, Miami and Boca Raton appear in
  secondary sources). A 2022 Czech article says the fund was Czech and the next
  one would be American, so this may end up out_of_scope_geography.
  - longevitytech.fund returned unrelated content, so there is no own site.
  - No registry entry was found.
  - PitchBook shows deals in 2025 and 2026, but I did not use them as evidence.
  - A newer dated source could change the activity result.

⏺ Agent "Extract longevitytech-fund" finished · 1m 22s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-12,investor-extractor,sonnet,longevitytech-fund,31237,13,81.8,ok"
      >> data/runs/run_log.csv…)
  ⎿  {
       "candidate_id": "presto-ventures",
       "name": "Presto Tech Horizons (Tech Horizons)",
     … +9 lines (ctrl+o to expand)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      48  2026-10-12,investor-extractor,sonnet,nation1,33287,15,67.1,ok
      49  2026-10-12,investor-extractor,sonnet,miton,36088,17,76.2,ok
      50  2026-10-12,investor-extractor,sonnet,look-ai-ventures,36649,18,
          78.0,ok
      51 +2026-10-12,investor-extractor,sonnet,longevitytech-fund,31237,1
         +3,81.8,ok                                                      

⏺ 4 background agents launched (↓ to manage)
   ├ Extract novira-capital
   ├ Extract orbit-capital
   ├ Extract patero
   └ Extract presto-ventures

⏺ The next four extractions are running: Novira Capital, Orbit Capital, Patero
  and Presto Tech Horizons. Once they finish, 46 of the 70 will remain.

  Longevitytech.fund's record leaves the country empty because sources conflict,
  and the team may now be US-based. Code will decide whether it's in scope.

✻ Cogitated for 1m 57s · done Monday 8:15 PM

› Message from investor-extractor
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/novira-capital.json. `src.validate` passed.
  Evidence dated within 24 months: 0. The only activity item is Smartlook
  (CzechCrunch, 2023-09-12), which is about 25 months old.
  Null fields: hq_country (conflicting_sources), legal_entities (empty, no IČO
  found), sectors, stages, ticket and capital (all not_published). The Smartlook
  announced_date is also null.
  Borderline:
  - novira.cz redirects to novira.com, a Zürich/Zug and Brno property group. It
  says "We are not a VC", with about 70% of capital in real estate and the rest
  in startups, loans and other investments.
  - I typed it `private_holding` and added a `real_estate_only` signal, which is
  partial because it also holds startups.
  - Smartlook was exited to Cisco in 2023 and no later deal was found.
  - Identifying the CzechCrunch "Novira Capital" with novira.com is my
  inference, because the site lists Smartlook among its startups.
  - The CzechCrunch quote came through WebFetch, so it may not be verbatim.

⏺ Novira Capital is done. It's a Brno/Zug property group that says "We are not a
  VC", with no deal since 2023, so code will exclude it. The extractor added a
  real_estate_only signal even though the group also holds startups. That signal
  is inaccurate, but it doesn't change the outcome; the verifier should flag
  it. Three extractions are still running.

✻ Baked for 3s · done Monday 8:16 PM

⏺ Agent "Extract novira-capital" finished · 1m 14s

› Message from investor-extractor
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/patero.json. src.validate passed.
  - Evidence dated within the last 24 months: 2 (Flowlance 2024-11-28, Flowpay
  2024-03-20, both CzechCrunch). The newest is 2024-11-28.
  - Null fields: type, sectors, stages, ticket, capital (all not_published).
  funds is empty. The legal entity's registry_id is an empty string because the
  schema requires a string.
  - Borderline: Patero s.r.o. (Praha 6) looks like a startup-building holding or
  co-investor, not a declared VC fund. Its site says "15+ startupů" and "3
  exity".
  - The IČO 03928446 appeared only in a search snippet of a notarial deed; the
  registry page returned 403. It was not recorded.
  - The Outfindo and Carebot involvement was not confirmed on any fetched page.
  The Flowpay item is a CzechCrunch "Kdo investuje" list, with no role or
  instrument stated.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-12,investor-extractor,sonnet,novira-capital,27538,16,74.3,ok" >>
      data/runs/run_log.csv)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      49  2026-10-12,investor-extractor,sonnet,miton,36088,17,76.2,ok
      50  2026-10-12,investor-extractor,sonnet,look-ai-ventures,36649,18,
          78.0,ok
      51  2026-10-12,investor-extractor,sonnet,longevitytech-fund,31237,1
          3,81.8,ok
      52 +2026-10-12,investor-extractor,sonnet,novira-capital,27538,16,74
         +.3,ok                                                          

⏺ Agent "Extract patero" finished · 1m 17s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-12,investor-extractor,sonnet,patero,26320,17,77.4,ok" >>
      data/runs/run_log.csv)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      50  2026-10-12,investor-extractor,sonnet,look-ai-ventures,36649,18,
          78.0,ok
      51  2026-10-12,investor-extractor,sonnet,longevitytech-fund,31237,1
          3,81.8,ok
      52  2026-10-12,investor-extractor,sonnet,novira-capital,27538,16,74
          .3,ok
      53 +2026-10-12,investor-extractor,sonnet,patero,26320,17,77.4,ok   

⏺ Novira Capital and Patero are done and logged. Orbit Capital and Presto Tech
  Horizons are still running.

  Patero's newest dated deal is from November 2024, inside the 24-month window.
  The extractor also counted a March 2024 deal as recent, but it falls before
  the window start; code applies the window anyway, so the record is unaffected.
  Patero's type is left empty: it looks like a holding that builds startups
  rather than a declared VC fund.

✻ Worked for 8s · done Monday 8:17 PM

› Message from investor-extractor
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/orbit-capital.json, and src.validate passed.
  - Evidence: 1 activity item (IAG, 2026-06-02, CzechCrunch via cc.cz), which is
  the newest date and within 24 months. Fund II (EUR 107m, 2026-07-02, Tech.eu)
  is recorded in funds and capital.
  - Null: ticket (not_published; only the EUR 3-15m debt-fund ticket is
  published). Sector (software_saas) and stage (growth) are weak mappings from
  generic wording. Capital is latest_fund_size only.
  - Borderline: Orbit is mainly growth debt (Fund II). I added a debt_only
  exclusion signal. The IAG round combined equity and venture debt, and Orbit's
  role and instrument are unknown. The Sloneek deal (Jun 2026) was left out
  because no dated source was fetched. No Orbit growth equity fund was
  confirmed.
  - Weaker sourcing: orbitcapital.com is nearly empty and its subpages 404. The
  legal entity is the fund vehicle Conseq-Orbit SICAV (IČO 08223467, Praha 1)
  via a tier-3 mirror, and its quote is the former name only. The Prague 4
  management company was not found. hq=CZ rests on a "Czech-Polish" description,
  and a Warsaw office is also reported.
⏺ Orbit Capital is done. It's mainly a growth-debt investor; the extractor
  flagged it as debt-only and found one dated deal in the window, which mixed
  equity and debt. Code and the verifier will decide whether it's in. Presto
  Tech Horizons is still running; I'll log Orbit when its usage arrives.

✻ Churned for 2s · done Monday 8:17 PM

⏺ Agent "Extract orbit-capital" finished · 1m 25s

› Message from investor-extractor
  Written: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/presto-ventures.json (src.validate passed).
  Evidence dated within 24 months: 3 (Occam pre-seed lead 2026-02-11,
  CzechCrunch; Tur.ai 2024-10-25, Tech.eu; Bavovna 2024-10-23, AIN). Newest:
  2026-02-11. The Oct 2024 items are about 24 months old, so they may fall
  outside the window depending on config.
  Null fields: sectors (no verbatim sector statement captured) and capital (no
  AUM published). Both use not_published.
  Borderline: the registry entity is Presto Ventures II a.s. (IČO 11678704, from
  a podnikatel.cz mirror and the site footer), not the Tech Horizons vehicle.
  The ticket "€500k to €5M" is the site's wording and may not be strictly a
  first cheque. The fund size of EUR 150M is a target taken from Tech.eu.
  Founder Rubeš was detained in March 2026; the firm says cooperation ended in
  Sept 2025. I recorded no exclusion signal for this.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-12,investor-extractor,sonnet,orbit-capital,36760,18,84.9,ok" >>
      data/runs/run_log.csv && g…)
  ⎿  46 remaining
     {
       "candidate_id": "purple-ventures",
     … +30 lines (ctrl+o to expand)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      51  2026-10-12,investor-extractor,sonnet,longevitytech-fund,31237,1
          3,81.8,ok
      52  2026-10-12,investor-extractor,sonnet,novira-capital,27538,16,74
          .3,ok
      53  2026-10-12,investor-extractor,sonnet,patero,26320,17,77.4,ok
      54 +2026-10-12,investor-extractor,sonnet,orbit-capital,36760,18,84.
         +9,ok                                                           
  ⎿  (timeout 3m 20s)

⏺ Agent "Extract presto-ventures" finished · 1m 37s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-12,investor-extractor,sonnet,presto-ventures,39533,20,97.1,ok" >>
      data/runs/run_log.csv)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      52  2026-10-12,investor-extractor,sonnet,novira-capital,27538,16,74
          .3,ok
      53  2026-10-12,investor-extractor,sonnet,patero,26320,17,77.4,ok
      54  2026-10-12,investor-extractor,sonnet,orbit-capital,36760,18,84.
          9,ok
      55 +2026-10-12,investor-extractor,sonnet,presto-ventures,39533,20,9
         +7.1,ok                                                         

⏺ 4 background agents launched (↓ to manage)
   ├ Extract purple-ventures
   ├ Extract purposetech
   ├ Extract reflex-capital
   └ Extract rockaway-ventures

⏺ Presto Tech Horizons is logged. The next four extractions are running: Purple
  Ventures, PurposeTech, Reflex Capital and Rockaway Ventures. After them, 42 of
  the 70 remain.

✻ Sautéed for 2m 1s · done Monday 8:19 PM

› Message from investor-extractor
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/reflex-capital.json; src.validate passed (1/1
  valid).
  Evidence: 3 items, 2 dated within 24 months (Merchantee 2026-06-09, Choice
  2026-03-16), plus Boataround 2024-06-10. The newest date is 2026-06-09.
  Null fields: sectors, stages, ticket, capital (all not_published); funds is
  []. The homepage shows only "€150M invested", which is deployed capital, so I
  did not use it as AUM.
  Borderline:
  - Every source is tier 3 (IČO 24269158 from a mesec.cz mirror; deals from
  raising.fi and tech.eu).
  - Merchantee date conflict: raising.fi says 2026-06-09 and nordic9 says
  2026-06-03. I used 06-09 and noted the conflict.
  - Merchantee role is lead and Choice is participant.
  - The team has offices in Prague and San Francisco, and I set hq_country to CZ
  from the Prague address only. I did not check a team page.
  - The hint's Grid.online deal is not verified.
  - The vc type rests on a media sentence ("Czech fund Reflex Capital invested
  €5.5m in boat charter company Boataround"), not on the investor's own site.

⏺ Reflex Capital is done: 2 dated deals in the window, the newest Merchantee in
  June 2026, all from third-party sources. Three extractions from this round are
  still running.

✻ Brewed for 1s · done Monday 8:20 PM

⏺ Agent "Extract reflex-capital" finished · 1m 2s

› Message from investor-extractor
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/purposetech.json. `src.validate` passed (1/1
  valid).
  Evidence items within 24 months: 1 (Auryx pre-seed, 2026-04-30, PurposeTech a
  participant, Celero Ventures led). Newest date: 2026-04-30.
  Fields left null: ticket (not_published), capital (not_published),
  legal_entities (empty).
  For legal_entities, the site names PurposeTech, s.r.o., but I couldn't find
  its IČO in a registry.
  For ticket, the website FAQ is placeholder text. cc.cz gives only total
  support per company (about EUR 0.5-1m) for the planned second fund, not a
  first cheque.
  Borderline: the only fund recorded is PT Capital (second fund, EUR 10m target,
  from CzechCrunch, 2026-02-10). The Vestbee EUR 2.3m first-fund figure was not
  on the fetched page. Other deals (Tingit Feb 2026, Lifeyear Jul 2025) were
  seen only on aggregators, so I didn't cite them. The Auryx source is a
  Cambridge Enterprise page. Its quote is a partial sentence, which the quote
  check may flag as weak. I could not confirm "Purpose Ventures" as related.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-12,investor-extractor,sonnet,reflex-capital,33373,18,61.7,ok" >>
      data/runs/run_log.csv)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      53  2026-10-12,investor-extractor,sonnet,patero,26320,17,77.4,ok
      54  2026-10-12,investor-extractor,sonnet,orbit-capital,36760,18,84.
          9,ok
      55  2026-10-12,investor-extractor,sonnet,presto-ventures,39533,20,9
          7.1,ok
      56 +2026-10-12,investor-extractor,sonnet,reflex-capital,33373,18,61
         +.7,ok                                                          
  ⎿  (another command ran in this repository at the same time; a change 
     made by either may show under either result)

⏺ Agent "Extract purposetech" finished · 1m 32s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-12,investor-extractor,sonnet,purposetech,32085,20,92.2,ok" >>
      data/runs/run_log.csv)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      54  2026-10-12,investor-extractor,sonnet,orbit-capital,36760,18,84.
          9,ok
      55  2026-10-12,investor-extractor,sonnet,presto-ventures,39533,20,9
          7.1,ok
      56  2026-10-12,investor-extractor,sonnet,reflex-capital,33373,18,61
          .7,ok
      57 +2026-10-12,investor-extractor,sonnet,purposetech,32085,20,92.2,
         +ok                                                             
  ⎿  (another command ran in this repository at the same time; a change 
     made by either may show under either result)

⏺ Reflex Capital and PurposeTech are done and logged. PurposeTech has one dated
  deal in the window: Auryx, April 2026, where it participated. Purple Ventures
  and Rockaway Ventures are still running.

✻ Churned for 6s · done Monday 8:20 PM

› Message from investor-extractor
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/rockaway-ventures.json. src.validate passed.
  Evidence: 2 activity items, both within 24 months, newest 2025-10-23 (Vermeer
  Series A, participant, Vestbee). The other is Filuta AI seed, lead,
  2025-06-24, on the investor's own news page.
  Fields left null: ticket, capital (both not_published), funds[] empty (no fund
  size published). legal_entities[0].role is also null.
  Borderline: the IČO 06387136 comes only from a mesec.cz mirror (tier 3). The
  site names "Rockaway Ventures Fund" and I could not confirm that the a.s. is
  the fund vehicle. HQ CZ rests on the contact-page address (Praha 6), where the
  block is labelled Rockaway Capital. I found no deal later than Oct 2025 and
  no exclusion signals.

⏺ Rockaway Ventures is done: 2 dated deals in the window, the newest Vermeer
  (October 2025). Purple Ventures is the last one running in this round. I'll
  log Rockaway when its usage figures arrive.

✻ Sautéed for 2s · done Monday 8:22 PM

⏺ Agent "Extract rockaway-ventures" finished · 3m 19s

› Message from investor-extractor
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/purple-ventures.json. src.validate passed (1/1
  valid).
  Evidence dated within 24 months: 1 (Fether Labs, Euro.cz, 2026-05-27). The
  Fund II source (tech.eu, 2024-06-27) is a fund item, not a deal.
  Nulls: sectors (null, not_published, wording kept in raw), capital
  (not_published). The ticket is EUR 250-400k from the investor's site.
  Borderline: the hint deals Flae Robotics (Oct 2026) and Delta Green (Oct 2025)
  are not recorded. Flae appears nowhere on the site or in search. Delta Green
  is dated only on aggregators; funding.tech.eu shows a May 2024 round with no
  exact date. The Fether Labs round stage is null and the role is participant
  (11M CZK alongside Chapter One and a16z Scout). The registry entry is a tier-3
  kurzy.cz mirror with a name-only quote. HQ CZ is inferred from the Brno
  footer address. The Fund II EUR 40M figure is the 2024 launch announcement,
  with close "unknown".

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-12,investor-extractor,sonnet,rockaway-ventures,36417,19,198.9,ok"
      >> data/runs/run_log.csv)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      55  2026-10-12,investor-extractor,sonnet,presto-ventures,39533,20,9
          7.1,ok
      56  2026-10-12,investor-extractor,sonnet,reflex-capital,33373,18,61
          .7,ok
      57  2026-10-12,investor-extractor,sonnet,purposetech,32085,20,92.2,
          ok
      58 +2026-10-12,investor-extractor,sonnet,rockaway-ventures,36417,19
         +,198.9,ok                                                      

⏺ Agent "Extract purple-ventures" finished · 3m 28s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-12,investor-extractor,sonnet,purple-ventures,38499,18,208.5,ok"
      >> data/runs/run_log.csv &…)
  ⎿  42 remaining
     {
       "candidate_id": "rockawayx",
     … +30 lines (ctrl+o to expand)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      56  2026-10-12,investor-extractor,sonnet,reflex-capital,33373,18,61
          .7,ok
      57  2026-10-12,investor-extractor,sonnet,purposetech,32085,20,92.2,
          ok
      58  2026-10-12,investor-extractor,sonnet,rockaway-ventures,36417,19
          ,198.9,ok
      59 +2026-10-12,investor-extractor,sonnet,purple-ventures,38499,18,2
         +08.5,ok                                                        
  ⎿  (timeout 2m 30s)

⏺ These two entries point to the same programme and URL, so I'll extract only
  seed-starter and log the duplicate as a decision instead of re-extracting it,
  leaving aliases.csv untouched since it's human-curated.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && head -3
      data/candidates/aliases.csv && cat >> docs/decisions.md <<'EOF'…)
  ⎿  alias_id,canonical_id,reason
     n1-ventures,nation1,"N1 / Nation 1 is one brand (nation1.vc, n1.rocks)
     "
     nation-1-vc,nation1,"same brand, scout_programmes id"
  ⎿  Updated docs/decisions.md (+4 -0)
      67  ## D-017 · 2026-10-12 · Extrakce v tempu limitu vyhledávání; zk
          ušební záznamy archivované
      68  - Alternativy: pustit všech 66 hned (extraktory by běžely bez v
          yhledávání a vyřadily by aktivní fondy pro chybějící datovaný d
          ůkaz); zkrátit frontu.
      69  - Proč: limit 200 vyhledávání na relaci se doplňuje ~100/h. Při
           ≤ 6 vyhledáváních na kandidáta pouštím 4 extraktory zhruba kaž
          dých 15 minut. Záznam s příznakem `SEARCH_BUDGET_EXHAUSTED` po 
          dokončení fronty extrahuji znovu. Čtyři zkušební záznamy podle 
          runbooku nepoužívám; místo smazání jsou v `data/records/trial_0
          1/` jako doklad iterace promptu.
      70 +                                                               
      71 +## D-018 · 2026-10-12 · `seed-starter-ceske-sporitelny` neextra
         +huji, je to duplicita `seed-starter`                           
      72 +- Alternativy: extrahovat oba (dva záznamy o tomtéž programu, d
         +vojí náklad); doplnit alias a znovu sloučit kandidáty (mění sez
         +nam kandidátů uprostřed pilotu).                               
      73 +- Proč: oba řádky mají stejný web (seedstarter.cz) a popisují t
         +entýž program České spořitelny; na shodu upozornila i triáž (ba
         +tch 07). Extrahuji jen `seed-starter`. `aliases.csv` je ruční s
         +eznam, proto alias nepřidávám sám: navrhuji ho Davidovi k dopln
         +ění. Do té doby zůstane `seed-starter-ceske-sporitelny` v `cz_v
         +c_decisions.csv` jako `pending`.                               

⏺ 3 background agents launched (↓ to manage)
   ├ Extract rockawayx
   ├ Extract seed-starter
   └ Extract soulmates-ventures

⏺ I'll make the helper always skip the duplicate, then start the 4th agent for
  this round.

  Ran 1 shell command (ctrl+o to expand)
⏺ investor-extractor(Extract spinoffy)
  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)

⏺ Four extractions are running: RockawayX, Seed Starter, Soulmates Ventures and
  Spinoffy. The second Seed Starter row is the same programme (same website), so
  I'm not extracting it separately. That decision is recorded in
  docs/decisions.md (D-018). I left aliases.csv alone because it's your
  hand-curated file; adding the alias there is your call.

✻ Crunched for 1m 38s · done Monday 8:24 PM

› Message from investor-extractor
  Written: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/spinoffy.json. src.validate passed.
  Evidence items within 24 months: 0 activity items. The four sourced fields
  (hq, type, stages, all from Lupa 2026-03-02) are dated 2026-03-02, which is
  the newest date.
  Null: website, legal_entities, sectors, ticket, capital, funds,
  evidence_of_activity (no entity or IČO published, no portfolio deal found).
  Borderline: newly launched fund with no deals yet and no website of its own.
  hq_country CZ rests on "V Česku ohlásil svůj start..." (launch in Czechia),
  not an explicit statement of team location. Single tier-3 source. Fund
  structured via J&T Banka and Amista; I did not verify Amista's role. I used 2
  searches and 2 fetches.

⏺ Spinoffy is done: a fund launched in March 2026 with no deals yet and no
  recorded fund close. Code will therefore treat it as having no recent
  investment, a borderline case for your manual review. Three extractions are
  still running.

✻ Churned for 2s · done Monday 8:25 PM

⏺ Agent "Extract spinoffy" finished · 40s

› Message from investor-extractor
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/rockawayx.json, and src.validate passed.
  - 2 evidence items are dated within 24 months. They are OnRe (2026-05-05,
  co-lead, Series A, Edgen article) and BetHog (2026-04-22, from the date shown
  on the rockawayx.com insights listing). The newest is 2026-05-05.
  - Null fields: hq_country (offices in London, Prague and Dubai, no single team
  location), stages, ticket, capital, funds (empty). The site's "$2B+ Assets"
  figure isn't labelled AUM.
  - Borderline:
    - Czech base is unproven. The only Czech legal entity found is Blockad
  s.r.o., IČO 08006458, from the kurzy.cz mirror.
    - It is a crypto/DeFi investor. The sector is mapped to "other", and it also
  runs liquid funds and vault curation.
    - The BetHog post is undated on its own page and its role is recorded as
  unknown, though the post says RockawayX is co-leading. The OnRe post on
  rockawayx.com is also undated, so a third-party article is cited instead.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-12,investor-extractor,sonnet,spinoffy,20959,8,40.7,ok" >>
      data/runs/run_log.csv)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      57  2026-10-12,investor-extractor,sonnet,purposetech,32085,20,92.2,
          ok
      58  2026-10-12,investor-extractor,sonnet,rockaway-ventures,36417,19
          ,198.9,ok
      59  2026-10-12,investor-extractor,sonnet,purple-ventures,38499,18,2
          08.5,ok
      60 +2026-10-12,investor-extractor,sonnet,spinoffy,20959,8,40.7,ok  

⏺ Agent "Extract rockawayx" finished · 1m 13s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-12,investor-extractor,sonnet,rockawayx,28961,16,72.7,ok" >>
      data/runs/run_log.csv)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      58  2026-10-12,investor-extractor,sonnet,rockaway-ventures,36417,19
          ,198.9,ok
      59  2026-10-12,investor-extractor,sonnet,purple-ventures,38499,18,2
          08.5,ok
      60  2026-10-12,investor-extractor,sonnet,spinoffy,20959,8,40.7,ok
      61 +2026-10-12,investor-extractor,sonnet,rockawayx,28961,16,72.7,ok

› Message from investor-extractor
  Written: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/seed-starter.json (src.validate passed).
  Evidence: 3 dated items, all within 24 months (Definic 2026-06-12, Repsense
  2025-12-17, Vestberry 2025-03-17); newest 2026-06-12.
  Null: capital (not_published); funds is an empty list.
  Borderline: CVC of Česká spořitelna (ČS Seed Starter a.s., IČO 61058769,
  Prague team, registry source ARES). Seed Starter was only a participant in the
  Definic and Repsense rounds. The cc.cz quotes came from WebFetch output
  rather than the raw page, so check_quotes should confirm them. The ARES quote
  is just the company name. I did not verify the hint's JIC Ventures LP claim.
  Sector "fintech" is inferred from "banking" wording.

⏺ Agent "Extract seed-starter" finished · 1m 18s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-12,investor-extractor,sonnet,seed-starter,35504,16,78.1,ok" >>
      data/runs/run_log.csv && gi…)
  ⎿  37 remaining
     {
       "candidate_id": "startguide-vc",
     … +22 lines (ctrl+o to expand)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      59  2026-10-12,investor-extractor,sonnet,purple-ventures,38499,18,2
          08.5,ok
      60  2026-10-12,investor-extractor,sonnet,spinoffy,20959,8,40.7,ok
      61  2026-10-12,investor-extractor,sonnet,rockawayx,28961,16,72.7,ok
      62 +2026-10-12,investor-extractor,sonnet,seed-starter,35504,16,78.1
         +,ok                                                            
  ⎿  (another command ran in this repository at the same time; a change 
     made by either may show under either result)
  ⎿  (timeout 2m)

⏺ 3 background agents launched (↓ to manage)
   ├ Extract startguide-vc
   ├ Extract startupyard
   └ Extract tachles

⏺ Four extractions are running: Soulmates Ventures, Startguide VC, StartupYard
  and Tachles VC. RockawayX, Seed Starter and Spinoffy are done and committed.
  About 34 rows remain after this batch.

✻ Worked for 1m 8s · done Monday 8:26 PM

› Message from investor-extractor
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/startguide-vc.json, and src.validate passed.
  - 0 evidence items are dated within the last 24 months. The newest (and only)
  deal is Carebot, 2024-03-22 (CzechCrunch), so this investor is probably
  dormant.
  - Null fields: capital (not_published). The SGOne vintage is null.
  - Borderline: no recent deal could be verified. A 2026 Carebot round exists,
  but I didn't verify that Startguide took part in it. The IČO 28418425 comes
  from the investor's own imprint. The registry mirror (podnikatel.cz) shows it
  only as a shareholder of START GUIDE ONE, a.s. (IČO 17323126), so it is not
  confirmed directly in the register. The ticket (about EUR 100k) and the fund
  (SGOne, EUR 6M target) come from an undated SGOne page, and SGOne's investment
  period ended in 2023.

⏺ Startguide VC is done: its only deal is Carebot from March 2024, so it's
  probably dormant, and the decide step will rule on that. Soulmates Ventures,
  StartupYard and Tachles VC are still running.

✻ Crunched for 1s · done Monday 8:28 PM

⏺ Agent "Extract startguide-vc" finished · 1m 28s

› Message from investor-extractor
  Written: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/soulmates-ventures.json. src.validate passed (1/1
  valid).
  Evidence: 3 deals, all within 24 months, newest 2026-09-03. They are
  Rightcharge (2026-09-03, Vestbee), Antiverse (2026-03-03, Vestbee) and
  Rightcharge (2025-10-23, the investor's own post).
  Left null: ticket.min only (the source says "up to EUR 3M"). Capital is the
  EUR 50M latest fund size, not AUM. The homepage's EUR 62M AUM was not quoted.
  Borderline: several quotes come from small-model WebFetch fragments (the
  Vestbee pages, kurzy.cz), so check_quotes should confirm them. The stage is
  only "seed" (a later stage is mentioned but not named). The sector mapping is
  partly interpretive. The brand also runs an accelerator-style program but
  invests equity. IČO 09789561 was confirmed on the investor's /legal/ page and
  the kurzy.cz mirror.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-12,investor-extractor,sonnet,startguide-vc,36183,18,88.1,ok" >>
      data/runs/run_log.csv)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      60  2026-10-12,investor-extractor,sonnet,spinoffy,20959,8,40.7,ok
      61  2026-10-12,investor-extractor,sonnet,rockawayx,28961,16,72.7,ok
      62  2026-10-12,investor-extractor,sonnet,seed-starter,35504,16,78.1
          ,ok
      63 +2026-10-12,investor-extractor,sonnet,startguide-vc,36183,18,88.
         +1,ok                                                           

⏺ Agent "Extract soulmates-ventures" finished · 3m 53s

› Message from investor-extractor
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/tachles.json. `src.validate` passed.
  Evidence dated within the last 24 months: 1 activity item (Hirundo,
  CzechCrunch article of 2025-02-12, so about 20 months old). Other dated items
  are sector (2024-06-13) and the undated type/stage quotes. Newest date is
  2025-02-12.
  Left null: hq_country, legal_entities (empty list), stages, ticket, capital,
  funds.
  Borderline:
  - The team's location is unclear. tachlesvc.com gives a Peachtree Corners, GA
  address, and the Czech Tachles VC Management s.r.o. sits in Prague (IČO not
  stated on the pages I read).
  - The Hirundo item is weak. The article lists it among 7 startups backed in
  2024, the role is unknown, the deal date is not stated, and Tachles' own
  amount is undisclosed.
  - I found no dated 2025–26 deal. Only the aggregator PitchBook lists 2026
  deals (Frostbridge, Papr), and I did not use it as evidence.

⏺ Agent "Extract tachles" finished · 1m 34s

⏺ I noticed Tachles VC's Hirundo deal date comes from a February 2025 recap
  article rather than the actual deal announcement—the exact
  article-date-vs-deal-date error flagged in PLAN §5.3. I'll leave this for the
  verifier to confirm and log.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && printf '%s\n' "20
      26-10-12,investor-extractor,sonnet,soulmates-ventures,38127,21,232.6,ok"
      "2026-10-12,in…)
  ⎿  34 remaining
     {
       "candidate_id": "tensor-ventures",
     … +22 lines (ctrl+o to expand)
  ⎿  Updated data/runs/run_log.csv (+2 -0)
      61  2026-10-12,investor-extractor,sonnet,rockawayx,28961,16,72.7,ok
      62  2026-10-12,investor-extractor,sonnet,seed-starter,35504,16,78.1
          ,ok
      63  2026-10-12,investor-extractor,sonnet,startguide-vc,36183,18,88.
          1,ok
      64 +2026-10-12,investor-extractor,sonnet,soulmates-ventures,38127,2
         +1,232.6,ok                                                     
      65 +2026-10-12,investor-extractor,sonnet,tachles,29912,20,93.5,ok  

› Message from investor-extractor
  Written: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/startupyard.json. src.validate passed.
  Evidence in the last 24 months: 1 item (Ydoca, CZK 500k, CzechCrunch), newest
  date 2025-02-14. That is about 20 months before AS_OF.
  Left null: capital (not_published). funds is empty. Instrument for the Ydoca
  deal is "unknown" because the article doesn't state it.
  Borderline: this is an accelerator (type vc, subtype accelerator). Its FAQ
  says a EUR 45k in-kind convertible note plus optional EUR 25k cash, about 5%
  equity. I set the ticket to the EUR 25k cash part only. No exclusion signal
  recorded.
  Borderline: the only registry entity found is the per-batch SPV "StartupYard
  Batch 15 s.r.o." (IČO 22266852), via a tier-3 mirror (finmag.cz). Other
  batches have their own IČOs, and I found no entity named plain StartupYard.
  Borderline: the Batch 15 announcement page prints no date. The sector quote
  carries 2025-09-11, which comes from the news archive listing.

⏺ Agent "Extract startupyard" finished · 1m 40s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-12,investor-extractor,sonnet,startupyard,36175,20,99.8,ok" >>
      data/runs/run_log.csv; pytho…)
  ⎿  {
       "candidate_id": "zaka-vc",
       "name": "Zaka VC",
     … +9 lines (ctrl+o to expand)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      63  2026-10-12,investor-extractor,sonnet,startguide-vc,36183,18,88.
          1,ok
      64  2026-10-12,investor-extractor,sonnet,soulmates-ventures,38127,2
          1,232.6,ok
      65  2026-10-12,investor-extractor,sonnet,tachles,29912,20,93.5,ok
      66 +2026-10-12,investor-extractor,sonnet,startupyard,36175,20,99.8,
         +ok                                                             

⏺ 4 background agents launched (↓ to manage)
   ├ Extract tensor-ventures
   ├ Extract tilia-impact-ventures
   ├ Extract united-founders
   └ Extract zaka-vc

⏺ StartupYard is done and logged. The next four extractions are running: Tensor
  Ventures, Tilia Impact Ventures, United Founders and Zaka VC. After them, 30
  of the 70 remain.
✻ Sautéed for 28s · done Monday 8:28 PM

› Message from investor-extractor
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/tilia-impact-ventures.json. `src.validate` passed
  (1/1).
  Evidence: 1 item dated within the last 24 months, newest 2026-05-19 (FaceUp,
  from the JIC Ventures release; Tilia took part as an existing investor). Legal
  entity is Tilia Impact Ventures, osoba rizikového kapitálu, s.r.o., IČO
  17848911, from the ARES API (tier 1).
  Null fields: `stages` (the site says only "Early stage", which doesn't map to
  the taxonomy), `capital`. `funds[]` is empty, because I couldn't verify a
  verbatim fund size. cc.cz (2023-09-21) mentions a Fund II target of EUR 32m.
  Borderline: the FaceUp `role` is `participant` and `instrument` is `unknown`.
  The Delta Green round (Oct 2025) is not cited, since I found no dated primary
  source. Both points are in `meta.notes`. Ticket EUR 300,000-1,200,000 is the
  investor's own "initial ticket" figure.

⏺ Tilia Impact Ventures is done: one dated deal in the window (FaceUp, May
  2026), and its legal entity is confirmed in the ARES registry. Three
  extractions are still running.

✻ Brewed for 1s · done Monday 8:29 PM

⏺ Agent "Extract tilia-impact-ventures" finished · 1m 23s

⏺ Agent "Extract united-founders" finished · 1m 23s

› Message from investor-extractor
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/united-founders.json. src.validate passed (1/1
  valid).
  Evidence items dated in the last 24 months: 2 (Peak Quantum, Wonderful.ai).
  Newest is 2026-04-14. Other dated sources used: Lupa 2025-11-05 (hq, sectors,
  stages, fund target).
  Left null: capital (not_published). No exclusion signals. Website was missing
  from the queue row; I found unitedfounders.vc.
  Borderline:
  - hq_country is CZ, but the team is spread across 8 European cities. Prague
  holds the GP, CFO, CTO and one managing partner.
  - The fund vehicle is a Luxembourg SCSp. The Czech entity is the investment
  advisor, United Founders Advisors s.r.o. (IČO 21594813, taken from the
  investor's own team page, not confirmed in a registry).
  - Peak Quantum is recorded as participant (the Munich Quantum Valley page says
  Cloudberry led). The Wonderful role is unknown.
  - EveryHealth is not confirmed by any fetched source, so it is not recorded.
  - Quotes from unitedfounders.vc (team page and homepage) came through WebFetch
  summaries, so run check_quotes on them. The ticket quote "Investment Ticket
  €100k - €1m" is the most likely to fail.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && printf '%s\n' "20
      26-10-12,investor-extractor,sonnet,tilia-impact-ventures,36484,17,83.0,ok"
      "2026-10-12,…)
  ⎿  30 remaining
     {
       "candidate_id": "btcz-ventures",
     … +16 lines (ctrl+o to expand)
  ⎿  Updated data/runs/run_log.csv (+2 -0)
      64  2026-10-12,investor-extractor,sonnet,soulmates-ventures,38127,2
          1,232.6,ok
      65  2026-10-12,investor-extractor,sonnet,tachles,29912,20,93.5,ok
      66  2026-10-12,investor-extractor,sonnet,startupyard,36175,20,99.8,
          ok
      67 +2026-10-12,investor-extractor,sonnet,tilia-impact-ventures,3648
         +4,17,83.0,ok                                                   
      68 +2026-10-12,investor-extractor,sonnet,united-founders,35797,18,8
         +3.2,ok                                                         

⏺ 2 background agents launched (↓ to manage)
   ├ Extract btcz-ventures
   └ Extract aternus-family-office

⏺ Tilia and United Founders are done and logged. Four extractions are running:
  Tensor Ventures, Zaka VC, BTCZ Ventures and Aternus Family Office. 28 rows
  remain after these.

✻ Cooked for 11s · done Monday 8:30 PM

› Message from investor-extractor
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/tensor-ventures.json. `src.validate` passed.
  - 2 activity items dated within the last 24 months. The newest is Edmund,
  2026-04-09 (Lupa.cz, Tensor as participant, Forward.one lead). The other is
  Repsense, 2025-12-17 (CzechCrunch, Tensor as lead).
  - Left null: ticket and capital (both not_published). The Fund I SCSp size is
  also not published.
  - The funds[] entry is Fund II with a target of EUR 50M (CzechCrunch, 15 May
  2024). The Czech management company Tensor Ventures a.s., IČO 06257241, is
  from the ARES API (tier 1).
  - Borderline:
    - The GP (Tensor Ventures GP S.à r.l.) and Fund I SCSp are Luxembourg
  entities. I found no registry number, so they are not in legal_entities.
    - The hint's Cnuic and PangeAI deals were not verified.
    - PitchBook gives 19 Mar 2026 for Edmund, which differs from the Lupa date.
  I did not use it.
    - The hq_country source is a Silicon Canals headline ("Czech-based…", tier
  3).

⏺ Tensor Ventures is done, with two dated deals in the window: Edmund (April
  2026) and Repsense (December 2025). Its Czech legal entity came from the ARES
  registry. I'll log it when the usage notification arrives; three extractions
  are still running.

✻ Churned for 1s · done Monday 8:30 PM

⏺ Agent "Extract tensor-ventures" finished · 1m 53s

› Message from investor-extractor
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/zaka-vc.json. src.validate passed.
  Evidence dated within 24 months: 3 (DeepSeq.AI 2026-02-16, Nephrogen
  2025-11-28, Vetstor 2025-04-08); newest is 2026-02-16.
  Left null: ticket (the site gives only "minimum ticket is 130K", no currency),
  capital, fund vintage, and legal_entities (empty).
  Borderline: no legal entity or IČO confirmed. ZAKA Management s.r.o. (IČO
  21053987) exists but nothing ties it to ZAKA VC, so K1 may fail. HQ is set to
  CZ from a cc.cz quote ("České fondy Zaka VC…"); the firm lists offices in
  Prague, Bratislava, London and Silicon Valley without naming an HQ. Newer
  deals (ParcelBio, Cirrus, FinalDose) are on undated or LinkedIn pages, and the
  site shows 17M with no currency against EUR 15M on the story page.
  Quote-check the itkey and cc.cz quotes.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-12,investor-extractor,sonnet,tensor-ventures,42220,20,112.9,ok"
      >> data/runs/run_log.csv)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      66  2026-10-12,investor-extractor,sonnet,startupyard,36175,20,99.8,
          ok
      67  2026-10-12,investor-extractor,sonnet,tilia-impact-ventures,3648
          4,17,83.0,ok
      68  2026-10-12,investor-extractor,sonnet,united-founders,35797,18,8
          3.2,ok
      69 +2026-10-12,investor-extractor,sonnet,tensor-ventures,42220,20,1
         +12.9,ok                                                        

⏺ Agent "Extract zaka-vc" finished · 1m 57s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-12,investor-extractor,sonnet,zaka-vc,39838,21,117.0,ok" >>
      data/runs/run_log.csv && git ad…)
  ⎿  28 remaining
     {
       "candidate_id": "bd-partners",
     … +20 lines (ctrl+o to expand)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      67  2026-10-12,investor-extractor,sonnet,tilia-impact-ventures,3648
          4,17,83.0,ok
      68  2026-10-12,investor-extractor,sonnet,united-founders,35797,18,8
          3.2,ok
      69  2026-10-12,investor-extractor,sonnet,tensor-ventures,42220,20,1
          12.9,ok
      70 +2026-10-12,investor-extractor,sonnet,zaka-vc,39838,21,117.0,ok 
  ⎿  (another command ran in this repository at the same time; a change 
     made by either may show under either result)

⏺ 2 background agents launched (↓ to manage)
   ├ Extract bd-partners
   └ Extract braiins

⏺ Tensor Ventures and Zaka VC are done and committed. Four extractions are
  running: BTCZ Ventures, Aternus Family Office, BD Partners and Braiins. 26
  rows remain after these.

✻ Cooked for 16s · done Monday 8:30 PM

› Message from investor-extractor
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/btcz-ventures.json. src.validate passed (1/1
  valid).
  Evidence within the last 24 months: 3 items in total (type, sectors, one
  activity item), all from the same IOCB Prague page dated 2025-12-03. That is
  also the newest date.
  Left null: website, hq_country, stages, ticket, capital, funds,
  legal_entities, and the activity role and instrument (both "unknown").
  Borderline:
  - BTCZ's own site and the legal entity/IČO were not found, and Prague as the
  team location is only a PitchBook lead, so hq_country is null.
  - The Taveren deal is only weakly shown. The IOCB page says BTCZ has supported
  the research for several years and that BPD Partners made a "latest
  contribution". It does not say that BTCZ invested in the Dec 2025 round or
  what the amount was.
  - BTCZ is a family-office venture arm (BPD Partners plus B3 Holding), so type
  "vc" is a judgment call.

⏺ BTCZ Ventures is done, but its record lists an investment its own source
  doesn't support: the IOCB page doesn't say BTCZ invested in the December 2025
  Taveren round. I'm logging that as AI error E-14 and leaving the item for the
  verifier and decide.py.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && cat >>
      docs/ai-errors.md <<'EOF'
      | E-14 | 2026-10-12 | investor-extractor | btcz-ventures | `evidence_of…)
  ⎿  Updated docs/ai-errors.md (+1 -0)
      17  | E-11 | 2026-10-12 | investor-extractor (zkušební běh) | credo
          -ventures | `stages` | Uvedena jen fáze `pre_seed`, ačkoli web 
          uvádí víc fází. | Orchestrátor (R3). | Prompt: uvést všechny fá
          ze, které zdroj jmenuje. |
      18  | E-12 | 2026-10-12 | všichni agenti (infrastruktura) | credo-v
          entures, depo-ventures, triáž batch 07/09 | — | Ne chyba modelu
          : Claude Code má na jednu relaci 200 vyhledávání sdílených všem
          i agenty (doplňuje se ~100/h). Triáž je spotřebovala, extraktor
           pak nedohledal investice z nápovědy. | Text chyby nástroje ve 
          výstupu agenta. | Prompt: max. 6 vyhledávání na kandidáta, nejd
          řív vlastní stránky kandidáta, příznak `SEARCH_BUDGET_EXHAUSTED
          ` v `meta.notes`. Extrakce běží po 4 s odstupem podle doplňován
          í limitu (D-017). |
      19  | E-13 | 2026-10-12 | investor-extractor | inven-capital | `evi
          dence_of_activity[0].role`, `ticket`, `type` | Role `co_lead` u
           investice Wint převzata ze shrnutí výsledku vyhledávání, ne z 
          citace (porušuje pravidlo „snippet není důkaz“); citace ticketu
           „Ticket size 2-30m EUR“ je poskládaná z popisku a hodnoty, ne 
          doslovná; typ `vc`, ačkoli jde o fond skupiny ČEZ (`cvc`), prot
          ože agent nenašel citaci. | Závěrečná zpráva agenta, kterou čet
          l orchestrátor. | Zatím nic; zachytí to `check_quotes.py` a ově
          řovatel. Pokud se vzor zopakuje, upravím prompt. |
      20 +| E-14 | 2026-10-12 | investor-extractor | btcz-ventures | `evi
         +dence_of_activity[0]` | Zapsána investice do Taveren (12/2025),
         + ačkoli zdroj (stránka IOCB) říká jen, že BTCZ výzkum dlouhodob
         +ě podporuje a „poslední příspěvek“ dala BPD Partners; účast BTC
         +Z v kole z prosince 2025 nedokládá. | Agent to sám přiznal v zá
         +věrečné zprávě. | Zatím nic; čekám, zda položku odmítne ověřova
         +tel (R6). Pokud ano, decide.py ji vynuluje. |                  

⏺ Agent "Extract btcz-ventures" finished · 44s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-12,investor-extractor,sonnet,btcz-ventures,23793,9,44.3,ok" >>
      data/runs/run_log.csv; pyth…)
  ⎿  26 remaining
     {
       "candidate_id": "dendis-capital",
     … +8 lines (ctrl+o to expand)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      68  2026-10-12,investor-extractor,sonnet,united-founders,35797,18,8
          3.2,ok
      69  2026-10-12,investor-extractor,sonnet,tensor-ventures,42220,20,1
          12.9,ok
      70  2026-10-12,investor-extractor,sonnet,zaka-vc,39838,21,117.0,ok
      71 +2026-10-12,investor-extractor,sonnet,btcz-ventures,23793,9,44.3
         +,ok                                                            

⏺ investor-extractor(Extract dendis-capital)
  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)

⏺ BTCZ Ventures is logged. Four extractions are running: Aternus Family Office,
  BD Partners, Braiins and Dendis Capital. That leaves 25 rows after these.

✻ Worked for 15s · done Monday 8:31 PM

› Message from investor-extractor
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/aternus-family-office.json; src.validate passed.
  - Evidence dated in the last 24 months: 1 (Jutro Medical Series A extension,
  Tech.eu, 2025-12-16, which is also the newest).
  - Left null: stages, ticket, capital (all not_published); funds is empty.
  - Borderline, exclusion signal: fund_of_funds_or_lp_only. Aternus is a multi
  family office whose portfolio is mainly stakes in PE, real estate and VC
  funds. The site says it co-invests directly only in "exceptional" cases.
  - Borderline, evidence: the single deal comes from a tier-3 source and states
  no role or instrument (role is participant and instrument is unknown in the
  record). The Aternus site has no dated deal pages.
  - Borderline, entity match: ATERNUS, a.s. IČO 25865056 comes from the website
  title plus a podnikatel.cz mirror. The mirror seat is Praha (Anežská 986/10)
  and the website gives Třinec. The registry quote I used is the statutory-body
  sentence, which does not show the name or IČO, so the quote check may flag it.
  The link between the family office and this entity is not fully confirmed.

⏺ Aternus Family Office is done. The extractor flagged it as mainly a
  fund-of-funds investor that co-invests directly only in exceptional cases,
  with one dated direct deal (Jutro Medical, December 2025). Code will weigh
  that signal against the deal at the decide step. I'll log the run once the
  usage figures arrive.

✻ Cooked for 2s · done Monday 8:31 PM

⏺ Agent "Extract aternus-family-office" finished · 1m 1s
› Message from investor-extractor
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/braiins.json, and src.validate passed.
  Evidence items within 24 months: 1 (Firefish seed, announced 2025-04-08, from
  Braiins' own blog, so self-reported). The hq_country source is dated
  2026-05-19, but it is not an activity item.
  Left null: type, sectors, stages, ticket, capital. The legal_entities list is
  empty because I found no IČO or imprint. funds is empty.
  Borderline: Braiins is an operating bitcoin-mining company, not a fund, so at
  most a corporate investor. It has one known minority investment (a 15% stake
  in Firefish). The fetched page does not state its role, so role is "unknown".
  I did not record the CAMMS Capital purchase as an investment because it was a
  whole-company acquisition. The Czech team location is unconfirmed; CZ comes
  from a media description of Braiins as a Czech company.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo "2026-10-12,
      investor-extractor,sonnet,aternus-family-office,30729,11,61.4,ok" >>
      data/runs/run_log.…)
  ⎿  25 remaining
     {
       "candidate_id": "emun",
     … +8 lines (ctrl+o to expand)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      69  2026-10-12,investor-extractor,sonnet,tensor-ventures,42220,20,1
          12.9,ok
      70  2026-10-12,investor-extractor,sonnet,zaka-vc,39838,21,117.0,ok
      71  2026-10-12,investor-extractor,sonnet,btcz-ventures,23793,9,44.3
          ,ok
      72 +2026-10-12,investor-extractor,sonnet,aternus-family-office,3072
         +9,11,61.4,ok                                                   

⏺ Agent "Extract braiins" finished · 1m 7s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-12,investor-extractor,sonnet,braiins,28516,15,66.6,ok" >>
      data/runs/run_log.csv && git add…)
  ⎿  {
       "candidate_id": "jsk-investments",
       "name": "JSK Investments",
     … +9 lines (ctrl+o to expand)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      70  2026-10-12,investor-extractor,sonnet,zaka-vc,39838,21,117.0,ok
      71  2026-10-12,investor-extractor,sonnet,btcz-ventures,23793,9,44.3
          ,ok
      72  2026-10-12,investor-extractor,sonnet,aternus-family-office,3072
          9,11,61.4,ok
      73 +2026-10-12,investor-extractor,sonnet,braiins,28516,15,66.6,ok  

⏺ 2 background agents launched (↓ to manage)
   ├ Extract emun
   └ Extract jsk-investments

⏺ Aternus, Braiins and BTCZ are logged and committed. Four extractions are
  running: BD Partners, Dendis Capital, EMUN and JSK Investments. 23 rows remain
  after these.

✻ Brewed for 18s · done Monday 8:32 PM

› Message from investor-extractor
  Written: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/bd-partners.json. src.validate passed.
  Evidence dated within 24 months: 1 (Myriad AI seed, Lupa.cz, 2025-09-16). The
  WanderWallet pre-seed (DEPO Ventures page, no printed date) is cited with
  announced_date null.
  Null fields: stages, ticket, capital (all not_published). ticket and capital
  are null because the CzechCrunch interview figures (250k-2M EUR, about 20M
  EUR) are not clearly a first cheque or AUM. funds is empty.
  Borderline:
  - bdpartners.cz is JavaScript-only, so identity comes from a Finmag/ARES
  mirror (BD Partners a.s., IČO 19286511, Praha-Dejvice).
  - The firm describes itself as a "joint family office" of two individuals, so
  type is family_office. It could also be read as private_holding.
  - The team location is inferred from the registered seat. Quote-check risk:
  the Lupa quote is short, and the registry quote is a title line from the
  mirror page.

⏺ BD Partners is done. It calls itself a joint family office of two people, so
  it falls outside the pilot's VC/CVC scope, and code should exclude it at the
  decide step. Three extractions are still running.

✻ Churned for 1s · done Monday 8:32 PM

⏺ Agent "Extract bd-partners" finished · 1m 32s

› Message from investor-extractor
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/dendis-capital.json. `src.validate` passed.
  Evidence: 1 item within 24 months, the newest dated 2026-07-14 (HTG Medical
  pre-seed, České noviny). Dendis appears there as an existing investor, so role
  is participant. The instrument is `unknown` because the source doesn't say.
  Left null: ticket and capital (both not_published); funds is empty. Stages is
  only `growth`: the site also says it backs "začínající podniky" but gives no
  stage label.
  Borderline: the entity is a family foundation (nadační fond, IČ 19786514) that
  invests directly, typed family_office. The IČ comes from the site footer; I
  couldn't confirm it in the registry. The hint's Carebot deal is unconfirmed. A
  Forbes.cz report on Carebot's 2026 round doesn't name Dendis, and only
  trackers list Dendis for Carebot in Sep 2025, so I left it out.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-12,investor-extractor,sonnet,bd-partners,40405,21,92.0,ok" >>
      data/runs/run_log.csv; pytho…)
  ⎿  23 remaining
     {
       "candidate_id": "metatron-global",
     … +7 lines (ctrl+o to expand)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      71  2026-10-12,investor-extractor,sonnet,btcz-ventures,23793,9,44.3
          ,ok
      72  2026-10-12,investor-extractor,sonnet,aternus-family-office,3072
          9,11,61.4,ok
      73  2026-10-12,investor-extractor,sonnet,braiins,28516,15,66.6,ok
      74 +2026-10-12,investor-extractor,sonnet,bd-partners,40405,21,92.0,
         +ok                                                             

⏺ Agent "Extract dendis-capital" finished · 1m 15s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-12,investor-extractor,sonnet,dendis-capital,34493,15,75.1,ok" >>
      data/runs/run_log.csv &&…)
  ⎿  {
       "candidate_id": "muni-ventures",
       "name": "MUNI Ventures",
     … +7 lines (ctrl+o to expand)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      72  2026-10-12,investor-extractor,sonnet,aternus-family-office,3072
          9,11,61.4,ok
      73  2026-10-12,investor-extractor,sonnet,braiins,28516,15,66.6,ok
      74  2026-10-12,investor-extractor,sonnet,bd-partners,40405,21,92.0,
          ok
      75 +2026-10-12,investor-extractor,sonnet,dendis-capital,34493,15,75
         +.1,ok                                                          

⏺ Stop Task
  ⎿  Extract emun · stopped

⏺ Stop Task
  ⎿  Extract jsk-investments · stopped

⏺ Agent "Extract emun" was stopped by Claude

⏺ Agent "Extract jsk-investments" was stopped by Claude

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && ls
      data/records/staging/emun.json data/records/staging/jsk-investments.json
      2>&1; mkdir -p data/records/…)
  ⎿  ls: data/records/staging/emun.json: No such file or directory
     ls: data/records/staging/jsk-investments.json: No such file or directo
     ry
     44
  ⎿  Updated data/runs/run_log.csv (+2 -0)
      73  2026-10-12,investor-extractor,sonnet,braiins,28516,15,66.6,ok
      74  2026-10-12,investor-extractor,sonnet,bd-partners,40405,21,92.0,
          ok
      75  2026-10-12,investor-extractor,sonnet,dendis-capital,34493,15,75
          .1,ok
      76 +2026-10-12,investor-extractor,sonnet,emun,,,,failed            
      77 +2026-10-12,investor-extractor,sonnet,jsk-investments,,,,failed 

⏺ Your usage limit was reached, so I've stopped at step R3 (extraction), as the
  runbook says to on a usage limit. Everything is committed and pushed.

  Done:
  - R0 setup: tests pass and ECB rates are loaded.
  - R1 triage: all 225 candidates triaged.
  - R2 queue: 158 candidates queued; 70 of them selected for extraction (D-016).
  - R3 extraction: 44 staging records exist, from the 69 unique queued
    candidates (one queue row is a duplicate, D-018). All 44 passed src.validate
    when the agents wrote them. I stopped the EMUN and JSK Investments
    extractions mid-run; neither wrote a file, and both are logged as failed in
    the run log.
  - Logs: decisions D-014 to D-018 and AI errors E-06 to E-14 are recorded. The
    extractor prompt fix has its own agents: commit.

  One correction: the last commit message says "45 of 69 extracted", but the
  actual count is 44.

  Left to do:
  - R3: the remaining 25 candidates, starting with EMUN, JSK Investments,
    Metatron Global and MUNI Ventures. At the search-refill pace that's about
    1.5 hours.
  - R4–R8: validate, quote check, verifier, decide, and the review sheet.
  - For you: whether to add seed-starter-ceske-sporitelny → seed-starter to
    aliases.csv.

  When you're ready, say continue; the runbook resumes from the first queue row
  without a record.

⏺ Usage limit reached · continuing automatically at 10pm · esc to cancel

✻ Worked for 26m 22s · done Monday 8:32 PM

⏺ Automatic continue cancelled · /rate-limit-options to re-arm

❯ continue                                                                      

  Ran 1 shell command (ctrl+o to expand)

⏺ Resuming R3 with 25 rows left. To keep prompts short, each agent now reads its
  own queue row from extract_selected.csv; the input is the same as before.

⏺ 4 background agents launched (↓ to manage)
   ├ Extract emun
   ├ Extract jsk-investments
   ├ Extract metatron-global
   └ Extract muni-ventures

⏺ While these four run, I'll start R4 on the 44 existing records.

  Ran 1 shell command (ctrl+o to expand)

⏺ All 44 records are valid. I'll run the quote check (R5) once extraction
  finishes, so it doesn't read records an agent is still editing.

✻ Brewed for 24s · done 3:49 PM
› Message from investor-extractor
  - Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/muni-ventures.json. `src.validate` passed.
  - No evidence items within 24 months; `evidence_of_activity` is empty. I found
  no investment by MUNI Ventures.
  - Null fields: website, hq_country, type, sectors, stages, ticket, capital.
  `funds` is empty.
  - Borderline: this is a Masaryk University technology-transfer subsidiary,
  founded 2024 and wholly owned by the university.
    - The founding article, dated 2024-04-25 on em.muni.cz, says it may enter
  investment funds on the university's behalf, but I found no direct company
  investments.
    - I recorded a weak `grant_or_program_only` signal (quote from that article)
  and left the decision to code.
    - The legal entity is MUNI Ventures, s.r.o., IČO 21503559, taken from a
  podnikatel.cz registry mirror (tier 3).
    - I did not confirm the IČO in the official registry. I used 2 searches and
  2 fetches.

⏺ MUNI Ventures is done: no direct investments found, so code will exclude it.
  Three extractions are still running.

✻ Churned for 1s · done 3:49 PM

⏺ Agent "Extract muni-ventures" finished · 43s

› Message from investor-extractor
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/emun.json. src.validate passed.
  - Evidence items dated within the last 24 months: 0. evidence_of_activity is
  empty, so there is no newest date.
  - Null fields: sectors, stages and ticket (not_published). funds is empty and
  evidence_of_activity is empty. capital is the reported AUM, CZK 16 bn, with
  as_of null.
  - Registry: IČO 28495349 (EMUN investiční společnost, a.s.) comes only from
  the mesec.cz mirror page. I did not confirm it in the register itself.
  - Borderline: EMUN is a wealth manager / multi-family office. Its Global
  Unicorns fund targets unicorns and is open-ended. A search summary said it
  buys through other funds, but I could not confirm that on a fetched page, so I
  recorded no fund_of_funds exclusion signal. A news item of 18 Sep 2026 says
  EMUN is developing "venture capital a growth equity" but names no deals. The
  funds page returned HTTP 500. Overall: likely no recent deal and a possible
  LP/access-only model.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-13,investor-extractor,sonnet,muni-ventures,29541,10,43.0,ok" >>
      data/runs/run_log.csv)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      75  2026-10-12,investor-extractor,sonnet,dendis-capital,34493,15,75
          .1,ok
      76  2026-10-12,investor-extractor,sonnet,emun,,,,failed
      77  2026-10-12,investor-extractor,sonnet,jsk-investments,,,,failed
      78 +2026-10-13,investor-extractor,sonnet,muni-ventures,29541,10,43.
         +0,ok                                                           

⏺ investor-extractor(Extract odyssey-44)
  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)

⏺ Agent "Extract emun" finished · 54s

› Message from investor-extractor
  - Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/metatron-global.json. `src.validate` passed.
  - 1 evidence item within 24 months, dated 2024-01-17: Ticketoo, from il
  Dolomiti (tier 3). The page names only "Metatron" as entering the company's
  capital.
  - Fields left null: website, hq_country, legal_entities (empty list), type,
  sectors, stages, ticket, capital. Funds is empty. The candidate's own domain,
  metatron.global, is only a registrar placeholder, and I found no registry
  entry or IČO.
  - Borderline: the link between the "Metatron" in the Ticketoo deal and
  Metatron Global is unconfirmed. It rests on aggregator listings only. The e15
  article (2015-08-31) says the company was created to invest in tech and
  internet start-ups, and names Vladimír Johanes and his sons as founders. Role
  is "participant", instrument "unknown" and round null, because the page
  doesn't state them. There are no exclusion signals, but the team's country is
  not established, so the record may be excluded as not found.

⏺ Agent "Extract metatron-global" finished · 54s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && printf '%s\n'
      "2026-10-13,investor-extractor,sonnet,emun,30553,13,54.0,ok"
      "2026-10-13,investor-extracto…)
  ⎿  hint: See the 'Note about fast-forwards' in 'git push --help' for deta
     ils.
  ⎿  Updated data/runs/run_log.csv (+2 -0)
      76  2026-10-12,investor-extractor,sonnet,emun,,,,failed
      77  2026-10-12,investor-extractor,sonnet,jsk-investments,,,,failed
      78  2026-10-13,investor-extractor,sonnet,muni-ventures,29541,10,43.
          0,ok
      79 +2026-10-13,investor-extractor,sonnet,emun,30553,13,54.0,ok     
      80 +2026-10-13,investor-extractor,sonnet,metatron-global,28370,11,5
         +4.7,ok                                                         
  ⎿  (another command ran in this repository at the same time; a change 
     made by either may show under either result)

⏺ 2 background agents launched (↓ to manage)
   ├ Extract rockaway-capital
   └ Extract springtide-ventures

⏺ The push was rejected again because the remote has new commits. I'll check
  what they are before merging.

  Ran 1 shell command (ctrl+o to expand)

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && git pull -q
      --no-rebase --no-edit && git push -q 2>&1|tail -1; git log --oneline -2)
  ⎿  c8f26dc Merge branch 'main' of https://github.com/DavidKoktavy/investo
     r-db
     e13789d data: R3 records emun, metatron-global, muni-ventures
  ⎿  Updated README.md (+1 -1)
  ⎿  (a git step in this command can move the working tree, so these may be
     its changes, not edits) (ctrl+o to expand)

⏺ The remote change was a one-line README edit; I merged it and pushed. Three
  extractions are running now (Odyssey 44, Rockaway Capital, Springtide
  Ventures), and JSK Investments is still in progress.

✻ Crunched for 22s · done 3:50 PM

› Message from investor-extractor
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/jsk-investments.json. `src.validate` passed (1/1
  valid). I did not run the quote check.
  - Evidence: 3 items, 2 within the last 24 months. The newest is MintNeuro,
  2026-10-09 (JSK's own news page); the other recent one is Andromeda Surgical
  Series A, 2026-09-15 (CzechCrunch). Elin.ai pre-seed, 2024-12-09 (Lupa.cz), is
  older than 24 months, so it counts only as the third deal.
  - Fields left null: `ticket` (not_published). The EUR 125k figure is the
  minimum investment for qualified investors in the SICAV, not JSK's own cheque.
  - Legal entity: JSK Investments SICAV a.s., IČO 23823445, from the ARES API
  (tier 1), created 2025-10-09. The older JSK Investments s.r.o. (IČO 06224270)
  is a different entity.
  - Borderline:
    - `type` is set to `vc`, not the triage hint `private_holding`. The vehicle
  is a CNB-licensed SICAV with Private & Growth Equity and Venture Capital
  subfunds, and the type quote comes from Newstream (2025-10-01).
    - `capital` (CZK 2bn) is the initial SICAV volume, entered as
  `latest_fund_size`, not AUM.
    - Role is `participant` for all three deals and instrument is `unknown`;
  none of the sources state them. The source pages do not call JSK a lead.
    - The sectors listed are the stated sectors of the Private & Growth Equity
  subfund, not the VC subfund.
    - The VC deals seen are medtech, neurotech and AI.

⏺ JSK Investments is done. Under the old triage rule it would have been excluded
  as a private holding without extraction. It now has a recent dated deal and a
  CNB-licensed fund with a VC sub-fund, which supports the D-015 rule change.

  The extractor called the Elin.ai deal (Dec 2024) "older than 24 months", but
  the window starts on 2024-10-11. This is the third time an extractor has
  misjudged the window. It doesn't affect results, because code computes it, so
  I'll log it as one recurring error.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && cat >>
      docs/ai-errors.md <<'EOF'
      | E-15 | 2026-10-13 | investor-extractor (opakovaně) | lighthouse-ventu…)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      78  2026-10-13,investor-extractor,sonnet,muni-ventures,29541,10,43.
          0,ok
      79  2026-10-13,investor-extractor,sonnet,emun,30553,13,54.0,ok
      80  2026-10-13,investor-extractor,sonnet,metatron-global,28370,11,5
          4.7,ok
      81 +2026-10-13,investor-extractor,sonnet,jsk-investments,,,,ok     
  ⎿  Updated docs/ai-errors.md (+1 -0)
      18  | E-12 | 2026-10-12 | všichni agenti (infrastruktura) | credo-v
          entures, depo-ventures, triáž batch 07/09 | — | Ne chyba modelu
          : Claude Code má na jednu relaci 200 vyhledávání sdílených všem
          i agenty (doplňuje se ~100/h). Triáž je spotřebovala, extraktor
           pak nedohledal investice z nápovědy. | Text chyby nástroje ve 
          výstupu agenta. | Prompt: max. 6 vyhledávání na kandidáta, nejd
          řív vlastní stránky kandidáta, příznak `SEARCH_BUDGET_EXHAUSTED
          ` v `meta.notes`. Extrakce běží po 4 s odstupem podle doplňován
          í limitu (D-017). |
      19  | E-13 | 2026-10-12 | investor-extractor | inven-capital | `evi
          dence_of_activity[0].role`, `ticket`, `type` | Role `co_lead` u
           investice Wint převzata ze shrnutí výsledku vyhledávání, ne z 
          citace (porušuje pravidlo „snippet není důkaz“); citace ticketu
           „Ticket size 2-30m EUR“ je poskládaná z popisku a hodnoty, ne 
          doslovná; typ `vc`, ačkoli jde o fond skupiny ČEZ (`cvc`), prot
          ože agent nenašel citaci. | Závěrečná zpráva agenta, kterou čet
          l orchestrátor. | Zatím nic; zachytí to `check_quotes.py` a ově
          řovatel. Pokud se vzor zopakuje, upravím prompt. |
      20  | E-14 | 2026-10-12 | investor-extractor | btcz-ventures | `evi
          dence_of_activity[0]` | Zapsána investice do Taveren (12/2025),
           ačkoli zdroj (stránka IOCB) říká jen, že BTCZ výzkum dlouhodob
          ě podporuje a „poslední příspěvek“ dala BPD Partners; účast BTC
          Z v kole z prosince 2025 nedokládá. | Agent to sám přiznal v zá
          věrečné zprávě. | Zatím nic; čekám, zda položku odmítne ověřova
          tel (R6). Pokud ano, decide.py ji vynuluje. |
      21 +| E-15 | 2026-10-13 | investor-extractor (opakovaně) | lighthou
         +se-ventures, patero, metatron-global, jsk-investments | závěreč
         +ná zpráva | Agent chybně počítá okno 24 měsíců od AS_OF (2026-1
         +0-11 → začátek 2024-10-11): Outfindo 2025-01 a Elin.ai 2024-12 
         +označil za starší než 24 měsíců, naopak Flowpay 2024-03 a Ticke
         +too 2024-01 za čerstvé. | Orchestrátor při čtení závěrečných zp
         +ráv. | Nic: okno počítá `decide.py` z dat v záznamu, chyba je j
         +en v textu zprávy. Potvrzuje princip „agent sbírá fakta, kód ro
         +zhoduje“. |                                                    
  ⎿  (another command ran in this repository at the same time; a change 
     made by either may show under either result)

⏺ Agent "Extract jsk-investments" finished · 1m 50s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && sed -i ''
      's/^2026-10-13,investor-extractor,sonnet,jsk-investments,,,,ok$/2026-10-13
      ,investor-extractor,…)
  ⎿  2026-10-13,investor-extractor,sonnet,jsk-investments,45894,19,110.4,ok
  ⎿  Updated data/runs/run_log.csv (+1 -1)
      78  2026-10-13,investor-extractor,sonnet,muni-ventures,29541,10,43.
          0,ok
      79  2026-10-13,investor-extractor,sonnet,emun,30553,13,54.0,ok
      80  2026-10-13,investor-extractor,sonnet,metatron-global,28370,11,5
          4.7,ok
      81 -2026-10-13,investor-extractor,sonnet,jsk-investments,,,,ok     
      81 +2026-10-13,investor-extractor,sonnet,jsk-investments,45894,19,1
         +10.4,ok                                                        
  ⎿  (another command ran in this repository at the same time; a change 
     made by either may show under either result)

⏺ investor-extractor(Extract stredocesky-inovacni-centrum)
  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)

⏺ JSK Investments is logged. Four extractions are now running: Odyssey 44,
  Rockaway Capital, Springtide Ventures and Středočeské inovační centrum. 17
  queue rows remain after these.

✻ Worked for 14s · done 3:51 PM

› Message from investor-extractor
  - Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/springtide-ventures.json; src.validate passed.
  - 1 activity item dated within the last 24 months: ThreatMark, 2025-01-07, an
  USD 8M convertible note, cited from ThreatMark's own press release. The second
  item is Source Defense Series B (2022-04-27, cc.cz), which is outside the
  window.
  - Left null: `capital` (not_published; it invests only KKCG money). `funds` is
  empty. Everything else has a source.
  - Borderline:
    - Captive KKCG venture arm, a 100% subsidiary with no external LPs. I typed
  it `cvc`, not the triage's `private_holding`.
    - The ThreatMark role is `unknown`. The press release names Springtide as
  the largest shareholder, but one outlet (ain.ua) says Springtide led the
  round, which conflicts with the company's own release.
    - The registry source is a tier-3 kurzy.cz mirror, IČO 01726587.
    - The firm's own news page shows no deal after August 2022. The newest deal
  I could source is ThreatMark in January 2025.
    - I did not check ČNB JERRS.

⏺ Springtide Ventures is done and typed cvc, which confirms the triage mistype
  (E-08) that D-015 corrected. It has one dated deal in the window: ThreatMark,
  January 2025, from the company's own press release. Three extractions are
  still running.

✻ Brewed for 2s · done 3:52 PM

⏺ Agent "Extract springtide-ventures" finished · 1m 46s

› Message from investor-extractor
  Written: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/stredocesky-inovacni-centrum.json; src.validate
  passed (1/1).
  Evidence dated within 24 months: 1 (Elredo, 2026-10-01, CzechCrunch cc.cz).
  Newest: 2026-10-01.
  Null fields: type (not_published), capital (not_published), funds (empty),
  Elredo company_website, round, instrument=unknown.
  Borderline: SIC is a regional innovation agency (spolek, IČO 04228235,
  registry source is the tier-3 podnikatel.cz mirror). SIC Ventures invests by
  convertible loan or equity, ticket up to EUR 80k (stated max, min null). Only
  one deal found. The article names "investiční program SIC" among Elredo
  investors (JIC Ventures led), with no amount or instrument. The quote
  "investiční program SIC a švédští Bond Ventures" is a fragment pieced from
  WebFetch output and was not checked against the raw page. sic.cz is an
  unrelated IT firm; the real site is s-ic.cz. The sectors/stages/ticket page is
  undated.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo "2026-10-13,
      investor-extractor,sonnet,springtide-ventures,38118,22,105.5,ok" >>
      data/runs/run_log.c…)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      79  2026-10-13,investor-extractor,sonnet,emun,30553,13,54.0,ok
      80  2026-10-13,investor-extractor,sonnet,metatron-global,28370,11,5
          4.7,ok
      81  2026-10-13,investor-extractor,sonnet,jsk-investments,45894,19,1
          10.4,ok
      82 +2026-10-13,investor-extractor,sonnet,springtide-ventures,38118,
         +22,105.5,ok                                                    
  ⎿  (another command ran in this repository at the same time; a change 
     made by either may show under either result)

⏺ investor-extractor(Extract thein)  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)

⏺ Agent "Extract stredocesky-inovacni-centrum" finished · 1m 47s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo "2026-10-13,
      investor-extractor,sonnet,stredocesky-inovacni-centrum,36158,23,106.8,ok"
      >> data/runs/…)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      80  2026-10-13,investor-extractor,sonnet,metatron-global,28370,11,5
          4.7,ok
      81  2026-10-13,investor-extractor,sonnet,jsk-investments,45894,19,1
          10.4,ok
      82  2026-10-13,investor-extractor,sonnet,springtide-ventures,38118,
          22,105.5,ok
      83 +2026-10-13,investor-extractor,sonnet,stredocesky-inovacni-centr
         +um,36158,23,106.8,ok                                           
  ⎿  (another command ran in this repository at the same time; a change 
     made by either may show under either result)

⏺ investor-extractor(Extract budeto)
  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)

⏺ Středočeské inovační centrum and Springtide are done and committed. Four
  extractions are running: Odyssey 44, Rockaway Capital, Thein and Budeto. 15
  queue rows remain after these.

✻ Cooked for 12s · done 3:53 PM

⏺ Agent "Extract soulmates-ventures" finished · 19h 29m 6s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && sed -i ''
      's/^2026-10-12,investor-extractor,sonnet,soulmates-ventures,38127,21,232.6
      ,ok$/2026-10-12,inve…)
  ⎿  2026-10-12,investor-extractor,sonnet,soulmates-ventures,40634,21,232.6
     ,ok
  ⎿  Updated data/runs/run_log.csv (+1 -1)
      61  2026-10-12,investor-extractor,sonnet,rockawayx,28961,16,72.7,ok
      62  2026-10-12,investor-extractor,sonnet,seed-starter,35504,16,78.1
          ,ok
      63  2026-10-12,investor-extractor,sonnet,startguide-vc,36183,18,88.
          1,ok
      64 -2026-10-12,investor-extractor,sonnet,soulmates-ventures,38127,2
         -1,232.6,ok                                                     
      64 +2026-10-12,investor-extractor,sonnet,soulmates-ventures,40634,2
         +1,232.6,ok                                                     
      65  2026-10-12,investor-extractor,sonnet,tachles,29912,20,93.5,ok
      66  2026-10-12,investor-extractor,sonnet,startupyard,36175,20,99.8,
          ok
      67  2026-10-12,investor-extractor,sonnet,tilia-impact-ventures,3648
          4,17,83.0,ok

⏺ An earlier Soulmates Ventures extraction reported its final token count, so I
  updated its run-log row. Four extractions are still running: Odyssey 44,
  Rockaway Capital, Thein and Budeto.

✻ Baked for 5s · done 3:53 PM

› Message from investor-extractor
  - Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/odyssey-44.json. `src.validate` passed.
  - Evidence items dated within the last 24 months: 0. The only deal found is
  FlixMobility (FlixBus), cc.cz, 2019-08-09, role participant.
  - Fields left null: sectors, stages and capital (all not_published). The
  ticket has min EUR 20,000,000 and no max.
  - Borderline: this is a Prague family office (Martin Kúšik, IČO 02494213 from
  its own site, not confirmed in a registry). The site says "We do not invest
  into start-ups", and its minimum is EUR 20m equity. Press suggests a shift to
  listed bonds and stocks, but I did not cite it. The Seedtable VC listing is
  not corroborated. There is no recent deal, so the record will probably be
  dormant or out of scope for type. I added no exclusion_signals, because no
  schema code fits a growth or PE-style family office.

⏺ Odyssey 44 is done. It's a Prague family office whose site says "We do not
  invest into start-ups", and its only deal found is from 2019, so code will
  exclude it. Three extractions are still running.

✻ Cogitated for 1s · done 3:53 PM

⏺ Agent "Extract odyssey-44" finished · 3m 17s

› Message from investor-extractor
  Written: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/rockaway-capital.json (src.validate passed).
  Evidence: 2 activity items dated within 24 months. Newest page date is
  2026-09-03: Wonderful, via United Founders, from Rockaway's own recap post.
  announced_date is null because that post recaps an earlier seed deal. The
  other item is Apptronik, 2026-02-13 (Lupa).
  Null: sectors, stages, ticket and capital (all not_published). The RockawayQ
  Digital Industry Holding SICAV fund entry has size null: E15 says about CZK
  0.5B initial plus a CZK 2B target, and I did not add them. I did not verify
  the hint's EUR 15M for United Founders or the CZK 2.5B fund.
  Borderline: this is the group holding (type private_holding), and deals run
  through subsidiaries that have their own records. Lupa attributes Apptronik to
  Rockaway Ventures, and its round participation is not explicit. The legal
  entity Rockaway GP a.s. (IČO 23278757) comes from the site imprint only, with
  no registry mirror checked (HQ is Praha 6, CZ). No exclusion signals.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-13,investor-extractor,sonnet,odyssey-44,33366,16,197.2,ok" >>
      data/runs/run_log.csv)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      81  2026-10-13,investor-extractor,sonnet,jsk-investments,45894,19,1
          10.4,ok
      82  2026-10-13,investor-extractor,sonnet,springtide-ventures,38118,
          22,105.5,ok
      83  2026-10-13,investor-extractor,sonnet,stredocesky-inovacni-centr
          um,36158,23,106.8,ok
      84 +2026-10-13,investor-extractor,sonnet,odyssey-44,33366,16,197.2,
         +ok                                                             

⏺ investor-extractor(Extract chilli-ventures)
  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)

⏺ Agent "Extract rockaway-capital" finished · 3m 17s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-13,investor-extractor,sonnet,rockaway-capital,36659,16,197.0,ok"
      >> data/runs/run_log.csv…)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      82  2026-10-13,investor-extractor,sonnet,springtide-ventures,38118,
          22,105.5,ok
      83  2026-10-13,investor-extractor,sonnet,stredocesky-inovacni-centr
          um,36158,23,106.8,ok
      84  2026-10-13,investor-extractor,sonnet,odyssey-44,33366,16,197.2,
          ok
      85 +2026-10-13,investor-extractor,sonnet,rockaway-capital,36659,16,
         +197.0,ok                                                       

⏺ investor-extractor(Extract tcf-capital)
  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)

⏺ Odyssey 44 and Rockaway Capital are logged and committed. Four extractions are
  running: Thein, Budeto, Chilli Ventures and TCF Capital. 13 queue rows remain
  after these.

✻ Cooked for 12s · done 3:53 PM

› Message from investor-extractor
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/thein.json; src.validate passed.
  - Evidence dated in the last 24 months: 0. The newest deal is Top Alulit,
  2024-01-16 (CzechCrunch). The only other item is Cotring and Železniční
  dodavatelská, 2021-06-10 (E15).
  - Fields left null: none, but the record has `funds=[]` and
  `exclusion_signals` is absent. Company websites are null. The ticket (EUR
  1-5m), the capital (EUR 40m "Volume of Funds Managed") and the sectors, stages
  and type all come from the undated CVCA member profile, which is
  self-reported.
  - Borderline:
    - www.thein.eu did not resolve (DNS error), so I could not read the
  investor's own site.
    - Thein is a PE-style group doing industrial buyouts (type `pe`), not VC.
    - The IČO 11733861 comes only from the Bloomberg LEI page (status LAPSED)
  and is not confirmed in ARES.
    - Search results say a Forbes.cz article reports that Thein Private Equity
  SICAV lost its fund status. The article is paywalled and undated, so I
  recorded it only in `meta.notes`.
    - There is no recent deal, so the record is likely dormant.

⏺ Thein is done. It's a private-equity buyout group, not VC, and its newest deal
  is from January 2024, outside the window. Code will exclude it. Three
  extractions are still running.

✻ Baked for 1s · done 3:54 PM

⏺ Agent "Extract thein" finished · 1m 24s

› Message from investor-extractor
  Written: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/chilli-ventures.json (src.validate passed).
  Evidence dated within 24 months: 1 (DecisionRules EUR 1.6M round, participant,
  newest 2025-05-06, from the company's own page).
  Null fields: sectors (not_published), capital (not_published), funds (empty).
  Borderline: the Modeinspect deal (PitchBook dates it 2025-12-04) has no dated
  primary or media source, so I left it out. The site also lists LP stakes in VC
  and PE funds, but it makes direct pre-seed and seed investments with a
  typical ticket of EUR 200-600k. The legal entity (IČO 04106059) comes from the
  kurzy.cz mirror (tier 3).

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-13,investor-extractor,sonnet,thein,37142,19,83.7,ok" >>
      data/runs/run_log.csv)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      83  2026-10-13,investor-extractor,sonnet,stredocesky-inovacni-centr
          um,36158,23,106.8,ok
      84  2026-10-13,investor-extractor,sonnet,odyssey-44,33366,16,197.2,
          ok
      85  2026-10-13,investor-extractor,sonnet,rockaway-capital,36659,16,
          197.0,ok
      86 +2026-10-13,investor-extractor,sonnet,thein,37142,19,83.7,ok    

⏺ investor-extractor(Extract bpd-partners)
  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)

⏺ Agent "Extract chilli-ventures" finished · 1m 2s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-13,investor-extractor,sonnet,chilli-ventures,31917,14,62.1,ok" >>
      data/runs/run_log.csv &&…)  ⎿  Updated data/runs/run_log.csv (+1 -0)
      84  2026-10-13,investor-extractor,sonnet,odyssey-44,33366,16,197.2,
          ok
      85  2026-10-13,investor-extractor,sonnet,rockaway-capital,36659,16,
          197.0,ok
      86  2026-10-13,investor-extractor,sonnet,thein,37142,19,83.7,ok
      87 +2026-10-13,investor-extractor,sonnet,chilli-ventures,31917,14,6
         +2.1,ok                                                         

⏺ investor-extractor(Extract grouport-ventures)
  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)

⏺ Thein and Chilli Ventures are logged and committed. Four extractions are
  running: Budeto, TCF Capital, BPD Partners and Grouport Ventures. 11 queue
  rows remain after these.

✻ Baked for 12s · done 3:54 PM

› Message from investor-extractor
  Written /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/budeto.json, and src.validate passed.
  - One evidence item, dated within the last 24 months. It is the Vetstor round,
  with CzechCrunch dated 2025-12-09 as the source and the newest date.
  - Left null: website, hq_country, legal_entities (empty list), type, sectors,
  stages, ticket, capital, funds.
  - Borderline: Budeto is a self-described startup studio, not a fund, so type
  is null with the note "not_applicable". I found no own website and no
  confirmed legal entity or country. BUDETO Learning s.r.o. (IČO 24087602,
  formed 2025-12-18) appeared only on a mirror, so I did not record it. Budeto's
  role and the instrument in the Vetstor round are not stated, so I set role to
  participant and instrument to unknown. The Langtail page says Budeto
  "co-founded and supported" the company but doesn't describe an investment, so
  I left Langtail out.

⏺ Budeto is done. It describes itself as a startup studio, not a fund, so its
  type and country are left empty. It has one dated deal in the window (Vetstor,
  Dec 2025). Three extractions are still running.

✻ Sautéed for 1s · done 3:55 PM

⏺ Agent "Extract budeto" finished · 1m 42s

› Message from investor-extractor
  - Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/tcf-capital.json; src.validate passed.
  - Evidence items dated within the last 24 months (to 2026-10-11): 0. Newest is
  Eco-Stations, 2024-07-26 (Newstream), about 26 months old. Second is Keboola
  Series A, 2023-12-01 (Tech.eu).
  - Left null: website, hq_country, stages, ticket. legal_entities and funds are
  empty (no IČO found), and exclusion_signals is empty. Capital is reported_aum
  EUR 720M, but that is from June 2023.
  - Borderline: TCF Capital is a family holding and investment group of Tomáš
  Čupr (type private_holding, main asset Rohlik Group), not a classic VC. The
  newest deal is a bit over 24 months old (the Eco-Stations quote has no
  explicit role), and I found no 2025-2026 deal. The Pilulka deal (Jul 2024) is
  a loan with a control-stake option, so I did not use it as equity evidence.
  The Eco-Stations ticket was left unused. The 720M figure and the sector
  mapping come from a single June 2023 E15 article.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-13,investor-extractor,sonnet,budeto,35112,21,101.7,ok" >>
      data/runs/run_log.csv)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      85  2026-10-13,investor-extractor,sonnet,rockaway-capital,36659,16,
          197.0,ok
      86  2026-10-13,investor-extractor,sonnet,thein,37142,19,83.7,ok
      87  2026-10-13,investor-extractor,sonnet,chilli-ventures,31917,14,6
          2.1,ok
      88 +2026-10-13,investor-extractor,sonnet,budeto,35112,21,101.7,ok  

⏺ investor-extractor(Extract ip-lab-ventures)
  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)

⏺ Agent "Extract tcf-capital" finished · 1m 16s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-13,investor-extractor,sonnet,tcf-capital,34282,20,76.0,ok" >>
      data/runs/run_log.csv && git…)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      86  2026-10-13,investor-extractor,sonnet,thein,37142,19,83.7,ok
      87  2026-10-13,investor-extractor,sonnet,chilli-ventures,31917,14,6
          2.1,ok
      88  2026-10-13,investor-extractor,sonnet,budeto,35112,21,101.7,ok
      89 +2026-10-13,investor-extractor,sonnet,tcf-capital,34282,20,76.0,
         +ok                                                             

⏺ investor-extractor(Extract kaya-vc)
  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)

⏺ Budeto and TCF Capital are done and committed. TCF Capital's newest deal is
  from July 2024, just outside the 24-month window. Four extractions are
  running: BPD Partners, Grouport Ventures, IP Lab Ventures and KAYA VC. Nine
  queue rows remain after these.

✻ Worked for 13s · done 3:55 PM

› Message from investor-extractor
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/grouport-ventures.json. `src.validate` passed.
  Evidence dated within 24 months: 0. The only deal is Augmented Robotics seed,
  2022-07-07, from a Tech.eu table. That is outside the window.
  Left null: website, hq_country, legal_entities (empty), type, sectors, stages,
  ticket, capital, funds.
  Borderline: no official site or registry entry found (grouport.cz and
  grouport.com don't resolve or are empty), so I added a `not_found_or_defunct`
  signal. Prague, a 2019 founding and the other portfolio names (Beem, Oxus.AI)
  appear only on aggregator pages.
  Borderline: the one deal's cited page spells the name "Gruport Ventures", and
  the 2022-07-07 date comes from a Tech.eu table and is not in the quote.
  Identity rests on aggregators (CB Insights, VCBacked) listing "Grouport" for
  the same round. The investee, Augmented Robotics, is Berlin-based. The deal is
  likely dormant at best, and the caveats are in `meta.notes`.

⏺ Grouport Ventures is done. No official site or registry entry was found, and
  its only deal is from 2022, so the agent flagged it as defunct and code will
  exclude it. Three extractions are still running.

✻ Sautéed for 2s · done 3:55 PM

⏺ Agent "Extract grouport-ventures" finished · 44s

› Message from investor-extractor
  Written: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/bpd-partners.json. `src.validate` passed (1/1
  valid).
  - Evidence: 0 activity items are dated within the last 24 months. The only
  dated deal is the Powerful Medical seed round, announced 2022-09-28 (company
  blog; cc.cz of 30.9.2022 corroborates), so the newest date is 2022-09-28.
  - Left null: website, stages, ticket, capital. Funds is empty.
  - Borderline: bpd partners a.s. (IČO 27342875, Praha) is a family office, not
  a classic VC. The dormant outcome is likely. Its hq_country=CZ comes from the
  registered seat on the finmag mirror (tier 3), because no team location is
  published.
  - Borderline: the e15 and finmag sources for type, sectors and legal entity
  are secondary. The e15 article has published_date null. I did not record the
  2025 Taveren Therapeutics deal because the source names BTCZ Ventures ("part
  of BPD Partners Group"), not bpd partners. The CB Insights entry for a 2024
  deal is an aggregator and I did not use it. The details are in meta.notes.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-13,investor-extractor,sonnet,grouport-ventures,28811,13,44.1,ok"
      >> data/runs/run_log.csv;…)
  ⎿  9 remaining
     {"candidate_id": "pilulka-lab", "name": "Pilulka Lab", "webs
     {"candidate_id": "y-soft-ventures", "name": "Y Soft Ventures
     … +7 lines (ctrl+o to expand)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      87  2026-10-13,investor-extractor,sonnet,chilli-ventures,31917,14,6
          2.1,ok
      88  2026-10-13,investor-extractor,sonnet,budeto,35112,21,101.7,ok
      89  2026-10-13,investor-extractor,sonnet,tcf-capital,34282,20,76.0,
          ok
      90 +2026-10-13,investor-extractor,sonnet,grouport-ventures,28811,13
         +,44.1,ok                                                       

⏺ Agent "Extract bpd-partners" finished · 1m 13s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-13,investor-extractor,sonnet,bpd-partners,35015,16,73.4,ok" >>
      data/runs/run_log.csv && gi…)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      88  2026-10-13,investor-extractor,sonnet,budeto,35112,21,101.7,ok
      89  2026-10-13,investor-extractor,sonnet,tcf-capital,34282,20,76.0,
          ok
      90  2026-10-13,investor-extractor,sonnet,grouport-ventures,28811,13
          ,44.1,ok
      91 +2026-10-13,investor-extractor,sonnet,bpd-partners,35015,16,73.4
         +,ok                                                            

⏺ 2 background agents launched (↓ to manage)
   ├ Extract pilulka-lab
   └ Extract y-soft-ventures

› Message from investor-extractor
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/kaya-vc.json. `src.validate` passed (1/1 valid).
  - 2 evidence items are dated within the last 24 months. They are Viktor Series
  A (2026-05-19, Fortune, Kaya a participant) and E2B Series A (2025-07-28,
  Insight Partners, Kaya a participant). The newest is 2026-05-19.
  - Left null: `sectors.value` (the investor's wording "digital, physical, and
  consumer economies" does not map to the taxonomy). `legal_entities` is empty:
  the site names no entity, ARES returned only namesakes, and I could not
  confirm any registered entity.
  - Also not confirmed from dated sources: TopK, the E2B seed and Upheal from
  the hint. The fund name and vintage are null.
  - Borderline: nothing excluding. `hq_country` CZ rests on the Prague address
  among four offices (Warsaw, Prague, San Francisco, London). The website
  figures are undated and self-reported: $500M AUM, $85M current fund, $1–3M
  ticket. The Fortune quote may not match the page text, so check it with
  `check_quotes`.

⏺ Agent "Extract kaya-vc" finished · 50s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-13,investor-extractor,sonnet,kaya-vc,36380,14,51.0,ok" >>
      data/runs/run_log.csv)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      89  2026-10-13,investor-extractor,sonnet,tcf-capital,34282,20,76.0,
          ok
      90  2026-10-13,investor-extractor,sonnet,grouport-ventures,28811,13
          ,44.1,ok
      91  2026-10-13,investor-extractor,sonnet,bpd-partners,35015,16,73.4
          ,ok
      92 +2026-10-13,investor-extractor,sonnet,kaya-vc,36380,14,51.0,ok  

⏺ investor-extractor(Extract 3ts-capital-partners)
  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)

⏺ KAYA VC and BPD Partners are done and logged. KAYA has 2 dated deals in the
  window, the newest in May 2026; BPD's newest deal is from 2022, so it is
  likely dormant. Four extractions are running: IP Lab Ventures, Pilulka Lab, Y
  Soft Ventures and 3TS Capital Partners. After them, 6 rows remain.

✻ Cogitated for 18s · done 3:56 PM
› Message from investor-extractor
  - Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/ip-lab-ventures.json. src.validate passed.
  - Evidence items dated within the last 24 months: 0 in evidence_of_activity.
  The only deal item is MendelFOLD, with announced_date null, taken from the
  Lupa article dated 2026-09-23. The newest dated source is that article. Quotes
  are from the WebFetch model's output and were not re-checked against the raw
  page.
  - Fields left null: website (iplabventures.com is a parked domain),
  hq_country, legal_entities (no IČO found), stages, capital. Ticket is max EUR
  1M only, with no minimum. Sector mapping to ai_data, deeptech_hardware and
  health_biotech is my own, from Lupa's wording.
  - Borderline: the fund is brand new (EIF mandate from the Czech National
  Recovery Plan, about CZK 656m, announced 2026-09-23). Fund size is a target of
  EUR 40M, "až 40 milionů eur". It describes itself as a venture builder for
  university spin-offs. No dated investment was found, and the MendelFOLD role
  and instrument are unclear. The Private Equity International profile says the
  team is in Prague, but it is an aggregator, so I did not use it.

⏺ IP Lab Ventures is done. It's a brand-new fund announced 2026-09-23 with no
  dated investment yet. It's a borderline new-fund case: it counts as active
  only if code treats that announcement as a fund close within 12 months. Three
  extractions are still running.

✻ Churned for 2s · done 3:56 PM

⏺ Agent "Extract ip-lab-ventures" finished · 1m 17s

› Message from investor-extractor
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/pilulka-lab.json, and src.validate passed.
  - Evidence within 24 months: 1 item, dated 2024-03-22 (Carebot round,
  CzechCrunch). That is about 31 months before AS_OF, so it falls outside the
  24-month window, not inside it. The other item is Carebot on 2021-12-06.
  - Fields left null: website, hq_country, legal_entities (empty list), sectors,
  stages, ticket, capital, funds (empty list).
  - Borderline: Pilulka Lab is a corporate accelerator (Pilulka plus
  StartupYard) that takes equity stakes, and its only found deal is Carebot. The
  role in the 2024 round is "participant". The domain pilulkalab.cz
  301-redirects to startupyard.com, which doesn't mention Pilulka Lab. I
  recorded a `not_found_or_defunct` signal with no source. No IČO or registry
  entry was confirmed, though a PSE document mentions a Pilulka Lab s.r.o.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-13,investor-extractor,sonnet,ip-lab-ventures,32162,16,77.3,ok" >>
      data/runs/run_log.csv)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      90  2026-10-13,investor-extractor,sonnet,grouport-ventures,28811,13
          ,44.1,ok
      91  2026-10-13,investor-extractor,sonnet,bpd-partners,35015,16,73.4
          ,ok
      92  2026-10-13,investor-extractor,sonnet,kaya-vc,36380,14,51.0,ok
      93 +2026-10-13,investor-extractor,sonnet,ip-lab-ventures,32162,16,7
         +7.3,ok                                                         

⏺ investor-extractor(Extract 500-emerging-europe)
  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)

⏺ Agent "Extract pilulka-lab" finished · 51s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-13,investor-extractor,sonnet,pilulka-lab,28183,12,51.6,ok" >>
      data/runs/run_log.csv && git…)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      91  2026-10-13,investor-extractor,sonnet,bpd-partners,35015,16,73.4
          ,ok
      92  2026-10-13,investor-extractor,sonnet,kaya-vc,36380,14,51.0,ok
      93  2026-10-13,investor-extractor,sonnet,ip-lab-ventures,32162,16,7
          7.3,ok
      94 +2026-10-13,investor-extractor,sonnet,pilulka-lab,28183,12,51.6,
         +ok                                                             

⏺ investor-extractor(Extract alpha-intelligence-capital)
  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)

⏺ IP Lab Ventures, KAYA VC and Pilulka Lab are committed. Four extractions are
  running: Y Soft Ventures, 3TS Capital Partners, 500 Emerging Europe and Alpha
  Intelligence Capital. Four queue rows remain after these.

✻ Churned for 13s · done 3:57 PM

› Message from investor-extractor
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/3ts-capital-partners.json. src.validate passed
  (1/1 valid).
  Evidence: 2 items within 24 months, newest is Tiger Technology (source dated
  2026-09-15; announced_date null) and Patronus (2026-04-05).
  Null fields: ticket (only round sizes of EUR 5-20M published), capital (no AUM
  stated), Tiger announced_date.
  Borderline:
  - Team is in Helsinki and Vienna, not Czechia, so hq_country is FI (out of
  scope geography).
  - 3TS calls itself an investment "adviser" to the TCEE funds. I recorded it as
  a growth VC manager and added no exclusion signal.
  - 3tscapital.com is JS-rendered, so its quotes may fail check_quotes.
  - The Y-tunnus 1505569-6 comes from the Fonecta directory, not the official
  register. The Heuking date "05-04-2026" is read as 5 April, which I could not
  confirm. The Tiger article is a tier-3 aggregator.

⏺ 3TS Capital Partners is done. Its team sits in Helsinki and Vienna (hq_country
  FI), so code will exclude it as out of scope by geography. Three extractions
  are still running.

✻ Sautéed for 1s · done 3:58 PM

⏺ Agent "Extract 3ts-capital-partners" finished · 1m 40s

› Message from investor-extractor
  - Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/y-soft-ventures.json. `src.validate` passed
  (1/1). I accidentally ran the whole `src.check_quotes` over all records, which
  created untracked `data/quote_checks/`. All 7 quotes for this record came
  back "found".
  - 1 evidence item within 24 months, the newest dated 2025-07-02. It is the
  RoboTwin pre-seed, sourced from EIT Jumpstarter (tier 3), role participant.
  Older deals (Dronetag, NenoVision 2019) have no usable dated source; the
  Dronetag article returned 403.
  - Left null: ticket and capital (not_published). `funds` is empty: the 2014
  Lupa interview only gives plans, not a fund size or close. The Lupa 2026-04
  claim that Miloš Sochor co-leads JIC Ventures was not verified.
  - Borderline:
    - Type is cvc, the venture arm of Y Soft Corporation, based in Brno.
    - Legal entities are Y Soft Ventures, a.s. (IČO 29314445) and Y Soft
  Ventures II, a.s. (IČO 07890150). Both come from mesec.cz, a tier-3 mirror of
  the register.
    - The II entity's registered activity is real-estate rental, which is odd
  for a fund vehicle.
    - Sector and stage mappings are coarse. The site says only "early-stage" and
  IoT/B2B tech.
    - There is a single recent deal, and the pages on ysoft.com/ventures are
  undated.
    - A search lead (WaveUp, not used as evidence) reports a leadership change
  on 2025-07-01: Lukáš Konečný became Managing Partner, with Sochor staying on
  as Venture Partner.

⏺ The Y Soft Ventures extractor ran src.check_quotes over all records, which is
  outside its job. Some records may still have been mid-write, so I'll delete
  that output and run R5 cleanly once extraction is done. I'm logging it as AI
  error E-16.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && ls
      data/quote_checks | wc -l; rm -rf data/quote_checks; printf '%s\n'
      "2026-10-13,investor-extractor,son…)
  ⎿  62
  ⎿  Deleted data/quote_checks/aspire11.json (+0 -89)
       1 -{                                                              
       2 -  "id": "aspire11",                                            
       3 -  "checked_at": "2026-10-13T13:58:07+00:00",                   
       4 -  "items": [                                                   
       5 -    {                                                          
       6 -      "path": "hq_country",                                    
       7 -      "url": "https://www.lupa.cz/aktuality/cesi-jsou-ve-velke-
         -investorske-lize-penize-posilaji-do-revolutu/",                
       8 -      "status": "found",                                       
       9 -      "score": 100,                                            
      10 -      "http_status": 200,                                      
      11 -      "note": ""                                               
      12 -    },                                                         
      13 -    {                                                          
      14 -      "path": "legal_entities[0]",                             
      15 -      "url": "https://www.aspire11cap.com/legal",              
      16 -      "status": "found",                                       
      17 -      "score": 100,                                            
      18 -      "http_status": 200,                                      
      19 -      "note": ""                                               
      20 -    },                                                         
      21 -    {                                                          
      22 -      "path": "legal_entities[1]",                             
      23 -      "url": "https://www.aspire11cap.com/legal",              
      24 -      "status": "found",                                       
      25 -      "score": 100,                                            
      26 -      "http_status": 200,                                      
      27 -      "note": ""                                               
      28 -    },                                                         
      29 -    {                                                          
      30 -      "path": "type",                                          
      31 -      "url": "https://www.aspire11cap.com",                    
      32 -      "status": "found",                                       
      33 -      "score": 100,                                            
      34 -      "http_status": 200,                                      
      35 -      "note": ""                                               
      36 -    },                                                         
      37 -    {                                                          
      38 -      "path": "sectors",                                       
      39 -      "url": "https://www.aspire11cap.com",                    
      40 -      "status": "found",                                       
     … 49 more lines (ctrl+o to expand)
  ⎿  Deleted data/quote_checks/aternus-family-office.json (+0 -57)
       1 -{                                                              
       2 -  "id": "aternus-family-office",                               
       3 -  "checked_at": "2026-10-13T13:58:07+00:00",                   
       4 -  "items": [                                                   
       5 -    {                                                          
       6 -      "path": "hq_country",                                    
       7 -      "url": "https://www.aternus.cz/cz/",                     
       8 -      "status": "found",                                       
       9 -      "score": 100,                                            
      10 -      "http_status": 200,                                      
      11 -      "note": ""                                               
      12 -    },                                                         
      13 -    {                                                          
      14 -      "path": "legal_entities[0]",                             
      15 -      "url": "https://www.podnikatel.cz/rejstrik/aternus-a-s-25
         -865056/",                                                      
      16 -      "status": "found",                                       
      17 -      "score": 100,                                            
      18 -      "http_status": 200,                                      
      19 -      "note": ""                                               
      20 -    },                                                         
      21 -    {                                                          
      22 -      "path": "type",                                          
      23 -      "url": "https://www.aternus.cz/cz/",                     
      24 -      "status": "found",                                       
      25 -      "score": 100,                                            
      26 -      "http_status": 200,                                      
      27 -      "note": ""                                               
      28 -    },                                                         
      29 -    {                                                          
      30 -      "path": "sectors",                                       
      31 -      "url": "https://www.aternus.cz/cz/",                     
      32 -      "status": "found",                                       
      33 -      "score": 100,                                            
      34 -      "http_status": 200,                                      
      35 -      "note": ""                                               
      36 -    },                                                         
      37 -    {                                                          
      38 -      "path": "evidence_of_activity[0]",                       
      39 -      "url": "https://tech.eu/2025/12/16/jutro-medical-extends-
         -series-a-to-eur36m-for-ai-enabled-primary-care-scale/",        
      40 -      "status": "found",                                       
     … 17 more lines (ctrl+o to expand)
  ⎿  Deleted data/quote_checks/bd-partners.json (+0 -57)
       1 -{                                                              
       2 -  "id": "bd-partners",                                         
       3 -  "checked_at": "2026-10-13T13:58:07+00:00",                   
       4 -  "items": [                                                   
       5 -    {                                                          
       6 -      "path": "hq_country",                                    
       7 -      "url": "https://www.finmag.cz/obchodni-rejstrik/ares/1928
         -6511-bd-partners-a-s",                                         
       8 -      "status": "found",                                       
       9 -      "score": 100,                                            
      10 -      "http_status": 200,                                      
      11 -      "note": ""                                               
      12 -    },                                                         
      13 -    {                                                          
      14 -      "path": "legal_entities[0]",                             
      15 -      "url": "https://www.finmag.cz/obchodni-rejstrik/ares/1928
         -6511-bd-partners-a-s",                                         
      16 -      "status": "found",                                       
      17 -      "score": 100,                                            
      18 -      "http_status": 200,                                      
      19 -      "note": ""                                               
      20 -    },                                                         
      21 -    {                                                          
      22 -      "path": "type",                                          
      23 -      "url": "https://cc.cz/sefoval-ppf-ted-investuje-do-startu
         -pu-vina-i-betonu-mame-na-to-az-25-miliardy-rika-bartonicek/",  
      24 -      "status": "found",                                       
      25 -      "score": 100,                                            
      26 -      "http_status": 200,                                      
      27 -      "note": ""                                               
      28 -    },                                                         
      29 -    {                                                          
      30 -      "path": "sectors",                                       
      31 -      "url": "https://cc.cz/sefoval-ppf-ted-investuje-do-startu
         -pu-vina-i-betonu-mame-na-to-az-25-miliardy-rika-bartonicek/",  
      32 -      "status": "found",                                       
      33 -      "score": 100,                                            
      34 -      "http_status": 200,                                      
      35 -      "note": ""                                               
      36 -    },                                                         
      37 -    {                                                          
      38 -      "path": "evidence_of_activity[0]",                       
      39 -      "url": "https://www.lupa.cz/aktuality/cesky-startup-byval
         -eho-inzenyra-v-nvidii-a-googlu-ziskal-160-milionu-na-ai-pro-zvl
         -adani-byrokracie/",                                            
      40 -      "status": "found",                                       
     … 17 more lines (ctrl+o to expand)
  ⎿  Deleted data/quote_checks/bpd-partners.json (+0 -49)
       1 -{                                                              
       2 -  "id": "bpd-partners",                                        
       3 -  "checked_at": "2026-10-13T13:58:07+00:00",                   
       4 -  "items": [                                                   
       5 -    {                                                          
       6 -      "path": "hq_country",                                    
       7 -      "url": "https://www.finmag.cz/obchodni-rejstrik/27342875-
         -bpd-partners-a-s",                                             
       8 -      "status": "found",                                       
       9 -      "score": 100,                                            
      10 -      "http_status": 200,                                      
      11 -      "note": ""                                               
      12 -    },                                                         
      13 -    {                                                          
      14 -      "path": "legal_entities[0]",                             
      15 -      "url": "https://www.finmag.cz/obchodni-rejstrik/27342875-
         -bpd-partners-a-s",                                             
      16 -      "status": "found",                                       
      17 -      "score": 100,                                            
      18 -      "http_status": 200,                                      
      19 -      "note": ""                                               
      20 -    },                                                         
      21 -    {                                                          
      22 -      "path": "type",                                          
      23 -      "url": "https://www.e15.cz/byznys/obchod-a-sluzby/zdravot
         -ni-pece-zlakala-dalsi-miliardare-investuji-do-ni-bpd-partners-1
         -378560",                                                       
      24 -      "status": "found",                                       
      25 -      "score": 100,                                            
      26 -      "http_status": 200,                                      
      27 -      "note": ""                                               
      28 -    },                                                         
      29 -    {                                                          
      30 -      "path": "sectors",                                       
      31 -      "url": "https://www.e15.cz/byznys/obchod-a-sluzby/zdravot
         -ni-pece-zlakala-dalsi-miliardare-investuji-do-ni-bpd-partners-1
         -378560",                                                       
      32 -      "status": "found",                                       
      33 -      "score": 100,                                            
      34 -      "http_status": 200,                                      
      35 -      "note": ""                                               
      36 -    },                                                         
      37 -    {                                                          
      38 -      "path": "evidence_of_activity[0]",                       
      39 -      "url": "https://www.powerfulmedical.com/blog/powerful-med
         -ical-raises-6-million-eur-in-seed-funding/",                   
      40 -      "status": "found",                                       
     … 9 more lines (ctrl+o to expand)
  ⎿  Deleted data/quote_checks/braiins.json (+0 -25)
       1 -{                                                              
       2 -  "id": "braiins",                                             
       3 -  "checked_at": "2026-10-13T13:58:07+00:00",                   
       4 -  "items": [                                                   
       5 -    {                                                          
       6 -      "path": "hq_country",                                    
       7 -      "url": "https://www.seznamzpravy.cz/clanek/ekonomika-fina
         -nce-byznys-meny-kryptomeny-cesky-braiins-rozsiruje-byznys-kupuj
         -e-newyorsky-komoditni-fond-306490",                            
       8 -      "status": "found",                                       
       9 -      "score": 100,                                            
      10 -      "http_status": 200,                                      
      11 -      "note": ""                                               
      12 -    },                                                         
      13 -    {                                                          
      14 -      "path": "evidence_of_activity[0]",                       
      15 -      "url": "https://braiins.com/blog/braiins-invests-in-bitco
         -in-backed-lending-platform-firefish-in-a-1-8m-seed-round",     
      16 -      "status": "found",                                       
      17 -      "score": 100,                                            
      18 -      "http_status": 200,                                      
      19 -      "note": ""                                               
      20 -    }                                                          
      21 -  ],                                                           
      22 -  "summary": {                                                 
      23 -    "found": 2                                                 
      24 -  }                                                            
      25 -}                                                              
  ⎿  … 59 more files changed
  ⎿  (another command ran in this repository at the same time; a change 
     made by either may show under either result)

⏺ Agent "Extract y-soft-ventures" finished · 1m 59s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-13,investor-extractor,sonnet,y-soft-ventures,34865,17,118.7,ok"
      >> data/runs/run_log.csv &…)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      93  2026-10-13,investor-extractor,sonnet,ip-lab-ventures,32162,16,7
          7.3,ok
      94  2026-10-13,investor-extractor,sonnet,pilulka-lab,28183,12,51.6,
          ok
      95  2026-10-13,investor-extractor,sonnet,3ts-capital-partners,35412
          ,24,99.5,ok
      96 +2026-10-13,investor-extractor,sonnet,y-soft-ventures,34865,17,1
         +18.7,ok                                                        
  ⎿  (another command ran in this repository at the same time; a change 
     made by either may show under either result)

⏺ 2 background agents launched (↓ to manage)
   ├ Extract badideas-fund
   └ Extract borovicka-capital

› Message from investor-extractor
  - Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/alpha-intelligence-capital.json; src.validate
  passed.
  - 1 evidence item within 24 months: Waiv, announced 2026-03-19, co_lead, tier
  3 (McDermott Will & Schulte).
  - Null fields: website, hq_country (conflicting_sources), legal_entities
  (empty), ticket and capital (not_published). The fund size comes from a 2023
  article.
  - Borderline: the team looks non-Czech, with offices in the US, France, UAE
  and Singapore per Maddyness 2023, and other directories give San
  Francisco/Paris/Singapore or Luxembourg. The Photoneo link is Slovak. The only
  website guess, aic.group, is a parked domain. The Waiv round is labelled
  Series A by McDermott and seed by Nordic9, and McDermott names five co-leads.
  All sources are tier 3.

⏺ Agent "Extract alpha-intelligence-capital" finished · 1m 13s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo "2026-10-13,
      investor-extractor,sonnet,alpha-intelligence-capital,31045,16,73.0,ok" >>
      data/runs/run…)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      94  2026-10-13,investor-extractor,sonnet,pilulka-lab,28183,12,51.6,
          ok
      95  2026-10-13,investor-extractor,sonnet,3ts-capital-partners,35412
          ,24,99.5,ok
      96  2026-10-13,investor-extractor,sonnet,y-soft-ventures,34865,17,1
          18.7,ok
      97 +2026-10-13,investor-extractor,sonnet,alpha-intelligence-capital
         +,31045,16,73.0,ok                                              
  ⎿  (another command ran in this repository at the same time; a change 
     made by either may show under either result)

⏺ 2 background agents launched (↓ to manage)
   ├ Extract diaspora-ventures
   └ Extract eic-fund

⏺ The last four extractions are now running: BADideas.fund, Borovička Capital,
  Diaspora Ventures and EIC Fund. 500 Emerging Europe is also still in progress.
  Once these five finish, I'll move on to validation, quote checks and
  verification.

✻ Crunched for 27s · done 3:58 PM

› Message from investor-extractor
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/diaspora-ventures.json, and src.validate passed.
  - Evidence items dated within the last 24 months: 0. evidence_of_activity is
  empty. The only lead is an aggregator (CB Insights) listing DiffuseDrive, May
  2025. Dealroom and funding.tech name other investors for that round, so I did
  not use it.
  - Fields left null: sectors (homepage says only "tech"), capital,
  legal_entities (empty), funds (empty). The newest dated source I cite is
  TechCrunch, 2020-07-21.
  - Borderline: the team looks US-based (hq_country US), per TechCrunch 2020.
  Aggregators disagree (NY, SF, Paris). The fund backs European (mainly French)
  founders, and I found no Czech link. It is a pre-seed rolling fund, and no
  registry ID was found. The ticket (USD 100k–200k) comes from the 2020 article,
  not the fund's own site.

⏺ Diaspora Ventures is done. Its team looks US-based and it has no dated deals
  in the window, so code will exclude it. Four extractions are still running:
  500 Emerging Europe, BADideas.fund, Borovička Capital and EIC Fund.

✻ Cooked for 2s · done 3:59 PM

⏺ Agent "Extract diaspora-ventures" finished · 42s

› Message from investor-extractor
  - Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/borovicka-capital.json; src.validate passed.
  - Evidence items dated within the last 24 months: 1 (Outfindo, Czech Crunch,
  2025-01-20), which is also the newest.
  - Left null: hq_country (not_found), sectors, stages, ticket and capital (all
  not_published). legal_entities and funds are empty, because I found no ICO or
  imprint.
  - Borderline: HQ is unverified, and the aggregator claim "Prague" is not
  usable as evidence. It is a family fund with a thin website, and I found only
  one dated deal. The `type` quote comes from the homepage description (it
  appears in a meta tag), so check_quotes may flag it as weak.
⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-13,investor-extractor,sonnet,diaspora-ventures,27264,8,42.3,ok"
      >> data/runs/run_log.csv)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      95  2026-10-13,investor-extractor,sonnet,3ts-capital-partners,35412
          ,24,99.5,ok
      96  2026-10-13,investor-extractor,sonnet,y-soft-ventures,34865,17,1
          18.7,ok
      97  2026-10-13,investor-extractor,sonnet,alpha-intelligence-capital
          ,31045,16,73.0,ok
      98 +2026-10-13,investor-extractor,sonnet,diaspora-ventures,27264,8,
         +42.3,ok                                                        
  ⎿  (another command ran in this repository at the same time; a change 
     made by either may show under either result)

⏺ Agent "Extract borovicka-capital" finished · 56s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-13,investor-extractor,sonnet,borovicka-capital,28086,12,56.7,ok"
      >> data/runs/run_log.csv…)
  ⎿  hint: See the 'Note about fast-forwards' in 'git push --help' for deta
     ils.
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      96  2026-10-13,investor-extractor,sonnet,y-soft-ventures,34865,17,1
          18.7,ok
      97  2026-10-13,investor-extractor,sonnet,alpha-intelligence-capital
          ,31045,16,73.0,ok
      98  2026-10-13,investor-extractor,sonnet,diaspora-ventures,27264,8,
          42.3,ok
      99 +2026-10-13,investor-extractor,sonnet,borovicka-capital,28086,12
         +,56.7,ok                                                       
  ⎿  (another command ran in this repository at the same time; a change 
     made by either may show under either result)

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && git fetch -q &&
      git log --oneline HEAD..origin/main && git diff --stat HEAD...origin/main
      && git pull -q…)
  ⎿  726579c Fix formatting in PLAN.md
      PLAN.md | 2 +-
      1 file changed, 1 insertion(+), 1 deletion(-)
  ⎿  Updated PLAN.md (+1 -1)
  ⎿  (a git step in this command can move the working tree, so these may be
     its changes, not edits) (ctrl+o to expand)
  ⎿  (another command ran in this repository at the same time; a change 
     made by either may show under either result)

⏺ Borovička Capital and Diaspora Ventures are committed. The remote had your
  one-line formatting fix in PLAN.md; I merged it and pushed. Three extractions
  are still running: 500 Emerging Europe, BADideas.fund and EIC Fund.

✻ Cooked for 14s · done 3:59 PM

› Message from investor-extractor
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/badideas-fund.json. src.validate passed (1/1
  valid).
  - Evidence: 1 item (Tapaya, Czechia). Its announced_date is null, so 0 items
  carry a date within 24 months. The portfolio page prints only "Apr 2026", and
  tech.eu showed 2026-04-28 but I couldn't verify its investor list in the page
  HTML, so I didn't cite it.
  - Fields left null: capital (conflicting_sources: EUR 22M on the firm page vs
  EUR 20.67M on the ALTUM page), legal_entities (empty; the site names no entity
  or registration number), and announced_date, round, role and instrument on
  the activity item.
  - Borderline: this is a Latvian fund, not Czech. It is a Latvian AIF anchored
  by ALTUM, with its manager registered with the Bank of Latvia. hq_country is
  LV, and the site's structured data gives Riga. Czech involvement is limited to
  the portfolio company Tapaya. The quote for the "Tapaya" activity item is
  just the company name from the portfolio page, so it may only get a weak
  quote-check result. The record has no exclusion signals; the only portfolio
  dates are month-level.

⏺ BADideas.fund is done. It's a Latvian fund (team in Riga), so code will
  exclude it as out of scope by geography. 500 Emerging Europe and EIC Fund are
  still running.

✻ Brewed for 1s · done 3:59 PM

⏺ Agent "Extract badideas-fund" finished · 1m 17s

› Message from investor-extractor
  - Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/eic-fund.json. src.validate passed (1/1 valid).
  - 1 evidence item is within the last 24 months: eleQtron Series A, 2026-05-05,
  tech.eu, participant. The other item is Sensoneo Series A, 2023-06-19, which
  is outside the window.
  - Fields left null: stages and ticket (both not_published). legal_entities and
  funds are empty lists.
  - Borderline:
    - EIC Fund is a European Commission-financed public equity vehicle, not a
  Czech VC, and I found no registry entry.
    - hq_country is LU. This rests only on a 2022 DZS article saying the
  external manager (Alter Domus) is Luxembourg-based, so it is weak and tier 3.
    - Ticket: EUR 10-30m is stated only for the STEP Scale Up scheme, so I did
  not record it.
    - Capital: EUR 4bn is the EIC's own "capitalisation" wording. I recorded it
  as reported_aum, which is arguably not AUM.
    - Quotes: the eleQtron, Sensoneo, hq_country and sectors quotes came through
  WebFetch summaries, so they may be weak or missing in check_quotes. The
  Sensoneo and eleQtron quotes are partial clauses.
    - The Microamp June 2026 deal appeared only on aggregators, so I left it
  out.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-13,investor-extractor,sonnet,badideas-fund,36509,15,77.3,ok" >>
      data/runs/run_log.csv)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
       97  2026-10-13,investor-extractor,sonnet,alpha-intelligence-capita
           l,31045,16,73.0,ok
       98  2026-10-13,investor-extractor,sonnet,diaspora-ventures,27264,8
           ,42.3,ok
       99  2026-10-13,investor-extractor,sonnet,borovicka-capital,28086,1
           2,56.7,ok
      100 +2026-10-13,investor-extractor,sonnet,badideas-fund,36509,15,77
          +.3,ok                                                         
  ⎿  (another command ran in this repository at the same time; a change 
     made by either may show under either result)

⏺ Agent "Extract eic-fund" finished · 1m 28s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-13,investor-extractor,sonnet,eic-fund,36417,20,88.0,ok" >>
      data/runs/run_log.csv && git ad…)
  ⎿  1 remaining
     {"candidate_id": "500-emerging-europe", "name": "500 Emerging Europe",
      "website"
  ⎿  Updated data/runs/run_log.csv (+1 -0)
       98  2026-10-13,investor-extractor,sonnet,diaspora-ventures,27264,8
           ,42.3,ok
       99  2026-10-13,investor-extractor,sonnet,borovicka-capital,28086,1
           2,56.7,ok
      100  2026-10-13,investor-extractor,sonnet,badideas-fund,36509,15,77
           .3,ok
      101 +2026-10-13,investor-extractor,sonnet,eic-fund,36417,20,88.0,ok

⏺ Extraction is nearly done: 68 of 69 queued candidates have records. 500
  Emerging Europe is still running, and R4 validation follows once it finishes.

✻ Crunched for 11s · done 4:00 PM

› Message from investor-extractor
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/500-emerging-europe.json; src.validate passed.
  Evidence dated within 24 months: 1 deal (Mission Control Games, Tech.eu,
  2026-04-15, participant). The fund and profile sources are dated 2026-01-14
  (Vestbee).
  Null fields: legal_entities (empty, no imprint or registry entry found),
  capital (not_published), ticket min (only "up to $1 million" published),
  website company_website.
  Borderline: this is e2vc (formerly 500 Emerging Europe), not a Czech team.
  hq_country is TR, from Vestbee's "Turkey-based", but the same article lists
  offices in SF, NY and London, so it is not firmly established. Fund III close
  status "first" comes from the article headline/URL, and the quoted sentence
  says only "close". Only one dated deal was found. Mandel AI and Bold Games
  appeared only on aggregators, so I did not record them.

⏺ Extraction is complete: 69 of 69 queued candidates have staging records. I'm
  running R4 (validate) now.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-13,investor-extractor,sonnet,500-emerging-europe,,,,ok" >>
      data/runs/run_log.csv; ls data/…)
  ⎿  69

     69/69 valid
  ⎿  Updated data/runs/run_log.csv (+1 -0)
       99  2026-10-13,investor-extractor,sonnet,borovicka-capital,28086,1
           2,56.7,ok
      100  2026-10-13,investor-extractor,sonnet,badideas-fund,36509,15,77
           .3,ok
      101  2026-10-13,investor-extractor,sonnet,eic-fund,36417,20,88.0,ok
      102 +2026-10-13,investor-extractor,sonnet,500-emerging-europe,,,,ok

⏺ Agent "Extract 500-emerging-europe" finished · 3m 18s

⏺ All 69 are valid. Committing R3/R4, then starting R5, the quote check, which
  fetches every cited page.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && sed -i ''
      's/^2026-10-13,investor-extractor,sonnet,500-emerging-europe,,,,ok$/2026-1
      0-13,investor-extrac…)
  ⎿  69 records, 237 unique URLs; fetching (cache: /Users/davidkoktavy/Desk
     top/Investor DB Starter/data/raw)
     3ts-capital-partners                     {'found': 8}
     … +13 lines (ctrl+o to expand)
  ⎿  Created data/quote_checks/3ts-capital-partners.json (+73 -0)
       1 +{                                                              
       2 +  "id": "3ts-capital-partners",                                
       3 +  "checked_at": "2026-10-13T14:01:14+00:00",                   
       4 +  "items": [                                                   
       5 +    {                                                          
       6 +      "path": "hq_country",                                    
       7 +      "url": "https://en.ain.ua/2024/02/05/3ts-capital-partner-
         +closes-fund-iv-111m",                                          
       8 +      "status": "found",                                       
       9 +      "score": 100,                                            
      10 +      "http_status": 200,                                      
      11 +      "note": ""                                               
      12 +    },                                                         
      13 +    {                                                          
      14 +      "path": "legal_entities[0]",                             
      15 +      "url": "https://fonecta.fi/profiili/3ts-capital-partners-
         +oy/545161",                                                    
      16 +      "status": "found",                                       
      17 +      "score": 100,                                            
      18 +      "http_status": 200,                                      
      19 +      "note": ""                                               
      20 +    },                                                         
      21 +    {                                                          
      22 +      "path": "type",                                          
      23 +      "url": "https://3tscapital.com/",                        
      24 +      "status": "found",                                       
      25 +      "score": 100,                                            
      26 +      "http_status": 200,                                      
      27 +      "note": ""                                               
      28 +    },                                                         
      29 +    {                                                          
      30 +      "path": "sectors",                                       
      31 +      "url": "https://en.ain.ua/2024/02/05/3ts-capital-partner-
         +closes-fund-iv-111m",                                          
      32 +      "status": "found",                                       
      33 +      "score": 100,                                            
      34 +      "http_status": 200,                                      
      35 +      "note": ""                                               
      36 +    },                                                         
      37 +    {                                                          
      38 +      "path": "stages",                                        
      39 +      "url": "https://3tscapital.com/",                        
      40 +      "status": "found",                                       
     … 33 more lines (ctrl+o to expand)
  ⎿  Created data/quote_checks/500-emerging-europe.json (+65 -0)
       1 +{                                                              
       2 +  "id": "500-emerging-europe",                                 
       3 +  "checked_at": "2026-10-13T14:01:14+00:00",                   
       4 +  "items": [                                                   
       5 +    {                                                          
       6 +      "path": "hq_country",                                    
       7 +      "url": "https://www.vestbee.com/insights/articles/e2vc-se
         +cures-first-close-of-100-m-fund",                              
       8 +      "status": "found",                                       
       9 +      "score": 100,                                            
      10 +      "http_status": 200,                                      
      11 +      "note": ""                                               
      12 +    },                                                         
      13 +    {                                                          
      14 +      "path": "type",                                          
      15 +      "url": "https://www.vestbee.com/insights/articles/e2vc-se
         +cures-first-close-of-100-m-fund",                              
      16 +      "status": "found",                                       
      17 +      "score": 100,                                            
      18 +      "http_status": 200,                                      
      19 +      "note": ""                                               
      20 +    },                                                         
      21 +    {                                                          
      22 +      "path": "sectors",                                       
      23 +      "url": "https://www.vestbee.com/insights/articles/e2vc-se
         +cures-first-close-of-100-m-fund",                              
      24 +      "status": "found",                                       
      25 +      "score": 100,                                            
      26 +      "http_status": 200,                                      
      27 +      "note": ""                                               
      28 +    },                                                         
      29 +    {                                                          
      30 +      "path": "stages",                                        
      31 +      "url": "https://www.vestbee.com/insights/articles/e2vc-se
         +cures-first-close-of-100-m-fund",                              
      32 +      "status": "found",                                       
      33 +      "score": 100,                                            
      34 +      "http_status": 200,                                      
      35 +      "note": ""                                               
      36 +    },                                                         
      37 +    {                                                          
      38 +      "path": "ticket",                                        
      39 +      "url": "https://www.vestbee.com/insights/articles/e2vc-se
         +cures-first-close-of-100-m-fund",                              
      40 +      "status": "found",                                       
     … 25 more lines (ctrl+o to expand)
  ⎿  Created data/quote_checks/alpha-intelligence-capital.json (+49 -0)
       1 +{                                                              
       2 +  "id": "alpha-intelligence-capital",                          
       3 +  "checked_at": "2026-10-13T14:01:14+00:00",                   
       4 +  "items": [                                                   
       5 +    {                                                          
       6 +      "path": "type",                                          
       7 +      "url": "https://www.maddyness.com/uk/2023/01/16/an-ai-foc
         +used-fund-with-a-tech-first-approach-a-profile-of-alpha-intelli
         +gence-capital/",                                               
       8 +      "status": "found",                                       
       9 +      "score": 100,                                            
      10 +      "http_status": 200,                                      
      11 +      "note": ""                                               
      12 +    },                                                         
      13 +    {                                                          
      14 +      "path": "sectors",                                       
      15 +      "url": "https://www.maddyness.com/uk/2023/01/16/an-ai-foc
         +used-fund-with-a-tech-first-approach-a-profile-of-alpha-intelli
         +gence-capital/",                                               
      16 +      "status": "found",                                       
      17 +      "score": 100,                                            
      18 +      "http_status": 200,                                      
      19 +      "note": ""                                               
      20 +    },                                                         
      21 +    {                                                          
      22 +      "path": "stages",                                        
      23 +      "url": "https://www.maddyness.com/uk/2023/01/16/an-ai-foc
         +used-fund-with-a-tech-first-approach-a-profile-of-alpha-intelli
         +gence-capital/",                                               
      24 +      "status": "found",                                       
      25 +      "score": 100,                                            
      26 +      "http_status": 200,                                      
      27 +      "note": ""                                               
      28 +    },                                                         
      29 +    {                                                          
      30 +      "path": "funds[0]",                                      
      31 +      "url": "https://www.maddyness.com/uk/2023/01/16/an-ai-foc
         +used-fund-with-a-tech-first-approach-a-profile-of-alpha-intelli
         +gence-capital/",                                               
      32 +      "status": "found",                                       
      33 +      "score": 100,                                            
      34 +      "http_status": 200,                                      
      35 +      "note": ""                                               
      36 +    },                                                         
      37 +    {                                                          
      38 +      "path": "evidence_of_activity[0]",                       
      39 +      "url": "https://www.mcdermottlaw.com/news/mcdermott-will-
         +schulte-advises-owkin-on-the-carve-out-of-waiv-and-its-33-milli
         +on-financing/",                                                
      40 +      "status": "found",                                       
     … 9 more lines (ctrl+o to expand)
  ⎿  Created data/quote_checks/aspire11.json (+89 -0)
       1 +{                                                              
       2 +  "id": "aspire11",                                            
       3 +  "checked_at": "2026-10-13T14:01:14+00:00",                   
       4 +  "items": [                                                   
       5 +    {                                                          
       6 +      "path": "hq_country",                                    
       7 +      "url": "https://www.lupa.cz/aktuality/cesi-jsou-ve-velke-
         +investorske-lize-penize-posilaji-do-revolutu/",                
       8 +      "status": "found",                                       
       9 +      "score": 100,                                            
      10 +      "http_status": 200,                                      
      11 +      "note": ""                                               
      12 +    },                                                         
      13 +    {                                                          
      14 +      "path": "legal_entities[0]",                             
      15 +      "url": "https://www.aspire11cap.com/legal",              
      16 +      "status": "found",                                       
      17 +      "score": 100,                                            
      18 +      "http_status": 200,                                      
      19 +      "note": ""                                               
      20 +    },                                                         
      21 +    {                                                          
      22 +      "path": "legal_entities[1]",                             
      23 +      "url": "https://www.aspire11cap.com/legal",              
      24 +      "status": "found",                                       
      25 +      "score": 100,                                            
      26 +      "http_status": 200,                                      
      27 +      "note": ""                                               
      28 +    },                                                         
      29 +    {                                                          
      30 +      "path": "type",                                          
      31 +      "url": "https://www.aspire11cap.com",                    
      32 +      "status": "found",                                       
      33 +      "score": 100,                                            
      34 +      "http_status": 200,                                      
      35 +      "note": ""                                               
      36 +    },                                                         
      37 +    {                                                          
      38 +      "path": "sectors",                                       
      39 +      "url": "https://www.aspire11cap.com",                    
      40 +      "status": "found",                                       
     … 49 more lines (ctrl+o to expand)
  ⎿  Created data/quote_checks/aternus-family-office.json (+57 -0)
       1 +{                                                              
       2 +  "id": "aternus-family-office",                               
       3 +  "checked_at": "2026-10-13T14:01:14+00:00",                   
       4 +  "items": [                                                   
       5 +    {                                                          
       6 +      "path": "hq_country",                                    
       7 +      "url": "https://www.aternus.cz/cz/",                     
       8 +      "status": "found",                                       
       9 +      "score": 100,                                            
      10 +      "http_status": 200,                                      
      11 +      "note": ""                                               
      12 +    },                                                         
      13 +    {                                                          
      14 +      "path": "legal_entities[0]",                             
      15 +      "url": "https://www.podnikatel.cz/rejstrik/aternus-a-s-25
         +865056/",                                                      
      16 +      "status": "found",                                       
      17 +      "score": 100,                                            
      18 +      "http_status": 200,                                      
      19 +      "note": ""                                               
      20 +    },                                                         
      21 +    {                                                          
      22 +      "path": "type",                                          
      23 +      "url": "https://www.aternus.cz/cz/",                     
      24 +      "status": "found",                                       
      25 +      "score": 100,                                            
      26 +      "http_status": 200,                                      
      27 +      "note": ""                                               
      28 +    },                                                         
      29 +    {                                                          
      30 +      "path": "sectors",                                       
      31 +      "url": "https://www.aternus.cz/cz/",                     
      32 +      "status": "found",                                       
      33 +      "score": 100,                                            
      34 +      "http_status": 200,                                      
      35 +      "note": ""                                               
      36 +    },                                                         
      37 +    {                                                          
      38 +      "path": "evidence_of_activity[0]",                       
      39 +      "url": "https://tech.eu/2025/12/16/jutro-medical-extends-
         +series-a-to-eur36m-for-ai-enabled-primary-care-scale/",        
      40 +      "status": "found",                                       
     … 17 more lines (ctrl+o to expand)
  ⎿  … 65 more files changed

⏺ --help isn't parsed, so that started the real quote check, and piping it into
  head may have cut it short. It's resumable, so I'll just run it to completion.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && .venv/bin/python
      -m src.check_quotes >
      /private/tmp/claude-502/-Users-davidkoktavy-Desktop-Investor-DB-S…)
  ⎿  budeto                                   {'found': 1}
     chilli-ventures                          {'found': 6}
     credo-ventures                           {'found': 8}
     … +58 lines (ctrl+o to expand)
  ⎿  Updated data/quote_checks/3ts-capital-partners.json (+1 -1)
      1  {
      2    "id": "3ts-capital-partners",
      3 -  "checked_at": "2026-10-13T14:01:14+00:00",                    
      3 +  "checked_at": "2026-10-13T14:01:53+00:00",                    
      4    "items": [
      5      {
      6        "path": "hq_country",
  ⎿  Updated data/quote_checks/500-emerging-europe.json (+1 -1)
      1  {
      2    "id": "500-emerging-europe",
      3 -  "checked_at": "2026-10-13T14:01:14+00:00",                    
      3 +  "checked_at": "2026-10-13T14:01:53+00:00",                    
      4    "items": [
      5      {
      6        "path": "hq_country",
  ⎿  Updated data/quote_checks/alpha-intelligence-capital.json (+1 -1)
      1  {
      2    "id": "alpha-intelligence-capital",
      3 -  "checked_at": "2026-10-13T14:01:14+00:00",                    
      3 +  "checked_at": "2026-10-13T14:01:53+00:00",                    
      4    "items": [
      5      {
      6        "path": "type",
  ⎿  Updated data/quote_checks/aspire11.json (+1 -1)
      1  {
      2    "id": "aspire11",
      3 -  "checked_at": "2026-10-13T14:01:14+00:00",                    
      3 +  "checked_at": "2026-10-13T14:01:53+00:00",                    
      4    "items": [
      5      {
      6        "path": "hq_country",
  ⎿  Updated data/quote_checks/aternus-family-office.json (+1 -1)
      1  {
      2    "id": "aternus-family-office",
      3 -  "checked_at": "2026-10-13T14:01:14+00:00",                    
      3 +  "checked_at": "2026-10-13T14:01:53+00:00",                    
      4    "items": [
      5      {
      6        "path": "hq_country",
  ⎿  … 64 more files changed
  ⎿  (timeout 10m)

⏺ Quote check done: 409 found, 3 missing, 7 unreachable—a surprisingly high hit
  rate given extractors often quoted from WebFetch summaries. I'll spot-check
  the reconstructed Inven Capital ticket quote (E-13) before trusting it.

  Ran 1 shell command (ctrl+o to expand)

⏺ Spot-checking the reconstructed Inven ticket quote, it scores 100—plausible
  since the label and value are likely adjacent once whitespace is normalized,
  but the verifier still checks each quote supports its claim. I'll commit R5
  and move on to R6, the Opus verifier, which only gets file paths.

  Ran 1 shell command (ctrl+o to expand)

⏺ 4 background agents launched (↓ to manage)
   ├ Verify 3ts-capital-partners
   ├ Verify 500-emerging-europe
   ├ Verify alpha-intelligence-capital
   └ Verify aspire11

⏺ R6 verification has started on the first 4 records. While they run, I'll
  update the helper to list records that still need verification.

  Ran 1 shell command (ctrl+o to expand)

⏺ The first four verifiers are running: 3TS Capital Partners, 500 Emerging
  Europe, Alpha Intelligence Capital and Aspire11. 65 records are still waiting
  for verification; the next four start as these finish.
✻ Cogitated for 1m 53s · done 4:02 PM

› Message from evidence-verifier
  alpha-intelligence-capital: 5 supported, 0 partially supported, 0 unsupported,
  0 contradicted, 0 unverifiable.
  Problems: none in the citations. The issue is the segment. Maddyness (2023)
  puts its offices in the US, France, UAE and Singapore, and nothing points to a
  team in Czechia, so my opinion is "no" for cz_vc.
  Its activity is in the window: it co-led Waiv's USD 33m Series A, announced
  2026-03-19. Sectors, stages and fund size come from a 2023 article and may be
  out of date.
  Output: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/alpha-intelligence-capital.json

⏺ Alpha Intelligence Capital is verified: all 5 items are supported. The
  verifier's view is that the team isn't in Czechia, so the record should drop
  out on geography. I'll log the run and start the next verifier when the usage
  notification arrives.

✻ Cooked for 2s · done 4:02 PM

⏺ Agent "Verify alpha-intelligence-capital" finished · 22s

› Message from evidence-verifier
  500-emerging-europe: 7 supported, 0 partial, 0 unsupported, 0 contradicted, 0
  unverifiable.
  No citation problems. The fund close type ("first") comes from the article
  headline, not from the quoted sentence.
  Record opinion: no. e2vc is an active VC, with a EUR 100M first close in Jan
  2026 and a pre-seed deal in Apr 2026. But the source calls it Turkey-based
  with offices in SF, NY and London. Nothing shows a team in Czechia, so it
  falls outside cz_vc.
  Output: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/500-emerging-europe.json

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo "2026-10-13,
      evidence-verifier,opus,alpha-intelligence-capital,16116,7,22.8,ok" >>
      data/runs/run_log…)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      100  2026-10-13,investor-extractor,sonnet,badideas-fund,36509,15,77
           .3,ok
      101  2026-10-13,investor-extractor,sonnet,eic-fund,36417,20,88.0,ok
      102  2026-10-13,investor-extractor,sonnet,500-emerging-europe,32139
           ,17,198.3,ok
      103 +2026-10-13,evidence-verifier,opus,alpha-intelligence-capital,1
          +6116,7,22.8,ok                                                

⏺ evidence-verifier(Verify aternus-family-office)
  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)

⏺ Agent "Verify 500-emerging-europe" finished · 29s

› Message from evidence-verifier
  3ts-capital-partners: 5 supported, 3 partially_supported, 0
  unsupported/contradicted/unverifiable. Written to
  /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/3ts-capital-partners.json
  1. Out of scope: the cited sources put the team in Helsinki and Vienna, and no
  cited page mentions Czechia (opinion: no). hq_country "FI" leaves out Vienna
  (AT).
  2. funds[0]: the cited page supports EUR 111m Fund IV, but not the name "TCEE
  Fund IV" or the 2021 vintage.
  3. Minor: sectors were narrowed to software_saas only. Patronus date
  "05-04-2026" can be read either way, but both readings are within the window.

⏺ Agent "Verify 3ts-capital-partners" finished · 32s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && printf '%s\n'
      "2026-10-13,evidence-verifier,opus,500-emerging-europe,17146,7,29.5,ok"
      "2026-10-13,eviden…)
  ⎿  Updated data/runs/run_log.csv (+2 -0)
      101  2026-10-13,investor-extractor,sonnet,eic-fund,36417,20,88.0,ok
      102  2026-10-13,investor-extractor,sonnet,500-emerging-europe,32139
           ,17,198.3,ok
      103  2026-10-13,evidence-verifier,opus,alpha-intelligence-capital,1
           6116,7,22.8,ok
      104 +2026-10-13,evidence-verifier,opus,500-emerging-europe,17146,7,
          +29.5,ok                                                       
      105 +2026-10-13,evidence-verifier,opus,3ts-capital-partners,18718,1
          +0,32.9,ok                                                     

⏺ 2 background agents launched (↓ to manage)
   ├ Verify badideas-fund
   └ Verify bd-partners

› Message from evidence-verifier
  aspire11: 6 supported, 4 partially_supported, 0 unsupported, 0 contradicted, 0
  unverifiable. Written to /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/aspire11.json
  Main problems:
  1. type `vc` is borderline. The homepage also describes a fund-of-funds
  strategy ("Tribes") next to late-stage/pre-IPO direct investments.
  2. hq_country CZ rests on "Česká investiční platforma" (Czech investment
  platform). No cited page says where the team is based.
  3. legal_entities[1]: the /legal page lists Partners investiční společnost as
  "Administrator", not as manager. sectors: the page says "technology", but the
  record maps it to "generalist".

⏺ Agent "Verify aspire11" finished · 35s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-13,evidence-verifier,opus,aspire11,19275,9,35.2,ok" >>
      data/runs/run_log.csv)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      103  2026-10-13,evidence-verifier,opus,alpha-intelligence-capital,1
           6116,7,22.8,ok
      104  2026-10-13,evidence-verifier,opus,500-emerging-europe,17146,7,
           29.5,ok
      105  2026-10-13,evidence-verifier,opus,3ts-capital-partners,18718,1
           0,32.9,ok
      106 +2026-10-13,evidence-verifier,opus,aspire11,19275,9,35.2,ok    

⏺ evidence-verifier(Verify borovicka-capital)
  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)

⏺ Five records are verified so far: 3TS, 500 Emerging Europe, Alpha
  Intelligence, Aspire11 and Aternus. Four verifiers are running: Aternus Family
  Office, BADideas.fund, BD Partners and Borovička Capital. 61 records are
  still waiting.

✻ Baked for 16s · done 4:03 PM

› Message from evidence-verifier
  borovicka-capital: 1 supported, 1 partially supported, 0 unsupported,
  contradicted or unverifiable.
  1. type: own site confirms vc ("investment company... venture capital
  investments"), but nothing on the page supports the subtype "family fund".
  2. hq_country is null with no source, so the Czech team location rests only on
  CzechCrunch calling it "čeští" (Czech).
  Outfindo deal (2025-01-20, participant) is inside the window. Opinion: yes,
  active, moderate confidence.
  File: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/borovicka-capital.json

⏺ Borovička Capital is verified: the Outfindo deal (Jan 2025) is inside the
  window and the verifier rates it active with moderate confidence. Its weak
  spot is the Czech team location, which has no direct source. That record has
  no hq_country, so decide.py will likely leave it pending. Three verifiers are
  still running.

✻ Worked for 2s · done 4:03 PM

⏺ Agent "Verify borovicka-capital" finished · 22s

› Message from evidence-verifier
  aternus-family-office: 3 supported, 3 partially_supported, 0 unsupported, 0
  contradicted, 0 unverifiable.
  1. Not a VC for cz_vc: by its own site, a multi family office that invests
  mainly as an LP in funds; the exclusion signal is supported.
  2. Deal and legal entity not confirmed: the Jutro Medical deal (Tech.eu, 16
  Dec 2025, in window) names only "Aternus" as a participant. The registry entry
  has its seat in Praha, not Třinec. Neither quote links it to this family
  office.
  3. Sectors describe the funds it holds, not its own direct investments.
  Output: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/aternus-family-office.json

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-13,evidence-verifier,opus,borovicka-capital,14683,7,22.6,ok" >>
      data/runs/run_log.csv; pyt…)
  ⎿  61 remaining: bpd-partners braiins
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      104  2026-10-13,evidence-verifier,opus,500-emerging-europe,17146,7,
           29.5,ok
      105  2026-10-13,evidence-verifier,opus,3ts-capital-partners,18718,1
           0,32.9,ok
      106  2026-10-13,evidence-verifier,opus,aspire11,19275,9,35.2,ok
      107 +2026-10-13,evidence-verifier,opus,borovicka-capital,14683,7,22
          +.6,ok                                                         

⏺ Agent "Verify aternus-family-office" finished · 36s

› Message from evidence-verifier
  badideas-fund: 4 supported, 3 partially_supported, 0 unsupported, 0
  contradicted, 0 unverifiable. Written to /Users/davidkoktavy/Desktop/Investor
  DB Starter/data/verification/badideas-fund.json
  1. This is a Latvian fund (a Latvian AIF anchored by ALTUM) with no Czech team
  on the cited pages, so it fails the CZ team requirement. Record opinion: no.
  2. The type and stages quotes are not on the page word for word (score 61).
  The page does say "Pre-seed and seed VC for CEE.", which supports both values.
  3. In evidence_of_activity[0], announced_date is null, but the portfolio page
  shows Tapaya with "Apr 2026", which is inside the window.

⏺ Agent "Verify badideas-fund" finished · 31s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && printf '%s\n'
      "2026-10-13,evidence-verifier,opus,aternus-family-office,17708,8,36.5,ok"
      "2026-10-13,evid…)
  ⎿  61 remaining: bpd-partners braiins btcz-ventures
  ⎿  Updated data/runs/run_log.csv (+2 -0)
      105  2026-10-13,evidence-verifier,opus,3ts-capital-partners,18718,1
           0,32.9,ok
      106  2026-10-13,evidence-verifier,opus,aspire11,19275,9,35.2,ok
      107  2026-10-13,evidence-verifier,opus,borovicka-capital,14683,7,22
           .6,ok
      108 +2026-10-13,evidence-verifier,opus,aternus-family-office,17708,
          +8,36.5,ok                                                     
      109 +2026-10-13,evidence-verifier,opus,badideas-fund,17276,8,31.0,o
          +k                                                             

⏺ 3 background agents launched (↓ to manage)
   ├ Verify bpd-partners
   ├ Verify braiins
   └ Verify btcz-ventures

› Message from evidence-verifier
  bd-partners: 3 supported, 3 partially_supported, 0 unsupported, 0
  contradicted, 0 unverifiable.
  1. The record's own source says BD Partners is "joint family office, nejsme
  klasický fond", so it falls outside the cz_vc segment (VC/CVC only).
  2. evidence_of_activity[1] (WanderWallet, co-lead) is confirmed, but the DEPO
  page has no date, so it may be outside the window. The in-window deal is
  Myriad AI (participant, 2025-09-16).
  3. type and sectors have self_reported=false, but they quote the investor's
  own partner, so it should be true. The meta note's board claim is not on the
  Finmag page.
  File: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/bd-partners.json

⏺ Agent "Verify bd-partners" finished · 46s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-13,evidence-verifier,opus,bd-partners,19227,9,46.5,ok" >>
      data/runs/run_log.csv; python3 /…)  ⎿  58 remaining: budeto
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      107  2026-10-13,evidence-verifier,opus,borovicka-capital,14683,7,22
           .6,ok
      108  2026-10-13,evidence-verifier,opus,aternus-family-office,17708,
           8,36.5,ok
      109  2026-10-13,evidence-verifier,opus,badideas-fund,17276,8,31.0,o
           k
      110 +2026-10-13,evidence-verifier,opus,bd-partners,19227,9,46.5,ok 

⏺ evidence-verifier(Verify budeto)
  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)

⏺ R6 verification: 9 of 69 records are verified, and four verifiers are running
  now (BPD Partners, Braiins, BTCZ, Budeto). Each one takes about half a minute.
  When all 69 are done, I'll run R7 (decide) and R8 (review sheet).

✻ Sautéed for 25s · done 4:03 PM

› Message from evidence-verifier
  btcz-ventures: 1 supported, 2 partially_supported, 0 unsupported, 0
  contradicted, 0 unverifiable. Opinion: unsure.
  1. evidence_of_activity[0]: the quote is about BTCZ funding research at IOCB
  (2018, 2023), not investing in Taveren. The Dec 2025 Taveren stake is credited
  to parent BPD Partners Group, so the in-window activity is not clearly
  BTCZ's.
  2. type: "vc" is a judgment call. The page shows a vehicle of BPD Partners
  Group and B3 Holding (Bruzek family), not a VC fund manager.
  3. hq_country is null and the page does not say where the team is based.
  File: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/btcz-ventures.json

⏺ The verifier caught the BTCZ problem I logged as E-14: the cited quote is
  about funding research, and the December 2025 Taveren stake belongs to the
  parent, BPD Partners Group. It rated the item partially_supported, not
  unsupported, though. In R7 I'll check whether decide.py still counts a
  partially supported item as activity.

✻ Brewed for 3s · done 4:04 PM

⏺ Agent "Verify btcz-ventures" finished · 30s

⏺ Agent "Verify braiins" finished · 31s

› Message from evidence-verifier
  braiins: 1 supported, 1 partially_supported. Advisory opinion: no, not an
  active VC/CVC investor. Written to /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/braiins.json
  1. evidence_of_activity[0] (Firefish): the stake was taken in Sept 2024,
  before the window opens on 2024-10-11. Only the blog's publication date
  (2025-04-08) falls inside the window.
  2. Braiins is a bitcoin-mining company, not a VC/CVC manager. The record shows
  one strategic minority stake (Braiins joined the round; the page does not say
  it led) and the type is null.

⏺ The Braiins verifier caught a date error: the Firefish stake was taken in
  September 2024, before the window opens. The record dated it by the April 2025
  blog post. I'll log it as an AI error at R7. Starting the next two verifiers
  now.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && printf '%s\n'
      "2026-10-13,evidence-verifier,opus,btcz-ventures,15463,6,30.5,ok"
      "2026-10-13,evidence-ver…)
  ⎿  57 remaining: chilli-ventures credo-ventures
  ⎿  Updated data/runs/run_log.csv (+2 -0)
      108  2026-10-13,evidence-verifier,opus,aternus-family-office,17708,
           8,36.5,ok
      109  2026-10-13,evidence-verifier,opus,badideas-fund,17276,8,31.0,o
           k
      110  2026-10-13,evidence-verifier,opus,bd-partners,19227,9,46.5,ok
      111 +2026-10-13,evidence-verifier,opus,btcz-ventures,15463,6,30.5,o
          +k                                                             
      112 +2026-10-13,evidence-verifier,opus,braiins,14919,6,31.7,ok     

› Message from evidence-verifier
  bpd-partners: 3 supported, 2 partially_supported, 0
  unsupported/contradicted/unverifiable. Written to
  /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/bpd-partners.json
  1. The only activity item (Powerful Medical seed, 2022-09-28) is real but
  falls outside both the 24-month and the 36-month window. No sourced evidence
  of current activity.
  2. `type` = family_office is inferred. E15 calls it an "investiční skupina"
  managing three billionaires' money, not a VC. The page's date (2021-03-13) was
  left null in the record.
  3. `sectors` maps "realitní development" (real-estate development) to
  proptech_construction, which is a stretch. Opinion: not an active VC of the
  claimed type.

⏺ Agent "Verify bpd-partners" finished · 35s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-13,evidence-verifier,opus,bpd-partners,17360,8,35.1,ok" >>
      data/runs/run_log.csv; python3…)
  ⎿  57 remaining: chilli-ventures credo-ventures czech-founders-vc
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      110  2026-10-13,evidence-verifier,opus,bd-partners,19227,9,46.5,ok
      111  2026-10-13,evidence-verifier,opus,btcz-ventures,15463,6,30.5,o
           k
      112  2026-10-13,evidence-verifier,opus,braiins,14919,6,31.7,ok
      113 +2026-10-13,evidence-verifier,opus,bpd-partners,17360,8,35.1,ok

⏺ 3 background agents launched (↓ to manage)
   ├ Verify chilli-ventures
   ├ Verify credo-ventures
   └ Verify czech-founders-vc

› Message from evidence-verifier
  budeto: 1 sourced item, rated partially_supported (0 supported, 0
  unsupported/contradicted/unverifiable). Written to
  /Users/davidkoktavy/Desktop/Investor DB Starter/data/verification/budeto.json
  1. evidence_of_activity[0] (Vetstor): the quote is word-for-word on the page,
  and the CzechCrunch article dated 2025-12-09 falls inside the window. It names
  Budeto as an investor in a EUR 1M round. But the article gives no stage for
  that round, so the record's "seed" label has no support.
  2. The article calls Budeto a startup studio, not a VC, and Vetstor started
  inside Budeto. The record's own fields agree: type null, hq_country null.
  Opinion: "no", it is not an active VC/CVC with a confirmed CZ team.

⏺ Agent "Verify budeto" finished · 33s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-13,evidence-verifier,opus,budeto,14838,6,33.0,ok" >>
      data/runs/run_log.csv; python3 /priva…)
  ⎿  54 remaining: dendis-capital
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      111  2026-10-13,evidence-verifier,opus,btcz-ventures,15463,6,30.5,o
           k
      112  2026-10-13,evidence-verifier,opus,braiins,14919,6,31.7,ok
      113  2026-10-13,evidence-verifier,opus,bpd-partners,17360,8,35.1,ok
      114 +2026-10-13,evidence-verifier,opus,budeto,14838,6,33.0,ok      

⏺ evidence-verifier(Verify dendis-capital)
  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)

⏺ 15 of 69 records are verified. Four verifiers are running now: Chilli
  Ventures, Credo Ventures, Czech Founders VC and Dendis Capital. 54 records
  remain.

✻ Sautéed for 20s · done 4:04 PM

› Message from evidence-verifier
  chilli-ventures: 5 supported, 1 partially_supported, 0 unsupported, 0
  contradicted, 0 unverifiable. Record opinion: unsure.
  1. `type`: partially_supported. The quote supports the stage, not "vc". The
  same site says "We invest exclusively our own capital" and "we are LP partners
  in VC funds", so this may be a family office or own-capital investor rather
  than a VC manager.
  2. `evidence_of_activity[0]` (DecisionRules, 2025-05-06): supported, Chilli
  Ventures named as a participant and inside the window. Minor point:
  self_reported=false is debatable, since the release comes from the investee.
  Output: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/chilli-ventures.json

⏺ Chilli Ventures is verified: 5 items supported, 1 partially supported. The
  open question is its type: it invests only its own capital and is also an LP
  in other funds, so it may be a family office rather than a VC. That case goes
  to your manual review. Three verifiers are still running.

✻ Baked for 2s · done 4:04 PM

⏺ Agent "Verify chilli-ventures" finished · 27s

⏺ Agent "Verify czech-founders-vc" finished · 27s

› Message from evidence-verifier
  czech-founders-vc: 6 supported, 0 partial / unsupported / contradicted /
  unverifiable. Opinion: yes.
  Serious problems: none.
  Minor: the Merchantee page gives two round sizes (EUR 1.8m in the headline,
  USD 2.1m in the body), but the record does not use the round size. The site
  also lists a Bratislava office, but Prague is primary.
  Output: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/czech-founders-vc.json

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && printf '%s\n'
      "2026-10-13,evidence-verifier,opus,chilli-ventures,16121,7,27.0,ok"
      "2026-10-13,evidence-v…)
  ⎿  53 remaining: depo-ventures diaspora-ventures
  ⎿  Updated data/runs/run_log.csv (+2 -0)
      112  2026-10-13,evidence-verifier,opus,braiins,14919,6,31.7,ok
      113  2026-10-13,evidence-verifier,opus,bpd-partners,17360,8,35.1,ok
      114  2026-10-13,evidence-verifier,opus,budeto,14838,6,33.0,ok
      115 +2026-10-13,evidence-verifier,opus,chilli-ventures,16121,7,27.0
          +,ok                                                           
      116 +2026-10-13,evidence-verifier,opus,czech-founders-vc,17024,9,27
          +.8,ok                                                         

› Message from evidence-verifier
  credo-ventures: 6 supported, 2 partially_supported, 0 unsupported, 0
  contradicted, 0 unverifiable. Written to /Users/davidkoktavy/Desktop/Investor
  DB Starter/data/verification/credo-ventures.json
  1. evidence_of_activity[2]: Delta Green was announced 2024-05-27, before the
  24-month window start of 2024-10-11, so it counts toward dormant status only.
  2. stages: the record has only pre_seed, but the homepage says "Pre-seed —
  Onwards".
  3. The two in-window deals (Duvo, Dec 2025; Picogrid, May 2026) come only from
  tier-3 aggregators, but both name Credo as an investor. Opinion: yes, an
  active Czech VC.

⏺ Agent "Verify credo-ventures" finished · 33s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-13,evidence-verifier,opus,credo-ventures,18657,11,33.9,ok" >>
      data/runs/run_log.csv && git…)
  ⎿  53 remaining: depo-ventures diaspora-ventures eic-fund
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      114  2026-10-13,evidence-verifier,opus,budeto,14838,6,33.0,ok
      115  2026-10-13,evidence-verifier,opus,chilli-ventures,16121,7,27.0
           ,ok
      116  2026-10-13,evidence-verifier,opus,czech-founders-vc,17024,9,27
           .8,ok
      117 +2026-10-13,evidence-verifier,opus,credo-ventures,18657,11,33.9
          +,ok                                                           

⏺ 3 background agents launched (↓ to manage)
   ├ Verify depo-ventures
   ├ Verify diaspora-ventures
   └ Verify eic-fund
› Message from evidence-verifier
  dendis-capital: 5 supported, 1 partially_supported, 0 unsupported, 0
  contradicted, 0 unverifiable. Written to /Users/davidkoktavy/Desktop/Investor
  DB Starter/data/verification/dendis-capital.json
  1. sectors: the cited site supports health_biotech and medtech, but nothing on
  it supports ai_data. Observed value: [health_biotech, medtech].
  2. evidence_of_activity[0] (HTG Medical pre-seed, 2026-07-14, inside the
  window) is supported. But the page is a PROTEXT commercial press release, so
  tier 3 overstates how independent it is.
  3. Opinion: yes, an active investor of the claimed type (family_office, a Brno
  family foundation). That type is not vc/cvc, so it falls outside the cz_vc
  segment.

⏺ Agent "Verify dendis-capital" finished · 32s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-13,evidence-verifier,opus,dendis-capital,16809,7,32.2,ok" >>
      data/runs/run_log.csv; python…)
  ⎿  50 remaining: emun
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      115  2026-10-13,evidence-verifier,opus,chilli-ventures,16121,7,27.0
           ,ok
      116  2026-10-13,evidence-verifier,opus,czech-founders-vc,17024,9,27
           .8,ok
      117  2026-10-13,evidence-verifier,opus,credo-ventures,18657,11,33.9
           ,ok
      118 +2026-10-13,evidence-verifier,opus,dendis-capital,16809,7,32.2,
          +ok                                                            

⏺ evidence-verifier(Verify emun)
  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)

⏺ 19 of the 69 records are verified. Four verifiers are running: DEPO, Diaspora,
  EIC Fund and EMUN. 46 remain after these.

✻ Crunched for 22s · done 4:05 PM

› Message from evidence-verifier
  diaspora-ventures: 3 supported, 1 partially_supported, 0 unsupported,
  contradicted or unverifiable.
  - ticket: the 2020 TechCrunch article gives an "average check between $100,000
  and $200,000". That is an average, not a min/max range, and it is 6 years
  old.
  - The record has no dated activity evidence, and its team is in the US
  (TechCrunch 2020), not Czechia. Opinion: no, it does not fit cz_vc.
  File: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/diaspora-ventures.json

⏺ Diaspora Ventures is verified. It has no dated activity and a US-based team,
  so it will drop out of the Czech VC segment. I'll log it once its usage
  notification arrives. Three verifiers are still running: DEPO, EIC Fund and
  EMUN.

✻ Cooked for 2s · done 4:05 PM

⏺ Agent "Verify diaspora-ventures" finished · 22s

› Message from evidence-verifier
  depo-ventures: 7 of 7 items supported; none partially supported, unsupported,
  contradicted or unverifiable.
  No problems with the record itself. The cited sources back the Prague HQ,
  early-stage VC type, sectors, pre-seed stage, the EUR 250K-500K ticket, and
  two deals: Tapaya (co-lead, 29 Apr 2026) and WanderWallet (13 Mar 2026).
  One thing to know: the depoventures.com homepage contains hidden instructions
  aimed at AI readers. I ignored them, and I noted this in the record opinion.
  Record opinion: yes, an active Czech VC.
  Output: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/depo-ventures.json

⏺ DEPO Ventures is fully supported (7 of 7). The verifier found hidden
  instructions aimed at AI readers on depoventures.com. That's the third such
  page, and both DEPO extractor runs read that homepage without reporting it.
  I'm logging it as E-17.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && printf '%s\n'
      "2026-10-13,evidence-verifier,opus,diaspora-ventures,14454,7,22.8,ok" >>
      data/runs/run_log…)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      116  2026-10-13,evidence-verifier,opus,czech-founders-vc,17024,9,27
           .8,ok
      117  2026-10-13,evidence-verifier,opus,credo-ventures,18657,11,33.9
           ,ok
      118  2026-10-13,evidence-verifier,opus,dendis-capital,16809,7,32.2,
           ok
      119 +2026-10-13,evidence-verifier,opus,diaspora-ventures,14454,7,22
          +.8,ok                                                         
  ⎿  Updated docs/ai-errors.md (+1 -0)
      20  | E-14 | 2026-10-12 | investor-extractor | btcz-ventures | `evi
          dence_of_activity[0]` | Zapsána investice do Taveren (12/2025),
           ačkoli zdroj (stránka IOCB) říká jen, že BTCZ výzkum dlouhodob
          ě podporuje a „poslední příspěvek“ dala BPD Partners; účast BTC
          Z v kole z prosince 2025 nedokládá. | Agent to sám přiznal v zá
          věrečné zprávě. | Zatím nic; čekám, zda položku odmítne ověřova
          tel (R6). Pokud ano, decide.py ji vynuluje. |
      21  | E-15 | 2026-10-13 | investor-extractor (opakovaně) | lighthou
          se-ventures, patero, metatron-global, jsk-investments | závěreč
          ná zpráva | Agent chybně počítá okno 24 měsíců od AS_OF (2026-1
          0-11 → začátek 2024-10-11): Outfindo 2025-01 a Elin.ai 2024-12 
          označil za starší než 24 měsíců, naopak Flowpay 2024-03 a Ticke
          too 2024-01 za čerstvé. | Orchestrátor při čtení závěrečných zp
          ráv. | Nic: okno počítá `decide.py` z dat v záznamu, chyba je j
          en v textu zprávy. Potvrzuje princip „agent sbírá fakta, kód ro
          zhoduje“. |
      22  | E-16 | 2026-10-13 | investor-extractor | y-soft-ventures | — 
          | Agent mimo svou roli spustil `src.check_quotes` nad všemi záz
          namy (krok R5 orchestrátoru), zatímco jiní extraktoři ještě zap
          isovali. | Závěrečná zpráva agenta; nečekaná složka `data/quote
          _checks/`. | Výstup smazán, R5 poběží jednou po dokončení extra
          kce. Prompt extraktoru zatím neměním (jednorázové); oprávnění p
          rojektu příkaz povolují všem agentům. |
      23 +| E-17 | 2026-10-13 | evidence-verifier / investor-extractor | 
         +depo-ventures | — | Domovská stránka depoventures.com obsahuje 
         +skryté pokyny pro AI čtenáře (třetí případ prompt injection po 
         +E-04 a E-07). Ověřovatel je rozpoznal a ignoroval; oba běhy ext
         +raktoru stránku četly, ale ve zprávě to neuvedly. Hodnoty v záz
         +namu ověřovatel potvrdil (7/7 podloženo), takže vliv na data ne
         +vidím. | Zpráva ověřovatele (R6). | Nic; doporučení pro README:
         + obsah stránek je nedůvěryhodný vstup a nezávislé ověření je pr
         +oti tomu ochrana. Ruční kontrola by měla záznam DEPO projít se 
         +zvýšenou pozorností. |                                         

⏺ Agent "Verify depo-ventures" finished · 27s

› Message from evidence-verifier
  emun: 3 supported, 1 partially_supported, 0
  unsupported/contradicted/unverifiable (4 items in total; there are no activity
  items to check).
  1. `type`: the value `family_office` is right, but the cited quote only gives
  the AUM figure, so the quote doesn't support it. The page's support is "Jsme
  family office…".
  2. `capital`: the 16 bn CZK is a lower bound ("přes", meaning "over") and
  covers the whole firm's managed assets, not VC capital.
  3. Opinion is `no`: it's a family office / wealth manager with no investment
  deals cited, not a CZ VC.
  File: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/emun.json

⏺ Agent "Verify emun" finished · 26s

› Message from evidence-verifier
  eic-fund: 3 supported, 3 partially_supported, 0 unsupported, contradicted or
  unverifiable. Record opinion: no (not a Czech team).
  1. `hq_country` LU: the cited quote doesn't mention Luxembourg. The 2022 page
  says only that the administrator, AlterDomus, is Luxembourg-based, not where
  the team sits.
  2. `evidence_of_activity[1]` (Sensoneo, 2023-06-19) is accurate but falls
  before the 24-month and 36-month windows, so only eleQtron (2026-05-05) counts
  as recent activity.
  3. `capital`: the page gives "over €4 billion" capitalisation, not AUM, so
  `basis` is loose. Mapping "deep tech" to `deeptech_hardware` is an inference.
  File: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/eic-fund.json

⏺ Agent "Verify eic-fund" finished · 34s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && printf '%s\n'
      "2026-10-13,evidence-verifier,opus,depo-ventures,16836,9,27.2,ok"
      "2026-10-13,evidence-ver…)
  ⎿  49 remaining: fazole-ventures founder-institute-prague gi21-capital gr
     ouport-ventures
  ⎿  Updated data/runs/run_log.csv (+3 -0)
      117  2026-10-13,evidence-verifier,opus,credo-ventures,18657,11,33.9
           ,ok
      118  2026-10-13,evidence-verifier,opus,dendis-capital,16809,7,32.2,
           ok
      119  2026-10-13,evidence-verifier,opus,diaspora-ventures,14454,7,22
           .8,ok
      120 +2026-10-13,evidence-verifier,opus,depo-ventures,16836,9,27.2,o
          +k                                                             
      121 +2026-10-13,evidence-verifier,opus,emun,15508,7,26.8,ok        
      122 +2026-10-13,evidence-verifier,opus,eic-fund,18239,10,34.8,ok   

⏺ The helper says 49 remain, but I've logged 23 verifications, which would leave
  46. I'll check which files actually exist.

  Ran 1 shell command (ctrl+o to expand)

⏺ My count was off: 20 verifications are done, all logged, so 49 remain.
  Launching the next 4.

⏺ 4 background agents launched (↓ to manage)
   ├ Verify fazole-ventures
   ├ Verify founder-institute-prague
   ├ Verify gi21-capital
   └ Verify grouport-ventures

⏺ Four verifiers are running: Fazole Ventures, Founder Institute Prague, Gi21
  Capital and Grouport Ventures. 45 records remain after these. I'm launching
  each new verifier as one finishes.

✻ Brewed for 29s · done 4:06 PM

› Message from evidence-verifier
  Verdicts: 1 partially_supported, 0 of any other kind. This is the record's
  only sourced item; all other fields are null.
  1. exclusion_signals[0] `grant_or_program_only`: the quote is verbatim on
  fi.co/faq. It shows equity is taken only as a pledged warrant, which points to
  a programme rather than a fund. But it's the global Founder Institute FAQ,
  not a Prague page, and it doesn't support the "entrance fee" in the note.
  2. Record opinion: no. It's an accelerator programme run by Founder Institute,
  Inc. (US). No investments, fund, Czech legal entity or Czech team is cited.
  Written to /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/founder-institute-prague.json

⏺ Founder Institute Prague is verified. It is an accelerator programme with no
  investments or Czech team cited, so it should drop out. Three verifiers are
  still running: Fazole, Gi21 and Grouport.

✻ Crunched for 2s · done 4:06 PM

⏺ Agent "Verify founder-institute-prague" finished · 15s

› Message from evidence-verifier
  grouport-ventures: 0 supported, 1 partially_supported, 0 unsupported, 0
  contradicted, 1 unverifiable. Record opinion: no.
  1. evidence_of_activity[0]: the only deal is from July 2022, before both the
  24-month window and the 36-month dormant start. The page names "Gruport
  Ventures", so it may not be the same investor. The page gives only "Jul 2022",
  so the exact day 2022-07-07 is not on it.
  2. Type, HQ and website are all null with no primary source. Nothing cited
  shows a Czech VC.
  3. exclusion_signals[0] (not_found_or_defunct) cites no source.
  File: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/grouport-ventures.json

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo "2026-10-13,
      evidence-verifier,opus,founder-institute-prague,13321,5,15.5,ok" >>
      data/runs/run_log.c…)
  ⎿  45 remaining: i-and-i-biotech
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      120  2026-10-13,evidence-verifier,opus,depo-ventures,16836,9,27.2,o
           k
      121  2026-10-13,evidence-verifier,opus,emun,15508,7,26.8,ok
      122  2026-10-13,evidence-verifier,opus,eic-fund,18239,10,34.8,ok
      123 +2026-10-13,evidence-verifier,opus,founder-institute-prague,133
          +21,5,15.5,ok                                                  

⏺ evidence-verifier(Verify i-and-i-biotech)
  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)

⏺ Agent "Verify grouport-ventures" finished · 20s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-13,evidence-verifier,opus,grouport-ventures,13933,6,20.1,ok" >>
      data/runs/run_log.csv)  ⎿  Updated data/runs/run_log.csv (+1 -0)
      121  2026-10-13,evidence-verifier,opus,emun,15508,7,26.8,ok
      122  2026-10-13,evidence-verifier,opus,eic-fund,18239,10,34.8,ok
      123  2026-10-13,evidence-verifier,opus,founder-institute-prague,133
           21,5,15.5,ok
      124 +2026-10-13,evidence-verifier,opus,grouport-ventures,13933,6,20
          +.1,ok                                                         

⏺ evidence-verifier(Verify i-and-i-prague)
  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)

⏺ 22 of 69 records are verified. Four verifiers are running: Fazole Ventures,
  Gi21 Capital, i&i Biotech and i&i Prague. 43 records remain after these.

✻ Baked for 11s · done 4:06 PM

› Message from evidence-verifier
  gi21-capital: 6 supported, 1 partially_supported (type), 0
  unsupported/contradicted/unverifiable. Record opinion: unsure.
  1. Type `vc` only partly fits. The firm's site calls it a "multi-stage
  investment group", and VC/PE tech investing is one of its four business lines
  (the others are data centres, hospitality and culture). It is closer to a
  billionaire's family-office/holding than a dedicated VC manager.
  2. Zerops seed (Gi21 as lead) is linked to the founder: Špoljarič co-founded
  the company Zerops spun out of. Hermetiq (2026-08-24) and FaceUp (2026-05-19)
  are independent deals, both within the window.
  Written to /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/gi21-capital.json

⏺ Gi21 Capital is verified: 6 items supported, but vc fits only partly. It is a
  multi-business investment group with a VC/PE line, so it goes to your manual
  review as a type judgment call. Three verifiers are still running.

✻ Cogitated for 2s · done 4:06 PM

⏺ Agent "Verify gi21-capital" finished · 32s

› Message from evidence-verifier
  fazole-ventures: 6 supported, 1 partially supported, 0 unsupported, 0
  contradicted, 0 unverifiable. Record opinion: yes (active Czech VC). Written
  to /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/fazole-ventures.json
  1. Only one deal is inside the 24-month window: Everbot, 16 Sep 2025. The
  GoodAccess deal (3 Feb 2023) is dated correctly but falls outside both the 24-
  and 36-month windows.
  2. `stages`: the record says "seed", but the quote only sets a
  product-maturity requirement. The page says "early-stage", so seed is an
  inference.
  3. `type`: Lupa calls it a "fond", but it is controlled by three individuals
  (Bouška, Černý, Přikryl). It could be a private vehicle rather than a VC
  managing outside money.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-13,evidence-verifier,opus,gi21-capital,18457,9,32.5,ok" >>
      data/runs/run_log.csv; python3…)
  ⎿  43 remaining: impulse-ventures
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      122  2026-10-13,evidence-verifier,opus,eic-fund,18239,10,34.8,ok
      123  2026-10-13,evidence-verifier,opus,founder-institute-prague,133
           21,5,15.5,ok
      124  2026-10-13,evidence-verifier,opus,grouport-ventures,13933,6,20
           .1,ok
      125 +2026-10-13,evidence-verifier,opus,gi21-capital,18457,9,32.5,ok

⏺ evidence-verifier(Verify impulse-ventures)
  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)

⏺ Agent "Verify fazole-ventures" finished · 42s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-13,evidence-verifier,opus,fazole-ventures,18306,8,42.8,ok" >>
      data/runs/run_log.csv && git…)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      123  2026-10-13,evidence-verifier,opus,founder-institute-prague,133
           21,5,15.5,ok
      124  2026-10-13,evidence-verifier,opus,grouport-ventures,13933,6,20
           .1,ok
      125  2026-10-13,evidence-verifier,opus,gi21-capital,18457,9,32.5,ok
      126 +2026-10-13,evidence-verifier,opus,fazole-ventures,18306,8,42.8
          +,ok                                                           

⏺ evidence-verifier(Verify incomming-ventures)
  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)

› Message from evidence-verifier
  i-and-i-prague: 3 items checked. 1 supported, 2 unverifiable, 0 unsupported, 0
  contradicted.
  1. hq_country and legal_entities[0] (company ID 06058485) both cite a kurzy.cz
  search-results page. Its robots.txt disallows fetching, so I could not check
  them. The company's homepage, which the record does not cite, shows the same
  Prague address.
  2. The record claims no type and has no activity evidence. By its homepage,
  this is a biotech incubator and venture builder. The VC investing runs through
  the separate i&i Biotech Fund. My opinion on whether this is an active
  investor of the claimed type: no.
  File: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/i-and-i-prague.json

⏺ Agent "Verify i-and-i-prague" finished · 23s

⏺ I found a conflict: kurzy.cz search pages are blocked by robots.txt, yet the
  extractor prompt lists kurzy.cz as an acceptable registry mirror. I'll log
  this as E-18 for the README.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-13,evidence-verifier,opus,i-and-i-prague,14599,6,23.8,ok" >>
      data/runs/run_log.csv && grep…)
  ⎿  12
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      124  2026-10-13,evidence-verifier,opus,grouport-ventures,13933,6,20
           .1,ok
      125  2026-10-13,evidence-verifier,opus,gi21-capital,18457,9,32.5,ok
      126  2026-10-13,evidence-verifier,opus,fazole-ventures,18306,8,42.8
           ,ok
      127 +2026-10-13,evidence-verifier,opus,i-and-i-prague,14599,6,23.8,
          +ok                                                            
  ⎿  Updated docs/ai-errors.md (+1 -0)
      21  | E-15 | 2026-10-13 | investor-extractor (opakovaně) | lighthou
          se-ventures, patero, metatron-global, jsk-investments | závěreč
          ná zpráva | Agent chybně počítá okno 24 měsíců od AS_OF (2026-1
          0-11 → začátek 2024-10-11): Outfindo 2025-01 a Elin.ai 2024-12 
          označil za starší než 24 měsíců, naopak Flowpay 2024-03 a Ticke
          too 2024-01 za čerstvé. | Orchestrátor při čtení závěrečných zp
          ráv. | Nic: okno počítá `decide.py` z dat v záznamu, chyba je j
          en v textu zprávy. Potvrzuje princip „agent sbírá fakta, kód ro
          zhoduje“. |
      22  | E-16 | 2026-10-13 | investor-extractor | y-soft-ventures | — 
          | Agent mimo svou roli spustil `src.check_quotes` nad všemi záz
          namy (krok R5 orchestrátoru), zatímco jiní extraktoři ještě zap
          isovali. | Závěrečná zpráva agenta; nečekaná složka `data/quote
          _checks/`. | Výstup smazán, R5 poběží jednou po dokončení extra
          kce. Prompt extraktoru zatím neměním (jednorázové); oprávnění p
          rojektu příkaz povolují všem agentům. |
      23  | E-17 | 2026-10-13 | evidence-verifier / investor-extractor | 
          depo-ventures | — | Domovská stránka depoventures.com obsahuje 
          skryté pokyny pro AI čtenáře (třetí případ prompt injection po 
          E-04 a E-07). Ověřovatel je rozpoznal a ignoroval; oba běhy ext
          raktoru stránku četly, ale ve zprávě to neuvedly. Hodnoty v záz
          namu ověřovatel potvrdil (7/7 podloženo), takže vliv na data ne
          vidím. | Zpráva ověřovatele (R6). | Nic; doporučení pro README:
           obsah stránek je nedůvěryhodný vstup a nezávislé ověření je pr
          oti tomu ochrana. Ruční kontrola by měla záznam DEPO projít se 
          zvýšenou pozorností. |
      24 +| E-18 | 2026-10-13 | investor-extractor (prompt) | i-and-i-pra
         +gue (a další záznamy s kurzy.cz) | `hq_country`, `legal_entitie
         +s` | Prompt extraktoru doporučuje `rejstrik-firem.kurzy.cz` jak
         +o zrcadlo rejstříku, ale vyhledávací stránky kurzy.cz zakazuje 
         +robots.txt. Ověřovatel je proto nemohl otevřít (`unverifiable`)
         +, `check_quotes.py` je hlásí jako nedostupné. Chyba je v mém za
         +dání, ne v modelu. | Ověřovatel (R6). | Zatím nic, aby šlo měři
         +t pilot beze změny. Pro další běh: v promptu nahradit kurzy.cz 
         +za ARES API / or.justice.cz (úroveň 1) a robots.txt zmínit výsl
         +ovně. |                                                        

⏺ evidence-verifier(Verify inven-capital)
  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)

⏺ Twelve staging records cite kurzy.cz. That's now logged as E-18, with a prompt
  fix proposed for the next run but not applied, so this pilot is measured on
  one unchanged prompt.

  Verification: 25 of 69 records done. Running now: i&i Biotech, Impulse
  Ventures, InCOMMing Ventures and Inven Capital.

✻ Cooked for 25s · done 4:07 PM

› Message from evidence-verifier
  i-and-i-biotech: 6 supported, 3 partially supported, 0
  unsupported/contradicted/unverifiable. Opinion: yes, an active life-science
  VC.
  1. `hq_country` and `legal_entities[0]`: the cited kurzy.cz registry page
  never mentions i&i. The Prague adviser link (Biotech Investments s.r.o.) is
  only on inibio.eu, and that site gives the fund's registered HQ as Luxembourg.
  2. `ticket`: EUR 0.5M–2M is the site's "sweet spot"; the same page says
  investments can start at €150k (observed min 150000).
  Written to /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/i-and-i-biotech.json

⏺ i&i Biotech is verified, and the verifier rates it an active life-science VC.
  Two items are only partly supported:
  - Team location: the Prague link rests only on the fund's own site, which
    gives the fund's registered HQ as Luxembourg.
  - Ticket: the recorded EUR 0.5–2M is only the "sweet spot"; the same page says
    investments start at €150k.

  Three verifiers are still running: Impulse Ventures, InCOMMing Ventures and
  Inven Capital.

✻ Churned for 2s · done 4:07 PM

⏺ Agent "Verify i-and-i-biotech" finished · 43s

› Message from evidence-verifier
  impulse-ventures: 4 supported, 2 partially_supported (legal_entities[0],
  type), 0 unsupported/contradicted/unverifiable.
  1. The only activity item (Dataddo, 2023-12-20) is real and names Impulse
  Ventures as the investor, but the deal is before the window start of
  2024-10-11, so it falls in the 24-36 month dormant band.
  2. `type` = vc is doubtful. The Seznam Zpravy article (2020) says it is an
  investment company, not a fund, investing only Ondřej Tomek's own money. So
  `role` = management_company is also unsupported.
  Opinion: no (dormant). File: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/impulse-ventures.json

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-13,evidence-verifier,opus,i-and-i-biotech,20220,10,43.1,ok" >>
      data/runs/run_log.csv; pyth…)
  ⎿  40 remaining: ip-lab-ventures
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      125  2026-10-13,evidence-verifier,opus,gi21-capital,18457,9,32.5,ok
      126  2026-10-13,evidence-verifier,opus,fazole-ventures,18306,8,42.8
           ,ok
      127  2026-10-13,evidence-verifier,opus,i-and-i-prague,14599,6,23.8,
           ok
      128 +2026-10-13,evidence-verifier,opus,i-and-i-biotech,20220,10,43.
          +1,ok                                                          

⏺ evidence-verifier(Verify ip-lab-ventures)
  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)

⏺ Agent "Verify impulse-ventures" finished · 33s

› Message from evidence-verifier
  incomming-ventures: 3 supported, 3 partially supported, 1 unverifiable, 0
  unsupported or contradicted.
  1. The only activity evidence (the CARZADA deal) is from 2016-05-18, about 10
  years before AS_OF. It counts as neither active nor dormant, so my opinion is
  "no".
  2. The cited quotes for type and sectors don't state VC or e-commerce. Only
  other text on the Altss page (a tier-3 aggregator) does. The 2016 article says
  there was no announced industry focus.
  3. The exclusion signal cites no source, and the legal entity is matched by
  name only.
  File: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/incomming-ventures.json

⏺ Agent "Verify incomming-ventures" finished · 33s
⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && printf '%s\n'
      "2026-10-13,evidence-verifier,opus,impulse-ventures,17856,8,33.4,ok"
      "2026-10-13,evidence-…)
  ⎿  39 remaining: j-t-ventures jic-ventures
  ⎿  Updated data/runs/run_log.csv (+2 -0)
      126  2026-10-13,evidence-verifier,opus,fazole-ventures,18306,8,42.8
           ,ok
      127  2026-10-13,evidence-verifier,opus,i-and-i-prague,14599,6,23.8,
           ok
      128  2026-10-13,evidence-verifier,opus,i-and-i-biotech,20220,10,43.
           1,ok
      129 +2026-10-13,evidence-verifier,opus,impulse-ventures,17856,8,33.
          +4,ok                                                          
      130 +2026-10-13,evidence-verifier,opus,incomming-ventures,16735,8,3
          +3.2,ok                                                        

⏺ 2 background agents launched (↓ to manage)
   ├ Verify j-t-ventures
   └ Verify jic-ventures

⏺ Verification is at 28 of 69. The four running now are Inven Capital, IP Lab
  Ventures, J&T Ventures and JIC Ventures; 37 more are waiting.

✻ Worked for 18s · done 4:07 PM

› Message from evidence-verifier
  inven-capital: 7 supported, 1 partially_supported, 0 unsupported, 0
  contradicted, 0 unverifiable.
  1. capital: the site says "we invest EUR 500m" but never calls it a fund size,
  so the label "latest_fund_size" is not supported. It reads more like total
  capital managed.
  2. evidence_of_activity[0] (Wint): the page has no printed date. The
  2026-09-11 date comes only from the URL ("Hace un mes" on the page fits). The
  source is tier 3.
  Also: evidence_of_activity[1] (Vytal) gave 403 to the quote script but loaded
  for me, and the exact quote is there, published 2025-03-12. The site's ČEZ
  footer hints at corporate VC, but no source says so.
  File: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/inven-capital.json

⏺ Inven Capital is verified: 7 of 8 items supported. The verifier flagged the
  EUR 500m capital label and the Wint deal date, which comes only from the URL.
  It did not catch the co_lead role taken from a search snippet (E-13), so
  that's a verifier miss to note for the README. I'll log the run once its usage
  arrives.

✻ Cooked for 3s · done 4:07 PM

⏺ Agent "Verify inven-capital" finished · 32s

› Message from evidence-verifier
  ip-lab-ventures: 3 supported, 2 partially_supported (0 unsupported, 0
  contradicted, 0 unverifiable). Written to /Users/davidkoktavy/Desktop/Investor
  DB Starter/data/verification/ip-lab-ventures.json. Record opinion: unsure.
  1. evidence_of_activity[0] (MendelFOLD) has no date, round or amount, and the
  source credits IP Lab the venture builder, not the fund. So nothing places
  activity in the 24-month window.
  2. funds[0]: the EUR 40m is a target size, newly announced Sep 2026. The
  source states no first or final close.
  3. hq_country is null, and the only source never says where the team is based.
  Type vc is inferred: the source never says outright that IP Lab Ventures
  manages the fund.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-13,evidence-verifier,opus,inven-capital,17281,9,32.7,ok" >>
      data/runs/run_log.csv; python3…)
  ⎿  37 remaining: jsk-investments
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      128  2026-10-13,evidence-verifier,opus,i-and-i-biotech,20220,10,43.
           1,ok
      129  2026-10-13,evidence-verifier,opus,impulse-ventures,17856,8,33.
           4,ok
      130  2026-10-13,evidence-verifier,opus,incomming-ventures,16735,8,3
           3.2,ok
      131 +2026-10-13,evidence-verifier,opus,inven-capital,17281,9,32.7,o
          +k                                                             

⏺ evidence-verifier(Verify jsk-investments)
  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)

⏺ Agent "Verify ip-lab-ventures" finished · 41s

› Message from evidence-verifier
  j-t-ventures: 8 supported, 1 partially_supported, 0 unsupported, 0
  contradicted, 0 unverifiable. Opinion: yes, an active Czech VC.
  - evidence_of_activity[2] (AEOS, 2024-10-07) falls 4 days before the 24-month
  window, which starts 2024-10-11, so it can't count toward K2. The record also
  leaves round as null, but the page says Series B.
  - Two deals inside the window are supported: Definic (lead, 2026-06-13) and
  Wultra (participant, 2026-06-29).
  Output: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/j-t-ventures.json

⏺ Agent "Verify j-t-ventures" finished · 33s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && printf '%s\n'
      "2026-10-13,evidence-verifier,opus,ip-lab-ventures,17623,6,41.9,ok"
      "2026-10-13,evidence-v…)
  ⎿  36 remaining: kaya-vc koopeo-ventures
  ⎿  Updated data/runs/run_log.csv (+2 -0)
      129  2026-10-13,evidence-verifier,opus,impulse-ventures,17856,8,33.
           4,ok
      130  2026-10-13,evidence-verifier,opus,incomming-ventures,16735,8,3
           3.2,ok
      131  2026-10-13,evidence-verifier,opus,inven-capital,17281,9,32.7,o
           k
      132 +2026-10-13,evidence-verifier,opus,ip-lab-ventures,17623,6,41.9
          +,ok                                                           
      133 +2026-10-13,evidence-verifier,opus,j-t-ventures,18740,10,33.5,o
          +k                                                             

⏺ 2 background agents launched (↓ to manage)
   ├ Verify kaya-vc
   └ Verify koopeo-ventures

› Message from evidence-verifier
  jic-ventures: 11 supported, 0 partially_supported, 0 unsupported, 0
  contradicted, 0 unverifiable.
  Serious problems: none. All three activity items are new rounds within the
  24-month window (Elredo lead, 2026-10-01; FaceUp, 2026-05-19; Aiviro,
  2025-12-16).
  Minor: legal entity JIC Ventures 2 a.s. is not explicitly linked to the fund
  on any cited page (role is 'other', which is correct). The fund is not finally
  closed (close: unknown).
  Opinion: yes, an active CZ VC with its team in Brno.
  File: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/jic-ventures.json

⏺ Agent "Verify jic-ventures" finished · 39s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-13,evidence-verifier,opus,jic-ventures,21667,12,39.9,ok" >>
      data/runs/run_log.csv && git a…)
  ⎿  34 remaining: lighthouse-ventures
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      131  2026-10-13,evidence-verifier,opus,inven-capital,17281,9,32.7,o
           k
      132  2026-10-13,evidence-verifier,opus,ip-lab-ventures,17623,6,41.9
           ,ok
      133  2026-10-13,evidence-verifier,opus,j-t-ventures,18740,10,33.5,o
           k
      134 +2026-10-13,evidence-verifier,opus,jic-ventures,21667,12,39.9,o
          +k                                                             

⏺ evidence-verifier(Verify lighthouse-ventures)
  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)

⏺ Verification: 32 of 69 records are done and committed. Four verifiers are
  running: JSK Investments, KAYA VC, Koopeo Ventures and Lighthouse Ventures. 33
  records remain after these.

✻ Cogitated for 22s · done 4:08 PM

› Message from evidence-verifier
  koopeo-ventures: 3 supported, 1 partially supported, 0
  unsupported/contradicted/unverifiable. Written to
  /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/koopeo-ventures.json
  1. `type` = vc is only partially supported: the site just says "We invest in
  innovative startups". It names no fund and no outside capital, so this could
  be an SE investing its own money (holding-style) rather than a VC manager.
  Record opinion: unsure.
  2. The only activity item is one Tech.eu article (17 Jul 2025, inside the
  window), which names it only as "Koopeo". The name matches and its own
  portfolio page lists Trifft, so I marked it supported.

⏺ Koopeo Ventures is verified: 3 supported, 1 partially supported. Its one deal,
  Trifft (July 2025), is inside the window. Whether it's a VC fund or a company
  investing its own money stays open for your manual review. I'll log the run
  once its usage figures arrive.

✻ Sautéed for 2s · done 4:09 PM

⏺ Agent "Verify koopeo-ventures" finished · 25s

› Message from evidence-verifier
  kaya-vc: 5 supported, 3 partially_supported, 0 unsupported, 0 contradicted, 0
  unverifiable. Record opinion: unsure.
  1. hq_country: Prague is one of four offices on kaya.vc (Warszawa is listed
  first). The page names no HQ and says nothing about where the team sits, so it
  doesn't establish a Czech team.
  2. evidence_of_activity[1] (E2B, Jul 2025): the Insight Partners page names
  only "Kaya", so it's likely but not confirmed to be this investor.
  evidence_of_activity[0] (Viktor, Fortune, May 2026, "Kaya VC") is supported
  and inside the window.
  3. stages: the page says "pre-seed through to meaningful scale", so [pre_seed,
  seed] is narrower than the source.
  File: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/kaya-vc.json

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-13,evidence-verifier,opus,koopeo-ventures,15741,8,25.3,ok" >>
      data/runs/run_log.csv; pytho…)
  ⎿  33 remaining: longevitytech-fund look-ai-ventures
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      132  2026-10-13,evidence-verifier,opus,ip-lab-ventures,17623,6,41.9
           ,ok
      133  2026-10-13,evidence-verifier,opus,j-t-ventures,18740,10,33.5,o
           k
      134  2026-10-13,evidence-verifier,opus,jic-ventures,21667,12,39.9,o
           k
      135 +2026-10-13,evidence-verifier,opus,koopeo-ventures,15741,8,25.3
          +,ok                                                           

⏺ evidence-verifier(Verify longevitytech-fund)
  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)

⏺ Agent "Verify kaya-vc" finished · 32s

› Message from evidence-verifier
  jsk-investments: 6 supported, 4 partially_supported, 0
  unsupported/contradicted/unverifiable. Opinion: yes. Written to
  /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/jsk-investments.json
  1. `type` = vc is only partly right: the SICAV is multi-strategy (a PE/growth
  fund taking majority stakes, a VC fund, a family-business fund).
  2. `sectors` come from the Private & Growth Equity fund, not the VC fund.
  `stages` pre_seed/seed is the extractor's reading of "early stage"; the page
  doesn't say it.
  3. `funds[0]` and `capital` give CZK 2bn for the whole umbrella SICAV. The
  fund name comes from ARES, not the cited article.

⏺ Agent "Verify jsk-investments" finished · 42s
› Message from evidence-verifier
  lighthouse-ventures: 8 supported, 0 partially_supported, 0 unsupported, 0
  contradicted, 0 unverifiable. Opinion: yes, an active Czech VC.
  No serious problems. Two small caveats:
  1. The `general_partner` role in `legal_entities[0]` is inferred from "GP" in
  the company name. The registry page doesn't state the role.
  2. The Outfindo article shows only "Updated January 20, 2025", not an original
  publish date. That date is still inside the window.
  Written to /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/lighthouse-ventures.json

⏺ Agent "Verify lighthouse-ventures" finished · 29s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && printf '%s\n'
      "2026-10-13,evidence-verifier,opus,kaya-vc,17670,8,32.7,ok"
      "2026-10-13,evidence-verifier,…)
  ⎿  32 remaining: look-ai-ventures metatron-global miton
  ⎿  Updated data/runs/run_log.csv (+3 -0)
      133  2026-10-13,evidence-verifier,opus,j-t-ventures,18740,10,33.5,o
           k
      134  2026-10-13,evidence-verifier,opus,jic-ventures,21667,12,39.9,o
           k
      135  2026-10-13,evidence-verifier,opus,koopeo-ventures,15741,8,25.3
           ,ok
      136 +2026-10-13,evidence-verifier,opus,kaya-vc,17670,8,32.7,ok     
      137 +2026-10-13,evidence-verifier,opus,jsk-investments,21399,10,42.
          +0,ok                                                          
      138 +2026-10-13,evidence-verifier,opus,lighthouse-ventures,18173,11
          +,29.4,ok                                                      

⏺ 3 background agents launched (↓ to manage)
   ├ Verify look-ai-ventures
   ├ Verify metatron-global
   └ Verify miton

⏺ R6 is at 36 of 69 verified. Four verifiers are running now: Longevitytech,
  Look AI, Metatron and Miton. 29 records are still queued after these.

✻ Brewed for 19s · done 4:09 PM

› Message from evidence-verifier
  metatron-global: 1 item checked, 1 partially_supported. Opinion: no. Written
  to /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/metatron-global.json
  1. evidence_of_activity[0] (il Dolomiti, Ticketoo round): the quote is on the
  page, but the article names only "Metatron", with nothing tying it to Metatron
  Global or Czechia.
  2. The deal date, 2024-01-17, is before the 24-month window start of
  2024-10-11, so it falls in the dormant band.
  3. Type, HQ and website are all null, so the record has no sourced evidence of
  a VC with a team in Czechia.

⏺ Metatron Global is verified. Its only deal predates the 24-month window, and
  nothing ties it to a Czech team, so it won't qualify. Three verifiers are
  still running.

✻ Baked for 1s · done 4:09 PM

⏺ Agent "Verify metatron-global" finished · 20s

› Message from evidence-verifier
  longevitytech-fund: 3 supported (`stages`, `evidence_of_activity[0]`,
  `evidence_of_activity[1]`), 0 partially supported, 0 unsupported, 0
  contradicted, 0 unverifiable. Overall opinion: unsure.
  1. Team country is unresolved. `hq_country` is null and neither cited page
  says where the fund is based, so nothing in the record backs a Czech team.
  2. `evidence_of_activity[1]` (Occuity, 2021-09-27) is real but older than both
  the 24- and 36-month windows. Only the Klothea Bio lead seed round
  (2024-11-25) falls inside the window. That release does not say "equity".
  3. Minor label issue: the `stages` quote comes from the fund's own "About"
  text in a press release, so `self_reported` should arguably be true.
  File: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/longevitytech-fund.json

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-13,evidence-verifier,opus,metatron-global,13611,6,20.1,ok" >>
      data/runs/run_log.csv; pytho…)
  ⎿  29 remaining: muni-ventures nation1
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      136  2026-10-13,evidence-verifier,opus,kaya-vc,17670,8,32.7,ok
      137  2026-10-13,evidence-verifier,opus,jsk-investments,21399,10,42.
           0,ok
      138  2026-10-13,evidence-verifier,opus,lighthouse-ventures,18173,11
           ,29.4,ok
      139 +2026-10-13,evidence-verifier,opus,metatron-global,13611,6,20.1
          +,ok                                                           

⏺ evidence-verifier(Verify muni-ventures)
  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)

⏺ Agent "Verify longevitytech-fund" finished · 39s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-13,evidence-verifier,opus,longevitytech-fund,16890,7,39.6,ok" >>
      data/runs/run_log.csv)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      137  2026-10-13,evidence-verifier,opus,jsk-investments,21399,10,42.
           0,ok
      138  2026-10-13,evidence-verifier,opus,lighthouse-ventures,18173,11
           ,29.4,ok
      139  2026-10-13,evidence-verifier,opus,metatron-global,13611,6,20.1
           ,ok
      140 +2026-10-13,evidence-verifier,opus,longevitytech-fund,16890,7,3
          +9.6,ok                                                        

⏺ evidence-verifier(Verify nation1)
  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)

› Message from evidence-verifier
  miton: 3 supported, 4 partially_supported, 0 unsupported, 0 contradicted, 0
  unverifiable. Written to /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/miton.json
  1. Type "vc" is uncertain. Miton invests its own money with no fund cycle and
  calls itself "VC, ale ne tak úplně" ("VC, but not quite"). It could just as
  well be a private holding. Record opinion: unsure.
  2. The sector and stage values are right, but their quotes don't state them.
  Both pages list them elsewhere.
  3. legal_entities[0] role "management_company" is not supported: per the
  finmag.cz registry mirror, MITON CZ invests and holds its own assets and
  manages no fund.

⏺ Agent "Verify miton" finished · 36s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-13,evidence-verifier,opus,miton,18285,9,36.4,ok" >>
      data/runs/run_log.csv && git add -A &&…)
  ⎿  27 remaining: novira-capital
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      138  2026-10-13,evidence-verifier,opus,lighthouse-ventures,18173,11
           ,29.4,ok
      139  2026-10-13,evidence-verifier,opus,metatron-global,13611,6,20.1
           ,ok
      140  2026-10-13,evidence-verifier,opus,longevitytech-fund,16890,7,3
           9.6,ok
      141 +2026-10-13,evidence-verifier,opus,miton,18285,9,36.4,ok       

⏺ evidence-verifier(Verify novira-capital)
  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)

› Message from evidence-verifier
  look-ai-ventures: 9 supported, 1 partially_supported, 1 unverifiable, 0
  unsupported/contradicted. Opinion: yes, active VC with its team in CZ.
  1. funds[0]: the name "Look AI Ventures I Subfund" is not on the cited tech.eu
  page; the EUR 20M target is supported.
  2. legal_entities[0]: or.justice.cz is blocked by robots.txt, so it was not
  checked.
  3. Ticket (EUR 250k) and fund size come from a 2023 launch-target article; the
  Dec 2025 Digicust deal (EUR 250k) is consistent.
  File: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/look-ai-ventures.json

⏺ Agent "Verify look-ai-ventures" finished · 39s

⏺ Look AI Ventures is confirmed as an active Czech VC, but I couldn't verify its
  legal entity since or.justice.cz also blocks fetching via robots.txt—so E-18
  extends beyond just kurzy.cz. I'll update that entry before R7.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-13,evidence-verifier,opus,look-ai-ventures,20050,10,39.1,ok" >>
      data/runs/run_log.csv; pyt…)
  ⎿  26 remaining: odyssey-44
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      139  2026-10-13,evidence-verifier,opus,metatron-global,13611,6,20.1
           ,ok
      140  2026-10-13,evidence-verifier,opus,longevitytech-fund,16890,7,3
           9.6,ok
      141  2026-10-13,evidence-verifier,opus,miton,18285,9,36.4,ok
      142 +2026-10-13,evidence-verifier,opus,look-ai-ventures,20050,10,39
          +.1,ok                                                         

⏺ evidence-verifier(Verify odyssey-44)
  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)

⏺ Verification is 42 of 69 done. Running now: MUNI Ventures, N1 Ventures, Novira
  Capital and Odyssey 44. 23 records are left after these.

✻ Crunched for 26s · done 4:10 PM

› Message from evidence-verifier
  muni-ventures: 1 supported, 1 partially supported, 0 unsupported, 0
  contradicted, 0 unverifiable (2 items).
  1. exclusion_signals[0] `grant_or_program_only` is only partly backed. The
  2024-04-25 university article does describe a technology-transfer vehicle, but
  it also says MUNI Ventures may put money into investment funds for the
  university, support spin-offs and fund development of discoveries. It never
  says the company only gives grants or runs programmes.
  Opinion: not an active VC (`no`). It is a Brno university commercialisation
  company with no equity investment shown in the cited sources.
  Output: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/muni-ventures.json

⏺ MUNI Ventures is verified: a Brno university commercialisation company with no
  equity investment in its sources, so it should drop out. The grant-only
  exclusion code is only partly backed. Three verifiers are still running.

✻ Cooked for 2s · done 4:10 PM

⏺ Agent "Verify muni-ventures" finished · 25s
› Message from evidence-verifier
  nation1: 4 supported, 1 partially supported, 0 unsupported, 0 contradicted, 0
  unverifiable. Overall opinion: unsure.
  1. hq_country is only partially supported. Lupa calls N1 a "Czech investment
  fund" but never says where the team works. The site lists offices in SF,
  Prague and Luxembourg, the funds are Luxembourg AIFs, and the firm says it has
  "one foot in Europe and the other in San Francisco".
  2. The other items check out. Flick seed deal (Lupa, 15 May 2026, in the
  window): N1 is a participant, not the lead. USD 60M is reported AUM across two
  funds.
  Written to /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/nation1.json

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-13,evidence-verifier,opus,muni-ventures,14941,7,25.9,ok" >>
      data/runs/run_log.csv; python3…)
  ⎿  25 remaining: orbit-capital patero
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      140  2026-10-13,evidence-verifier,opus,longevitytech-fund,16890,7,3
           9.6,ok
      141  2026-10-13,evidence-verifier,opus,miton,18285,9,36.4,ok
      142  2026-10-13,evidence-verifier,opus,look-ai-ventures,20050,10,39
           .1,ok
      143 +2026-10-13,evidence-verifier,opus,muni-ventures,14941,7,25.9,o
          +k                                                             

⏺ evidence-verifier(Verify orbit-capital)
  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)

⏺ Agent "Verify nation1" finished · 27s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-13,evidence-verifier,opus,nation1,16106,8,27.9,ok" >>
      data/runs/run_log.csv && git add -A…)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      141  2026-10-13,evidence-verifier,opus,miton,18285,9,36.4,ok
      142  2026-10-13,evidence-verifier,opus,look-ai-ventures,20050,10,39
           .1,ok
      143  2026-10-13,evidence-verifier,opus,muni-ventures,14941,7,25.9,o
           k
      144 +2026-10-13,evidence-verifier,opus,nation1,16106,8,27.9,ok     

⏺ evidence-verifier(Verify patero)
  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)

⏺ R6 progress: 44 of 69 records are verified and committed. Four verifiers are
  running now: Novira Capital, Odyssey 44, Orbit Capital and Patero. That leaves
  21 after these.

✻ Brewed for 13s · done 4:10 PM

› Message from evidence-verifier
  novira-capital: 1 supported, 2 partially_supported, 0
  unsupported/contradicted/unverifiable. Opinion: no. Novira's own site (script
  got HTTP 401, I read it myself) says "We are not a VC": a group in Zurich/Zug
  with ~70% of its capital in real estate.
  1. evidence_of_activity[0]: Novira did invest in Smartlook, but in 2020. The
  cited article (2023-09-12) looks back on the 2023 exit. That is outside both
  the 24-month and the 36-month window.
  2. exclusion_signals[0]: the code is real_estate_only, but the source says
  ~70% real estate, not 100%.
  File: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/novira-capital.json

⏺ Novira Capital is verified and will drop out: its own site says "We are not a
  VC". Two problems in the record:
  - The cited article is a 2023 exit recap of a 2020 investment, so the activity
    date is wrong.
  - The real_estate_only exclusion code is overstated; the source says only
    about 70% of its capital is in real estate.

  Three verifiers are still running.

✻ Cogitated for 2s · done 4:10 PM

⏺ Agent "Verify novira-capital" finished · 38s

⏺ Agent "Verify odyssey-44" finished · 33s

› Message from evidence-verifier
  odyssey-44: 5 items checked: 5 supported, 0 partially_supported, 0
  unsupported, 0 contradicted, 0 unverifiable.
  1. Not a VC. Its own site calls it a family office, says "We do not invest
  into start-ups" and sets a minimum ticket of €20m equity. My advisory opinion
  is "no".
  2. The only activity item is old. It is the FlixMobility deal from 9 Aug 2019
  (CC.cz), which is outside both the 24- and 36-month windows before AS_OF.
  3. Minor: the IČO comes only from the firm's own site footer and is not
  checked against the registry. The role "management_company" is a loose label
  for the family office entity.
  Output: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/odyssey-44.json

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && printf '%s\n'
      "2026-10-13,evidence-verifier,opus,novira-capital,15943,7,38.9,ok"
      "2026-10-13,evidence-ve…)
  ⎿  23 remaining: pilulka-lab presto-ventures
  ⎿  Updated data/runs/run_log.csv (+2 -0)
      142  2026-10-13,evidence-verifier,opus,look-ai-ventures,20050,10,39
           .1,ok
      143  2026-10-13,evidence-verifier,opus,muni-ventures,14941,7,25.9,o
           k
      144  2026-10-13,evidence-verifier,opus,nation1,16106,8,27.9,ok
      145 +2026-10-13,evidence-verifier,opus,novira-capital,15943,7,38.9,
          +ok                                                            
      146 +2026-10-13,evidence-verifier,opus,odyssey-44,16182,7,33.9,ok  

⏺ 2 background agents launched (↓ to manage)
   ├ Verify pilulka-lab
   └ Verify presto-ventures

⏺ Verification is at 46 of 69. Novira Capital and Odyssey 44 are done; both will
  drop out as not VC. Four verifiers are running: Orbit Capital, Patero,
  Pilulka Lab and Presto Ventures. After these, 19 remain.

✻ Sautéed for 9s · done 4:11 PM

› Message from evidence-verifier
  patero: 3 supported, 1 partially_supported, 0 unsupported, 0 contradicted, 0
  unverifiable.
  1. evidence_of_activity[1] (Flowpay, 2024-03-20) falls before the window start
  of 2024-10-11, so it is outside the 24-month window. The extractor's note
  says it is "within 24", which is wrong.
  2. Only Flowlance (2024-11-28) is in the window, so the record depends on one
  deal.
  3. type is null, and Patero's site describes a startup-investor group, not a
  VC fund. My opinion: unsure.
  Output: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/patero.json

⏺ Patero is verified, but it now rests on a single in-window deal (Flowlance,
  Nov 2024), and its type is unclear, so the verifier is unsure. The verifier
  also confirmed the window miscount I logged as E-15. Three verifiers are still
  running.

✻ Cogitated for 2s · done 4:11 PM

⏺ Agent "Verify patero" finished · 28s

› Message from evidence-verifier
  orbit-capital: 4 supported, 5 partially_supported, 0 unsupported, 0
  contradicted, 0 unverifiable.
  1. The cited pages show it is a debt investor, not VC. The only evidenced fund
  is a debt fund (Growth Debt Fund II, EUR 107m, second close), and Orbit's
  part of the IAG deal (2026-06-02, inside the window) looks like the debt part.
  The "vc" type and the "debt_only" signal are both only partly supported.
  2. hq_country=CZ rests on Vestbee's "Czech-Polish" wording only. No source
  states a city or where the team sits.
  3. legal_entities[0]: IČO 08223467 was named Orbit Capital SICAV until Nov
  2023. It is now Conseq-Orbit SICAV, run by Conseq Funds, so the link to
  today's Orbit manager isn't shown.
  Written to /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/orbit-capital.json

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-13,evidence-verifier,opus,patero,16132,8,28.3,ok" >>
      data/runs/run_log.csv; python3 /priva…)
  ⎿  21 remaining: purple-ventures purposetech
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      144  2026-10-13,evidence-verifier,opus,nation1,16106,8,27.9,ok
      145  2026-10-13,evidence-verifier,opus,novira-capital,15943,7,38.9,
           ok
      146  2026-10-13,evidence-verifier,opus,odyssey-44,16182,7,33.9,ok
      147 +2026-10-13,evidence-verifier,opus,patero,16132,8,28.3,ok      

⏺ evidence-verifier(Verify purple-ventures)
  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)

⏺ Agent "Verify orbit-capital" finished · 39s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-13,evidence-verifier,opus,orbit-capital,19512,9,39.2,ok" >>
      data/runs/run_log.csv && git a…)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      145  2026-10-13,evidence-verifier,opus,novira-capital,15943,7,38.9,
           ok
      146  2026-10-13,evidence-verifier,opus,odyssey-44,16182,7,33.9,ok
      147  2026-10-13,evidence-verifier,opus,patero,16132,8,28.3,ok
      148 +2026-10-13,evidence-verifier,opus,orbit-capital,19512,9,39.2,o
          +k                                                             
  ⎿  Created data/verification/pilulka-lab.json (+35 -0)
       1 +{                                                              
       2 +  "id": "pilulka-lab",                                         
       3 +  "verified_at": "2026-10-13T16:30:00+02:00",                  
       4 +  "verifier": "evidence-verifier/opus",                        
       5 +  "items": [                                                   
       6 +    {                                                          
       7 +      "path": "type",                                          
       8 +      "verdict": "partially_supported",                        
       9 +      "reason": "The article calls Pilulka Lab an 'Akcelerátor'
         + that online pharmacy Pilulka and StartupYard opened together a
         +nd that takes equity (7% of Carebot). That supports a corporate
         +-backed accelerator. The cited quote only says 'accelerator', n
         +ot that it is a CVC.",                                         
      10 +      "observed_value": "accelerator"                          
      11 +    },                                                         
      12 +    {                                                          
      13 +      "path": "evidence_of_activity[0]",                       
      14 +      "verdict": "partially_supported",                        
      15 +      "reason": "The article dated 22.3.2024 lists 'inovační la
         +boratoř Pilulka Lab' under 'Kdo investuje' in Carebot's EUR 1.2
         +M round, so the deal itself is supported. But 2024-03-22 is bef
         +ore the 24-month window start (2024-10-11), so it is not eviden
         +ce of activity in the window. It falls in the 24-36 month dorma
         +nt band.",                                                     
      16 +      "observed_value": null                                   
      17 +    },                                                         
      18 +    {                                                          
      19 +      "path": "evidence_of_activity[1]",                       
      20 +      "verdict": "partially_supported",                        
      21 +      "reason": "The article dated 2021-12-06 says the accelera
         +tor got a 7% minority stake in Carebot for 'jednotky milionů ko
         +run', so the deal is supported. It is far outside both the 24-m
         +onth and 36-month windows before AS_OF 2026-10-11.",           
      22 +      "observed_value": null                                   
      23 +    },                                                         
      24 +    {                                                          
      25 +      "path": "exclusion_signals[0]",                          
      26 +      "verdict": "unverifiable",                               
      27 +      "reason": "No source URL is cited for this signal. The cl
         +aimed redirect from pilulkalab.cz to startupyard.com cannot be 
         +checked from the cited pages. Neither cited article says where 
         +Pilulka Lab is based or whether it is still active.",          
      28 +      "observed_value": null                                   
      29 +    }                                                          
      30 +  ],                                                           
      31 +  "record_opinion": {                                          
      32 +    "active_investor_of_claimed_type": "no",                   
      33 +    "reason": "The cited sources show one portfolio company (Ca
         +rebot): a 2021 stake and a follow-on listing in March 2024. Bot
         +h are outside the 24-month window. Pilulka Lab is described as 
         +an accelerator jointly run by a corporate (Pilulka) and Startup
         +Yard, not as a CVC fund. No source shows where its team is base
         +d."                                                            
      34 +  }                                                            
      35 +}                                                              

⏺ evidence-verifier(Verify purposetech)
  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)

⏺ R6 verification is at 48 of 69 records, committed and pushed. Four verifiers
  are running: Pilulka Lab, Presto Ventures, Purple Ventures and PurposeTech. 17
  records remain after these.

✻ Worked for 13s · done 4:11 PM

› Message from evidence-verifier
  pilulka-lab: 0 supported, 3 partially_supported, 1 unverifiable (exclusion
  signal, which cites no source); 0 unsupported or contradicted. Written to
  /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/pilulka-lab.json
  1. No activity in the window. Both Carebot deals (2024-03-22 and 2021-12-06)
  fall before the window start of 2024-10-11; the 2024 one is in the dormant
  band.
  2. The page supports "accelerator" (opened by Pilulka and StartupYard), not
  "cvc"; the cited quote never says CVC.
  3. No HQ or team country in any cited source. Record opinion: no.
⏺ Pilulka Lab is verified and won't qualify: it has no deals in the window and
  no team country, and the sources support "accelerator" rather than "cvc".
  Three verifiers are still running.

✻ Baked for 2s · done 4:11 PM

⏺ Agent "Verify pilulka-lab" finished · 29s

› Message from evidence-verifier
  presto-ventures: 8 supported, 1 partially_supported (funds[0]), 0 unsupported,
  0 contradicted, 0 unverifiable. Opinion: yes, an active VC investor based in
  Prague.
  1. funds[0]: the Tech.eu article only says the fund "is investing €150
  million". It does not support close="target" or vintage 2024.
  2. The record name "Presto Tech Horizons" mixes up the manager (Presto
  Ventures) and its fund brand. The legal entity is the Fund II vehicle, not the
  Tech Horizons vehicle.
  3. Two activity items (Oct 2024) are only about 2 weeks inside the window
  start (2024-10-11). The Occam deal (Feb 2026) is the solid one.
  File: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/presto-ventures.json

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && printf '%s\n'
      "2026-10-13,evidence-verifier,opus,pilulka-lab,16129,7,29.7,ok"
      "2026-10-13,evidence-verif…)
  ⎿  19 remaining: reflex-capital rockaway-capital
  ⎿  Updated data/runs/run_log.csv (+2 -0)
      146  2026-10-13,evidence-verifier,opus,odyssey-44,16182,7,33.9,ok
      147  2026-10-13,evidence-verifier,opus,patero,16132,8,28.3,ok
      148  2026-10-13,evidence-verifier,opus,orbit-capital,19512,9,39.2,o
           k
      149 +2026-10-13,evidence-verifier,opus,pilulka-lab,16129,7,29.7,ok 
      150 +2026-10-13,evidence-verifier,opus,presto-ventures,,,,ok       

⏺ 2 background agents launched (↓ to manage)
   ├ Verify reflex-capital
   └ Verify rockaway-capital

⏺ Agent "Verify presto-ventures" finished · 40s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && sed -i ''
      's/^2026-10-13,evidence-verifier,opus,presto-ventures,,,,ok$/2026-10-13,ev
      idence-verifier,opus…)
  ⎿  2026-10-13,evidence-verifier,opus,presto-ventures,20253,10,40.9,ok
  ⎿  Updated data/runs/run_log.csv (+1 -1)
      147  2026-10-13,evidence-verifier,opus,patero,16132,8,28.3,ok
      148  2026-10-13,evidence-verifier,opus,orbit-capital,19512,9,39.2,o
           k
      149  2026-10-13,evidence-verifier,opus,pilulka-lab,16129,7,29.7,ok
      150 -2026-10-13,evidence-verifier,opus,presto-ventures,,,,ok       
      150 +2026-10-13,evidence-verifier,opus,presto-ventures,20253,10,40.
          +9,ok                                                          

› Message from evidence-verifier
  purple-ventures: 6 supported, 1 partially supported, 0 unsupported, 0
  contradicted, 0 unverifiable. Opinion: yes, an active Czech VC.
  Main problem: funds[0]. Tech.eu supports the EUR 40M fund (June 2024) but
  never calls it "Fund II" and doesn't say whether it is a first close, final
  close or target. The site says Fund II raised "over CZK 700 million" and
  doesn't say how that relates to the EUR 40M fund.
  Minor: hq_country rests on the legal footer address in Brno. One partner is
  based in Prague and one in Utrecht, so the team location is never stated
  directly.
  Written to /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/purple-ventures.json

⏺ Agent "Verify purple-ventures" finished · 29s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-13,evidence-verifier,opus,purple-ventures,17946,9,29.8,ok" >>
      data/runs/run_log.csv && git…)
  ⎿  17 remaining: rockaway-ventures
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      148  2026-10-13,evidence-verifier,opus,orbit-capital,19512,9,39.2,o
           k
      149  2026-10-13,evidence-verifier,opus,pilulka-lab,16129,7,29.7,ok
      150  2026-10-13,evidence-verifier,opus,presto-ventures,20253,10,40.
           9,ok
      151 +2026-10-13,evidence-verifier,opus,purple-ventures,17946,9,29.8
          +,ok                                                           

⏺ evidence-verifier(Verify rockaway-ventures)
  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)

› Message from evidence-verifier
  purposetech: all 6 items are supported (0 partially_supported, 0 unsupported,
  0 contradicted, 0 unverifiable).
  Problems: none serious. Two minor ones:
  1. The Czech team location rests only on the Prague mailing address on the
  investor's own site. The CzechCrunch article does not say where the team is.
  2. The ticket is left null, but CzechCrunch states EUR 0.5-1m per company for
  the new fund (PT Capital, PurposeTech's second fund). The extractor chose not
  to treat that as a ticket.
  Record opinion: yes, an active Czech VC.
  File: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/purposetech.json

⏺ Agent "Verify purposetech" finished · 29s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-13,evidence-verifier,opus,purposetech,16856,8,29.2,ok" >>
      data/runs/run_log.csv; python3 /…)
  ⎿  16 remaining: rockawayx
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      149  2026-10-13,evidence-verifier,opus,pilulka-lab,16129,7,29.7,ok
      150  2026-10-13,evidence-verifier,opus,presto-ventures,20253,10,40.
           9,ok
      151  2026-10-13,evidence-verifier,opus,purple-ventures,17946,9,29.8
           ,ok
      152 +2026-10-13,evidence-verifier,opus,purposetech,16856,8,29.2,ok 

⏺ evidence-verifier(Verify rockawayx)
  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)

⏺ Verification is at 53 of 69. Running now: Reflex Capital, Rockaway Capital,
  Rockaway Ventures and RockawayX. 12 remain after these.

✻ Brewed for 25s · done 4:12 PM

› Message from evidence-verifier
  reflex-capital: 4 supported, 2 partially supported, 0 unsupported,
  contradicted or unverifiable.
  1. `type` "vc" is inferred: the cited page calls it only a "Czech fund", and
  the homepage has no VC label either.
  2. `evidence_of_activity[2]` (Boataround, 2024-06-10) is before the window
  start of 2024-10-11; the two 2026 deals are in the window.
  3. Merchantee's `round` says "pre-seed", which is not in the cited source.
  Also, the San Francisco office leaves the team's country slightly uncertain.
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/reflex-capital.json

⏺ Reflex Capital is verified: 4 supported, 2 partially supported. Its two 2026
  deals are inside the window; only the "VC" type label and the Merchantee round
  stage are inferred rather than stated. Three verifiers are still running.

✻ Baked for 2s · done 4:12 PM

⏺ Agent "Verify reflex-capital" finished · 30s

› Message from evidence-verifier
  rockaway-capital: 3 supported, 3 partially_supported, 0 unsupported, 0
  contradicted, 0 unverifiable.
  1. Neither activity item is a Rockaway Capital deal: Apptronik (13 Feb 2026)
  was Rockaway Ventures and Wonderful was United Founders, both subsidiaries
  with their own records.
  2. Wonderful is an undated seed deal recapped in a 3 Sep 2026 post, so it
  cannot be placed in the window.
  3. funds[0] vintage 2026 is inferred from the article date; the article does
  not state it.
  Opinion: unsure. Prague group holding, not itself a VC manager. File:
  /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/rockaway-capital.json

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && printf '%s\n'
      "2026-10-13,evidence-verifier,opus,reflex-capital,17198,9,30.8,ok"
      "2026-10-13,evidence-ve…)
  ⎿  15 remaining: seed-starter soulmates-ventures
  ⎿  Updated data/runs/run_log.csv (+2 -0)
      150  2026-10-13,evidence-verifier,opus,presto-ventures,20253,10,40.
           9,ok
      151  2026-10-13,evidence-verifier,opus,purple-ventures,17946,9,29.8
           ,ok
      152  2026-10-13,evidence-verifier,opus,purposetech,16856,8,29.2,ok
      153 +2026-10-13,evidence-verifier,opus,reflex-capital,17198,9,30.8,
          +ok                                                            
      154 +2026-10-13,evidence-verifier,opus,rockaway-capital,,,,ok      

⏺ 2 background agents launched (↓ to manage)
   ├ Verify seed-starter
   └ Verify soulmates-ventures

⏺ Agent "Verify rockaway-capital" finished · 37s

› Message from evidence-verifier
  rockaway-ventures: 7 supported, 0 partially_supported, 0 unsupported, 0
  contradicted, 0 unverifiable. Record opinion: yes.
  No serious problems. Two minor caveats:
  1) The contact-page address in Praha 6 is labelled Rockaway Capital (the
  parent group), not Rockaway Ventures.
  2) The sector "E-Travel & Hospitality" was not mapped to any category.
  Output: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/rockaway-ventures.json

⏺ Agent "Verify rockaway-ventures" finished · 31s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && sed -i ''
      's/^2026-10-13,evidence-verifier,opus,rockaway-capital,,,,ok$/2026-10-13,e
      vidence-verifier,opu…)
  ⎿  13 remaining: spinoffy
  ⎿  Updated data/runs/run_log.csv (+2 -1)
      151  2026-10-13,evidence-verifier,opus,purple-ventures,17946,9,29.8
           ,ok
      152  2026-10-13,evidence-verifier,opus,purposetech,16856,8,29.2,ok
      153  2026-10-13,evidence-verifier,opus,reflex-capital,17198,9,30.8,
           ok
      154 -2026-10-13,evidence-verifier,opus,rockaway-capital,,,,ok      
      154 +2026-10-13,evidence-verifier,opus,rockaway-capital,18677,9,37.
          +3,ok                                                          
      155 +2026-10-13,evidence-verifier,opus,rockaway-ventures,17972,11,3
          +1.0,ok                                                        

⏺ evidence-verifier(Verify spinoffy)
  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)

› Message from evidence-verifier
  rockawayx: 3 supported, 1 partially supported, 1 unverifiable, 0 unsupported
  or contradicted. Written to /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/rockawayx.json
  1. evidence_of_activity[0] (OnRe): I did not fetch the Edgen page because its
  robots.txt disallows it. RockawayX's own insights page lists the OnRe co-lead
  dated 2026-05-05, but the record doesn't cite that page for this item.
  2. type "vc" is only partly supported: RockawayX is a crypto firm that also
  runs yield, liquidity and blockchain infrastructure, so it is not clearly a VC
  manager.
  3. Czech team is not shown: the site says the team of 45 is spread across
  London, Prague and Dubai. My record opinion is "unsure".
⏺ Agent "Verify rockawayx" finished · 34s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-13,evidence-verifier,opus,rockawayx,17224,8,34.9,ok" >>
      data/runs/run_log.csv; python3 /pr…)
  ⎿  12 remaining: springtide-ventures
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      153  2026-10-13,evidence-verifier,opus,reflex-capital,17198,9,30.8,
           ok
      154  2026-10-13,evidence-verifier,opus,rockaway-capital,18677,9,37.
           3,ok
      155  2026-10-13,evidence-verifier,opus,rockaway-ventures,17972,11,3
           1.0,ok
      156 +2026-10-13,evidence-verifier,opus,rockawayx,17224,8,34.9,ok   

⏺ evidence-verifier(Verify springtide-ventures)
  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)

⏺ Verification is at 57 of 69. Four verifiers are running: Seed Starter,
  Soulmates Ventures, Spinoffy and Springtide Ventures. Eight remain after them.

✻ Churned for 23s · done 4:12 PM

› Message from evidence-verifier
  spinoffy: 2 supported, 1 partially_supported, 0
  unsupported/contradicted/unverifiable (3 items). Written to
  /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/spinoffy.json
  1. No activity evidence at all: the only source is a 2026-03-02 launch article
  with no deals, no fund close and no fund size. Opinion: not an active
  investor (no).
  2. hq_country is only partially supported: the article says the fund launched
  in Czechia but never says where the team is based.
  3. Minor: sectors is null as `not_published`, but the cited article does list
  sectors (AI/cyber, robotics, materials, quantum, cleantech).

⏺ Spinoffy is verified. It has no deals and no fund close yet, only a launch
  article, so it isn't an active investor. Three verifiers are still running.

✻ Churned for 1s · done 4:13 PM

⏺ Agent "Verify spinoffy" finished · 26s

› Message from evidence-verifier
  seed-starter: 8 supported, 1 partially supported, 0 unsupported, contradicted
  or unverifiable. I opened all five cited pages once each.
  Most serious problem: the sectors value "fintech" is the extractor's reading
  of "technologies that help banking thrive"; the page gives no sector list.
  Minor: the legal entity's role (management_company) is not stated on any page.
  Opinion: yes, an active Czech CVC. Three investments (Definic, Repsense,
  Vestberry) dated Mar 2025 to Jun 2026 are all inside the 24-month window.
  File: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/seed-starter.json

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && printf '%s\n'
      "2026-10-13,evidence-verifier,opus,spinoffy,15047,6,26.2,ok"
      "2026-10-13,evidence-verifier…)
  ⎿  11 remaining: startguide-vc startupyard
  ⎿  Updated data/runs/run_log.csv (+2 -0)
      154  2026-10-13,evidence-verifier,opus,rockaway-capital,18677,9,37.
           3,ok
      155  2026-10-13,evidence-verifier,opus,rockaway-ventures,17972,11,3
           1.0,ok
      156  2026-10-13,evidence-verifier,opus,rockawayx,17224,8,34.9,ok
      157 +2026-10-13,evidence-verifier,opus,spinoffy,15047,6,26.2,ok    
      158 +2026-10-13,evidence-verifier,opus,seed-starter,,,,ok          

⏺ 2 background agents launched (↓ to manage)
   ├ Verify startguide-vc
   └ Verify startupyard

⏺ Agent "Verify seed-starter" finished · 37s

› Message from evidence-verifier
  soulmates-ventures: 10 supported, 1 partially_supported, 0 unsupported,
  contradicted or unverifiable. Written to /Users/davidkoktavy/Desktop/Investor
  DB Starter/data/verification/soulmates-ventures.json
  1. funds[0] (partially supported): the cited page confirms the EUR 50M fund.
  The "Article 9 SFDR" fund name is not in the cited quote, and vintage 2025 is
  guessed from the article date.
  2. Minor gaps, not errors: the homepage gives target stage "Seed/SA" but
  series_a is not in stages, and "circular economy" is not mapped to a sector.
  Opinion: yes. A Prague-based VC (CZ entity, IČO 09789561) that led 3 rounds
  between Oct 2025 and Sep 2026, all within the window.

⏺ Agent "Verify soulmates-ventures" finished · 38s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && sed -i ''
      's/^2026-10-13,evidence-verifier,opus,seed-starter,,,,ok$/2026-10-13,evide
      nce-verifier,opus,se…)
  ⎿  9 remaining: stredocesky-inovacni-centrum tachles
  ⎿  Updated data/runs/run_log.csv (+2 -1)
      155  2026-10-13,evidence-verifier,opus,rockaway-ventures,17972,11,3
           1.0,ok
      156  2026-10-13,evidence-verifier,opus,rockawayx,17224,8,34.9,ok
      157  2026-10-13,evidence-verifier,opus,spinoffy,15047,6,26.2,ok
      158 -2026-10-13,evidence-verifier,opus,seed-starter,,,,ok          
      158 +2026-10-13,evidence-verifier,opus,seed-starter,19280,10,37.4,o
          +k                                                             
      159 +2026-10-13,evidence-verifier,opus,soulmates-ventures,20249,12,
          +38.9,ok                                                       

⏺ 2 background agents launched (↓ to manage)
   ├ Verify stredocesky-inovacni-centrum
   └ Verify tachles

⏺ R6 is at 60 of 69 records verified, committed and pushed. Four verifiers are
  running: Springtide, Startguide, StartupYard and Středočeské inovační centrum,
  plus Tachles. Five records are still waiting after those.

✻ Baked for 19s · done 4:13 PM

› Message from evidence-verifier
  springtide-ventures: 6 supported, 2 partially_supported, 0 unsupported, 0
  contradicted, 0 unverifiable.
  1. The only deal in the window is one follow-on: an $8M convertible note into
  ThreatMark (2025-01-07), an existing portfolio company. The Source Defense
  deal (2022-04-27) is outside both the 24- and 36-month windows.
  2. hq_country: the quote names Prague, Tel-Aviv and Boston equally. Only the
  registry shows the Prague seat, and no team member's location is stated.
  3. type: 'cvc' is an interpretation. The page shows a captive arm of KKCG
  Group, which is a private investment group, not an operating company. Record
  opinion: unsure.
  File: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/springtide-ventures.json

⏺ Springtide Ventures is verified, but the verifier is unsure about it. Its only
  in-window deal is a convertible-note follow-on into ThreatMark (Jan 2025).
  Calling it a corporate VC is an interpretation: its parent, KKCG, is an
  investment group, not an operating company. It's a judgment call for your
  manual review.

✻ Churned for 2s · done 4:13 PM

⏺ Agent "Verify springtide-ventures" finished · 49s

› Message from evidence-verifier
  startupyard: 5 supported, 2 partially_supported, 0 unsupported, 0
  contradicted, 0 unverifiable.
  1. ticket: only the optional €25k cash part. Per the FAQ, the full convertible
  note is €70k (€45k in-kind + €25k cash, about 5% equity).
  2. sectors: the AI/deep-tech quote covers Batch 15 only, not the firm's
  general mandate. The cited page shows no date, so 2025-09-11 is unconfirmed.
  Opinion: yes, an active Prague accelerator; the Ydoca deal (CZK 500k,
  2025-02-14) is supported and in the window. Whether an accelerator counts as a
  VC is for decide.py to rule.
  File: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/startupyard.json

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && printf '%s\n'
      "2026-10-13,evidence-verifier,opus,springtide-ventures,20309,9,49.3,ok"
      "2026-10-13,eviden…)
  ⎿  7 remaining: tcf-capital tensor-ventures
  ⎿  Updated data/runs/run_log.csv (+2 -0)
      157  2026-10-13,evidence-verifier,opus,spinoffy,15047,6,26.2,ok
      158  2026-10-13,evidence-verifier,opus,seed-starter,19280,10,37.4,o
           k
      159  2026-10-13,evidence-verifier,opus,soulmates-ventures,20249,12,
           38.9,ok
      160 +2026-10-13,evidence-verifier,opus,springtide-ventures,20309,9,
          +49.3,ok                                                       
      161 +2026-10-13,evidence-verifier,opus,startupyard,,,,ok           

⏺ 2 background agents launched (↓ to manage)
   ├ Verify tcf-capital
   └ Verify tensor-ventures

⏺ Agent "Verify startupyard" finished · 31s

› Message from evidence-verifier
  startguide-vc: 7 supported, 1 partially_supported, 0 unsupported, 0
  contradicted, 0 unverifiable. Written to /Users/davidkoktavy/Desktop/Investor
  DB Starter/data/verification/startguide-vc.json
  1. The only activity item (Carebot, 2024-03-22) is outside the 24-month window
  (window starts 2024-10-11), so it counts only as dormant.
  2. Ticket: the record says EUR 100k–100k. The page says "okolo 100 000 Eur"
  (about EUR 100k) and also states "50-200 000 USD". This is for the SGOne fund,
  which stopped taking investments on 1 May 2023.
  Opinion: unsure, because nothing cited shows an investment in the last 24
  months.

⏺ Agent "Verify startguide-vc" finished · 32s

› Message from evidence-verifier
  All 6 items supported; 0 partially supported, unsupported, contradicted or
  unverifiable.
  Problem 1: the investor type is doubtful. This is a regional innovation agency
  (a spolek, i.e. an association) running a small programme of loans and equity
  up to EUR 80k. That is not clearly VC/CVC, and the record leaves type null.
  Record opinion: unsure.
  Problem 2: the only activity item (Elredo, 2026-10-01, in the window) names
  just "investiční program SIC". It is tied to Středočeské inovační centrum only
  by the article's tag.
  Output: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/stredocesky-inovacni-centrum.json

⏺ Agent "Verify stredocesky-inovacni-centrum" finished · 28s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && sed -i ''
      's/^2026-10-13,evidence-verifier,opus,startupyard,,,,ok$/2026-10-13,eviden
      ce-verifier,opus,sta…)
  ⎿  5 remaining: thein tilia-impact-ventures united-founders y-soft-ventur
     es zaka-vc
  ⎿  Updated data/runs/run_log.csv (+3 -1)
      158  2026-10-13,evidence-verifier,opus,seed-starter,19280,10,37.4,o
           k
      159  2026-10-13,evidence-verifier,opus,soulmates-ventures,20249,12,
           38.9,ok
      160  2026-10-13,evidence-verifier,opus,springtide-ventures,20309,9,
           49.3,ok
      161 -2026-10-13,evidence-verifier,opus,startupyard,,,,ok           
      161 +2026-10-13,evidence-verifier,opus,startupyard,17736,10,31.9,ok
      162 +2026-10-13,evidence-verifier,opus,startguide-vc,18195,8,32.4,o
          +k                                                             
      163 +2026-10-13,evidence-verifier,opus,stredocesky-inovacni-centrum
          +,16776,8,29.0,ok                                              

⏺ evidence-verifier(Verify thein)
  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)
› Message from evidence-verifier
  tachles: 2 supported, 1 partially_supported, 0
  unsupported/contradicted/unverifiable. Written to
  /Users/davidkoktavy/Desktop/Investor DB Starter/data/verification/tachles.json
  1. evidence_of_activity[0] (Hirundo): the article is a 2025-02-12 recap of
  2024 deals with no deal dates. The record's announced_date is the article
  date, so the deal may be older than the window start (2024-10-11).
  2. USD 7.6M is the total raised over two rounds, not Tachles' share; the
  record only quotes it.
  3. Team country is unclear: CzechCrunch calls it a "Czech fund", but the
  website gives a US (Georgia) address and partners in Israel and the US.
  Opinion: unsure.

⏺ Agent "Verify tachles" finished · 33s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-13,evidence-verifier,opus,tachles,16745,8,33.1,ok" >>
      data/runs/run_log.csv)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      161  2026-10-13,evidence-verifier,opus,startupyard,17736,10,31.9,ok
      162  2026-10-13,evidence-verifier,opus,startguide-vc,18195,8,32.4,o
           k
      163  2026-10-13,evidence-verifier,opus,stredocesky-inovacni-centrum
           ,16776,8,29.0,ok
      164 +2026-10-13,evidence-verifier,opus,tachles,16745,8,33.1,ok     

⏺ evidence-verifier(Verify tilia-impact-ventures)
  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)

⏺ 65 of 69 records are verified. Four verifiers are running: TCF Capital, Tensor
  Ventures, Thein and Tilia Impact Ventures. United Founders, Y Soft Ventures
  and Zaka VC are still to go; then I'll run R7 (decide).

  The Tachles verifier confirmed the article-date problem I suspected: the cited
  article only recaps 2024 deals, so its date may not be the deal date.

✻ Sautéed for 23s · done 4:14 PM

› Message from evidence-verifier
  tensor-ventures: 6 supported, 2 partially supported; 0 unsupported,
  contradicted or unverifiable. Opinion: yes, an active Czech deeptech VC.
  1. funds[0]: the source supports the EUR 50M target but calls it a
  "Co-investment Fund". The "Fund II" name and the 2024 vintage are not in the
  cited source.
  2. legal_entities[0]: the source confirms the ARES ID and name, but nothing on
  the page states its role as management company.
  Both activity items (Repsense lead, Dec 2025; Edmund participant, Apr 2026)
  are supported and fall within the window.
  File: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/tensor-ventures.json

⏺ Tensor Ventures is verified, and the verifier rates it an active Czech
  deeptech VC. Both of its deals fall inside the window. Two smaller points are
  only partly backed by their sources: the fund's "Fund II" name and 2024
  vintage, and the legal entity's management-company role.

  TCF Capital, Thein and Tilia Impact Ventures are still being verified. United
  Founders, Y Soft Ventures and Zaka VC are next.

✻ Brewed for 2s · done 4:14 PM

⏺ Agent "Verify tensor-ventures" finished · 30s

⏺ Agent "Verify tcf-capital" finished · 32s

› Message from evidence-verifier
  tcf-capital: 5 supported, 0 partially_supported, 0 unsupported, 0
  contradicted, 0 unverifiable. Opinion: no.
  1. Both deals are outside the 24-month window (it starts 2024-10-11):
  Eco-Stations 2024-07-26 and Keboola 2023-12-01. Both are in the dormant range.
  2. The source calls it a later-stage private holding focused on "profitable
  companies at a later stage", not a VC. Its EUR 720M AUM is mostly the Rohlik
  stake.
  3. hq_country is null and no cited page says where the team sits.
  File: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/tcf-capital.json

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && printf '%s\n'
      "2026-10-13,evidence-verifier,opus,tensor-ventures,19013,11,30.1,ok"
      "2026-10-13,evidence-…)
  ⎿  Updated data/runs/run_log.csv (+2 -0)
      162  2026-10-13,evidence-verifier,opus,startguide-vc,18195,8,32.4,o
           k
      163  2026-10-13,evidence-verifier,opus,stredocesky-inovacni-centrum
           ,16776,8,29.0,ok
      164  2026-10-13,evidence-verifier,opus,tachles,16745,8,33.1,ok
      165 +2026-10-13,evidence-verifier,opus,tensor-ventures,19013,11,30.
          +1,ok                                                          
      166 +2026-10-13,evidence-verifier,opus,tcf-capital,17167,8,32.8,ok 

⏺ 2 background agents launched (↓ to manage)
   ├ Verify united-founders
   └ Verify y-soft-ventures

⏺ TCF Capital and Tensor Ventures are verified and logged. TCF won't qualify:
  both its deals fall outside the 24-month window, and it describes itself as a
  later-stage holding, not a VC.

  Four verifiers are running now: Thein, Tilia Impact Ventures, United Founders
  and Y Soft Ventures. Zaka VC is the last one left after that.

✻ Worked for 8s · done 4:14 PM

› Message from evidence-verifier
  tilia-impact-ventures: 5 supported, 1 partially_supported, 0 unsupported,
  contradicted or unverifiable.
  - type is only partially supported: the site never says "venture capital". The
  VC reading rests on "backs founders", equity/convertible tickets and the
  "osoba rizikového kapitálu" legal form.
  - The FaceUp Series A (JIC, 2026-05-19) is inside the window and names Tilia
  as a participating investor.
  - Team location is inferred only from the Prague address; the page doesn't say
  where the team works. Opinion: yes.
  File: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/tilia-impact-ventures.json

⏺ Tilia Impact Ventures is verified and the verifier rates it an active Czech
  VC. Its FaceUp Series A participation (May 2026) is inside the window. The
  "VC" label and the Prague team location are inferred rather than stated
  outright. I'll log it once its usage figures arrive and start Zaka VC, the
  last record.

✻ Cooked for 2s · done 4:14 PM

⏺ Agent "Verify tilia-impact-ventures" finished · 28s

› Message from evidence-verifier
  thein: 7 supported, 1 partially_supported, 1 unsupported. Opinion: no. Written
  to /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/thein.json
  1. The type is PE/holding (LBO, growth capital, majority control), not VC.
  2. The newest deal, Top Alulit on 2024-01-16, is outside the 24-month window
  and inside the dormant band.
  3. evidence_of_activity[1] (2021) is a 100% acquisition and older than 36
  months. The SICAV's LEI has lapsed.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && printf '%s\n'
      "2026-10-13,evidence-verifier,opus,tilia-impact-ventures,16692,8,28.3,ok"
      "2026-10-13,evid…)
  ⎿  Updated data/runs/run_log.csv (+2 -0)
      164  2026-10-13,evidence-verifier,opus,tachles,16745,8,33.1,ok
      165  2026-10-13,evidence-verifier,opus,tensor-ventures,19013,11,30.
           1,ok
      166  2026-10-13,evidence-verifier,opus,tcf-capital,17167,8,32.8,ok
      167 +2026-10-13,evidence-verifier,opus,tilia-impact-ventures,16692,
          +8,28.3,ok                                                     
      168 +2026-10-13,evidence-verifier,opus,thein,,,,ok                 

⏺ evidence-verifier(Verify zaka-vc)
  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)

⏺ Agent "Verify thein" finished · 38s

⏺ While the last 3 verifiers run, I'll check how decide.py treats
  partially_supported before running R7.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && sed -i ''
      's/^2026-10-13,evidence-verifier,opus,thein,,,,ok$/2026-10-13,evidence-ver
      ifier,opus,thein,193…)
  ⎿  class Support:
         """Combines the verifier verdict and the quote-check status for on
     e sourced item."""
     … +139 lines (ctrl+o to expand)
  ⎿  Updated data/runs/run_log.csv (+1 -1)
      165  2026-10-13,evidence-verifier,opus,tensor-ventures,19013,11,30.
           1,ok
      166  2026-10-13,evidence-verifier,opus,tcf-capital,17167,8,32.8,ok
      167  2026-10-13,evidence-verifier,opus,tilia-impact-ventures,16692,
           8,28.3,ok
      168 -2026-10-13,evidence-verifier,opus,thein,,,,ok                 
      168 +2026-10-13,evidence-verifier,opus,thein,19388,9,38.9,ok       

⏺ Here's how decide.py will treat the borderline cases:

  - Partial support: partially_supported items count as supported (flagged, not
    dropped).
  - Missing type or country: a null type or hq_country excludes the record.
  - No legal entity: an active record without a supported legal entity is
    excluded under K1 as not_found_or_defunct.

  That last rule could exclude clearly active funds such as KAYA, N1 and Zaka,
  whose extractors found no confirmed entity. I'll check the outcome once the
  last three verifiers finish.

✻ Sautéed for 13s · done 4:14 PM

› Message from evidence-verifier
  united-founders: 9 supported, 1 partially_supported, 0 unsupported, 0
  contradicted, 0 unverifiable.
  - funds[0] is only partly supported. The Lupa article gives EUR 80M (about CZK
  2bn) as planned investment volume. The page does not state the fund name
  "United Founders SCSp" or the 2025 vintage.
  - hq_country=CZ is supported, but the team is pan-European, so the country
  call is borderline. The fund was founded in Prague, and the GP/co-founder and
  the advisor s.r.o. are in Prague. Other partners sit in Paris, Berlin, Munich,
  Vienna and Bratislava.
  Opinion: yes, active Czech-based VC (2 deals in window). Written to
  /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/united-founders.json

⏺ United Founders is verified, and the verifier rates it an active Czech-based
  VC with 2 deals in the window. The country call is borderline, though: it was
  founded in Prague, but its partners are spread across Europe. Y Soft Ventures
  and Zaka VC are still being verified.

✻ Crunched for 2s · done 4:15 PM

⏺ Agent "Verify united-founders" finished · 36s

⏺ Agent "Verify y-soft-ventures" finished · 37s

› Message from evidence-verifier
  y-soft-ventures: 5 supported, 2 partially_supported, 0
  unsupported/contradicted/unverifiable. Record opinion: yes, an active CZ CVC.
  1. legal_entities[1]: nothing on the cited page shows Y Soft Ventures II, a.s.
  is a fund vehicle. Its NACE is real-estate rental only.
  2. stages: the page says only "early-stage", so pre_seed/seed is the
  extractor's own mapping.
  3. The only activity item (RoboTwin, July 2, 2025, within the window) is
  supported, but its date is the publication date. The round is EUR 1.25m
  pre-seed. The team being in CZ is inferred from the Brno registered seat.
  File: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/y-soft-ventures.json
⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && printf '%s\n'
      "2026-10-13,evidence-verifier,opus,united-founders,20379,9,36.3,ok"
      "2026-10-13,evidence-v…)
  ⎿  Updated data/runs/run_log.csv (+2 -0)
      166  2026-10-13,evidence-verifier,opus,tcf-capital,17167,8,32.8,ok
      167  2026-10-13,evidence-verifier,opus,tilia-impact-ventures,16692,
           8,28.3,ok
      168  2026-10-13,evidence-verifier,opus,thein,19388,9,38.9,ok
      169 +2026-10-13,evidence-verifier,opus,united-founders,20379,9,36.3
          +,ok                                                           
      170 +2026-10-13,evidence-verifier,opus,y-soft-ventures,18965,10,37.
          +7,ok                                                          

⏺ United Founders and Y Soft Ventures are verified and logged; 68 of 69 records
  are done and committed. Y Soft Ventures came out as an active Czech corporate
  VC with one deal in the window. Zaka VC is the last verifier still running; R7
  (decide) starts when it finishes.

✻ Sautéed for 8s · done 4:15 PM

› Message from evidence-verifier
  zaka-vc: 8 supported, 0 partially_supported, 0 unsupported, 0 contradicted, 0
  unverifiable.
  - funds[0]: the our-story page says EUR 15M, but the homepage table shows Fund
  1 as "17M" with no currency, so the fund size or close status is unclear.
  - evidence_of_activity[0] (DeepSeq.AI): the page names ZAKA as lead (the
  record says role unknown), and the deal was first announced in Jan 2026, not
  2026-02-16. Both dates are inside the window.
  - hq_country: the only source is a media label ("České fondy"). The team spans
  Prague, Bratislava, London and SF. Opinion: yes.
  File: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/zaka-vc.json

⏺ R6 is complete: all 69 records are verified. Running R7 (decide) now.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-13,evidence-verifier,opus,zaka-vc,,,,ok" >>
      data/runs/run_log.csv; ls data/verification |…)
  ⎿  69
       89  none      pending
       27  pipeline  active
     … +14 lines (ctrl+o to expand)
  ⎿  Created data/candidates/cz_vc_decisions.csv (+226 -0)
        1 +candidate_id,name,decided_by,status,exclusion_reason,type,hq_c
          +ountry,latest_investment,latest_investment_date,flags,changes 
        2 +3ts-capital-partners,3TS Capital Partners,pipeline,excluded,ou
          +t_of_scope_geography,vc,FI,Patronus (RR Technologies GmbH),202
          +6-04-05,hq_country: verifier=partially_supported | sectors: ve
          +rifier=partially_supported | funds[0]: verifier=partially_supp
          +orted,capital: computed (latest_fund_size)                    
        3 +500-emerging-europe,500 Emerging Europe,pipeline,excluded,out_
          +of_scope_geography,vc,TR,Mission Control Games,2026-04-15,,cap
          +ital: computed (latest_fund_size)                             
        4 +abris-capital,Abris Capital,none,pending,,,,,,"queued, not ext
          +racted",                                                      
        5 +accel,Accel,none,pending,,,,,,"queued, not extracted",        
        6 +accolade,Accolade,none,pending,,,,,,"queued, not extracted",  
        7 +across-private-investments,Across Private Investments,triage,e
          +xcluded,out_of_scope_geography,unknown,SK,,,"triage evidence: 
          +page, confidence low",                                        
        8 +ai-startup-incubator,AI Startup Incubator,none,pending,,,,,,"q
          +ueued, not extracted",                                        
        9 +air-ventures,Air Ventures,none,pending,,,,,,"queued, not extra
          +cted",                                                        
       10 +airbridge,Airbridge,none,pending,,,,,,"queued, not extracted",
       11 +akcelerator-vsem,Akcelerátor VŠEM,none,pending,,,,,,"queued, n
          +ot extracted",                                                
       12 +alea-capital,Alea Capital Partners,triage,excluded,out_of_scop
          +e_geography,pe,PT,,,"triage evidence: page, confidence medium"
          +,                                                             
       13 +alfa8,alfa8,none,pending,,,,,,"queued, not extracted",        
       14 +alpha-intelligence-capital,Alpha Intelligence Capital,pipeline
          +,excluded,out_of_scope_geography,vc,,Waiv,2026-03-19,hq_countr
          +y unknown,capital: computed (latest_fund_size)                
       15 +angelinvest,Angelinvest,none,pending,,,,,,"queued, not extract
          +ed",                                                          
       16 +arctern-ventures,ArcTern Ventures,none,pending,,,,,,"queued, n
          +ot extracted",                                                
       17 +arieli-capital,Arieli Capital,none,pending,,,,,,"queued, not e
          +xtracted",                                                    
       18 +arx-equity-partners,ARX Equity Partners,none,pending,,,,,,"que
          +ued, not extracted",                                          
       19 +aspire11,Aspire11,pipeline,active,,vc,CZ,Vinted,2026-06-23,hq_
          +country: verifier=partially_supported | type: verifier=partial
          +ly_supported | sectors: verifier=partially_supported | legal_e
          +ntities[1]: verifier=partially_supported | verifier opinion: u
          +nsure,                                                        
       20 +aternus-family-office,Aternus Family Office,pipeline,excluded,
          +out_of_scope_type,family_office,CZ,Jutro Medical,2025-12-16,se
          +ctors: verifier=partially_supported | legal_entities[0]: verif
          +ier=partially_supported | evidence_of_activity[0]: verifier=pa
          +rtially_supported,                                            
       21 +atomico,Atomico,triage,excluded,out_of_scope_geography,vc,GB,,
          +,"triage evidence: snippet, confidence low",                  
       22 +austrian-growth-capital-fund,Austrian Growth Capital Fund,tria
          +ge,excluded,out_of_scope_geography,pe,AT,,,"triage evidence: s
          +nippet, confidence low",                                      
       23 +badideas-fund,BADideas.fund,pipeline,excluded,out_of_scope_typ
          +e,,LV,,,hq_country: verifier=partially_supported | type unknow
          +n,type: nulled (quote not found on page) | stages: nulled (quo
          +te not found on page) | evidence_of_activity[0]: dropped (quot
          +e not found on page) | capital: computed (latest_fund_size)   
       24 +bakala-capital,Bakala Capital,none,pending,,,,,,"queued, not e
          +xtracted",                                                    
       25 +battery-ventures,Battery Ventures,none,pending,,,,,,"queued, n
          +ot extracted",                                                
       26 +bd-partners,BD Partners,pipeline,excluded,out_of_scope_type,fa
          +mily_office,CZ,Myriad AI,2025-09-16,"type: verifier=partially_
          +supported | sectors: verifier=partially_supported | evidence_o
          +f_activity[1]: verifier=partially_supported | verifier opinion
          +: yes, but excluded by rules",                                
       27 +bohemia-venture-capital,Bohemia Venture Capital,none,pending,,
          +,,,,"queued, not extracted",                                  
       28 +bolt-accelerator,BOLT,none,pending,,,,,,"queued, not extracted
          +",                                                            
       29 +bond-ventures,Bond Ventures,none,pending,,,,,,"queued, not ext
          +racted",                                                      
       30 +bonuvis,Bonuvis,triage,excluded,advisor_or_intermediary,adviso
          +r,CZ,,,"triage evidence: page, confidence high",              
       31 +borovicka-capital,Borovicka Capital,pipeline,excluded,out_of_s
          +cope_geography,vc,,Outfindo,2025-01-20,"type: verifier=partial
          +ly_supported | hq_country unknown | verifier opinion: yes, but
          + excluded by rules",                                          
       32 +bpd-partners,BPD Partners,pipeline,excluded,out_of_scope_type,
          +family_office,CZ,Powerful Medical,2022-09-28,type: verifier=pa
          +rtially_supported | sectors: verifier=partially_supported,    
       33 +braiins,Braiins,pipeline,excluded,out_of_scope_type,,CZ,Firefi
          +sh,2025-04-08,evidence_of_activity[0]: verifier=partially_supp
          +orted | type unknown,                                         
       34 +brightcap-ventures,BrightCap Ventures,none,pending,,,,,,"queue
          +d, not extracted",                                            
       35 +btcz-ventures,BTCZ Ventures,pipeline,excluded,out_of_scope_geo
          +graphy,vc,,Taveren Therapeutics,2025-12-03,type: verifier=part
          +ially_supported | evidence_of_activity[0]: verifier=partially_
          +supported | hq_country unknown,                               
       36 +budeto,Budeto,pipeline,excluded,out_of_scope_type,,,Vetstor,20
          +25-12-09,evidence_of_activity[0]: verifier=partially_supported
          + | type unknown,                                              
       37 +category-ventures,Category Ventures,triage,excluded,out_of_sco
          +pe_geography,vc,US,,,"triage evidence: page, confidence medium
          +",                                                            
       38 +cb-espri,CB Espri,triage,excluded,out_of_scope_geography,unkno
          +wn,SK,,,"triage evidence: snippet, confidence low",           
       39 +chilli-ventures,Chilli Ventures,pipeline,active,,vc,CZ,Decisio
          +nRules,2025-05-06,type: verifier=partially_supported | verifie
          +r opinion: unsure,                                            
       40 +creandum,Creandum,triage,excluded,out_of_scope_geography,vc,SE
          +,,,"triage evidence: snippet, confidence medium",             
     … 186 more lines (ctrl+o to expand)
  ⎿  Created data/records/cz_vc.csv (+28 -0)
       1 +id,name,website,type,hq_country,sectors,stages,ticket_min,ticke
         +t_max,ticket_currency,ticket_min_eur,ticket_max_eur,ticket_sour
         +ce,capital,capital_currency,capital_eur,capital_basis,capital_a
         +s_of,capital_source,latest_investment,latest_investment_date,la
         +test_investment_source,n_investments_in_window,legal_entity    
       2 +aspire11,Aspire11,https://www.aspire11cap.com,vc,CZ,generalist,
         +growth,,,,,,,515000000,EUR,515000000,latest_fund_size,,https://
         +www.aspire11cap.com,Vinted,2026-06-23,https://www.lupa.cz/aktua
         +lity/fond-aspire11-muchy-a-borkovce-poslal-skoro-pul-miliardy-d
         +o-platformy-vinted/,2,"Aspire 11 Capital SICAV, a.s. (CZ-OR 236
         +20030); Partners investiční společnost, a.s. (CZ-OR 24716006)" 
       3 +chilli-ventures,Chilli Ventures,https://www.chilliventures.cz,v
         +c,CZ,,pre_seed;seed,200000,600000,EUR,200000,600000,https://www
         +.chilliventures.cz,,,,,,,DecisionRules,2025-05-06,https://www.d
         +ecisionrules.io/articles/decisionrules-raises-eu1-6m-to-scale-a
         +utomation-globally,1,Chilli Ventures a.s. (CZ-OR 04106059)     
       4 +credo-ventures,Credo Ventures,https://www.credoventures.com,vc,
         +CZ,,pre_seed,1000000,5000000,USD,894374,4471872,https://www.cre
         +doventures.com,,,,,,,Picogrid,2026-05-29,https://buttondown.com
         +/raisetrack/archive/angel-registry-update-may-29-2026/,2,Credo 
         +Ventures a.s. (CZ-OR 28538137)                                 
       5 +fazole-ventures,Fazole Ventures,https://www.fazole.vc,vc,CZ,,se
         +ed,50000,800000,EUR,50000,800000,https://www.fazole.vc/indexEN.
         +html,,,,,,,Everbot,2025-09-16,https://www.lupa.cz/aktuality/sta
         +rtup-z-opavy-slucuje-desitky-ai-typu-gpt-llama-ci-deepseek-do-j
         +ednoho-rozhrani-ziskal-na-to-investici/,1,Fazole Ventures s.r.o
         +. (CZ-OR 07491492)                                             
       6 +gi21-capital,Gi21 Capital,https://www.gi21capital.com,vc,CZ,sof
         +tware_saas;ai_data;deeptech_hardware,,,,,,,,,,,,,,Hermetiq,2026
         +-08-24,https://www.lupa.cz/aktuality/cesky-miliardar-investuje-
         +do-americke-firmy-ktera-pomoci-ai-automatizuje-buildovani-softw
         +aru/,3,Gi21 Capital a.s. (CZ-OR 19584229)                      
       7 +i-and-i-biotech,i&i Biotech Fund (i&i Bio),https://www.inibio.e
         +u,vc,CZ,health_biotech;medtech,,500000,2000000,EUR,500000,20000
         +00,https://www.inibio.eu,47000000,EUR,47000000,latest_fund_size
         +,,https://www.inibio.eu/news,Antiverse,2026-03-03,https://vestb
         +ee.com/insights/articles/antiverse-raises-9-3-m,2,Biotech Inves
         +tments s.r.o. (CZ-OR 10885978)                                 
       8 +inven-capital,Inven Capital,https://www.invencapital.cz,vc,CZ,c
         +limate_energy,,2000000,30000000,EUR,2000000,30000000,https://ww
         +w.invencapital.cz,500000000,EUR,500000000,latest_fund_size,,htt
         +ps://www.invencapital.cz,Wint,2026-09-11,https://www.descubre.v
         +c/noticia/wint-recauda-36m-en-serie-d-con-el-respaldo-del-fondo
         +-latinoamericano-lip-ventures-2026-09-11,2,"Inven Capital, SICA
         +V, a.s. (CZ-OR 02059533)"                                      
       9 +j-t-ventures,J&T Ventures,https://www.jtventures.cz,vc,CZ,gener
         +alist,pre_seed;seed;series_a,300000,3000000,EUR,300000,3000000,
         +https://www.jtventures.cz,,,,,,,Wultra,2026-06-29,https://pulse
         +2.com/wultra-raises-e6-8-million-series-a-to-expand-post-quantu
         +m-digital-identity-solutions/,2,J&T Ventures CG SICAV a.s. (CZ-
         +OR 08220867)                                                   
      10 +jic-ventures,JIC Ventures,https://www.jic.cz/ventures/,vc,CZ,de
         +eptech_hardware;software_saas,pre_seed;seed,,1000000,EUR,,10000
         +00,https://www.jic.cz/ventures/,400000000,CZK,16399492,latest_f
         +und_size,2026-04-07,https://ctp.eu/news/ctp-becomes-largest-inv
         +estor-in-new-e16-million-jic-ventures-start-up-fund/,Elredo,202
         +6-10-01,https://cc.cz/driv-je-v-usa-ignorovali-ted-uz-uzaviraji
         +-obri-kontrakty-a-stehuji-se-tam-navic-ziskali-dalsi-investory/
         +,3,"JIC Ventures 2 a.s., osoba rizikového kapitálu (CZ-OR 24320
         +358)"                                                          
      11 +jsk-investments,JSK Investments,https://www.jskinvestments.cz,v
         +c,CZ,consumer_ecommerce;logistics_supply_chain;industrial_manuf
         +acturing;health_biotech,pre_seed;seed,,,,,,,2000000000,CZK,8199
         +7458,latest_fund_size,2025-10-01,https://www.newstream.cz/money
         +/kijonkova-spousti-vlastni-fond-pro-kvalifikovane-investory,Min
         +tNeuro,2026-10-09,https://www.jskinvestments.cz/cs/media/jsk-in
         +vestments-sicav-a-s-investuje-do-britskeho-vyvojare-cipu-pro-ne
         +urotechnologie-mint-neuro,3,JSK Investments SICAV a.s. (CZ-OR 2
         +3823445)                                                       
      12 +koopeo-ventures,Koopeo Ventures,https://koopeoventures.com,vc,C
         +Z,,,,,,,,,,,,,,,TRIFFT Loyalty,2025-07-17,https://tech.eu/2025/
         +07/17/trifft-loyalty-raises-550k-pre-seed-to-scale-its-ai-drive
         +n-emotional-loyalty-platform/,1,KOOPEO Ventures SE (CZ-OR 05269
         +113)                                                           
      13 +lighthouse-ventures,Lighthouse Ventures,https://lhv.vc,vc,CZ,so
         +ftware_saas;fintech;ai_data,pre_seed;seed,200000,1000000,EUR,20
         +0000,1000000,https://lhv.vc/faq/,,,,,,,Hermetiq,2026-08-31,http
         +s://lhv.vc/news-and-events/,2,Lighthouse Ventures GP s.r.o. (CZ
         +-OR 07500912)                                                  
      14 +look-ai-ventures,Look AI Ventures,https://lookai.vc,vc,CZ,ai_da
         +ta,seed,250000,250000,EUR,250000,250000,https://tech.eu/2023/04
         +/13/czech-republic-has-a-new-investment-fund-for-ai-start-ups,2
         +0000000,EUR,20000000,latest_fund_size,2023-04-13,https://tech.e
         +u/2023/04/13/czech-republic-has-a-new-investment-fund-for-ai-st
         +art-ups,Sodex Innovations,2026-07-13,https://tech.eu/2026/07/13
         +/sodex-innovations-secures-4m-to-bring-real-time-intelligence-t
         +o-construction-sites/,3,"FTP Dimension investiční společnost, a
         +.s. (CZ-OR 29659302)"                                          
      15 +miton,Miton,https://miton.cz,vc,CZ,ai_data;fintech;consumer_eco
         +mmerce;health_biotech,pre_seed;seed;series_a,300000,2000000,EUR
         +,300000,2000000,https://miton.cz/o-nas/,,,,,,,Ace (padel app),2
         +026-10-01,https://cc.cz/prodal-startup-americanum-ted-se-veze-n
         +a-vlne-padelu-pulku-jeho-nove-aplikace-ziskava-za-miliony-miton
         +/,1,"MITON CZ, s.r.o. (CZ-OR 25417967)"                        
      16 +orbit-capital,Orbit Capital,https://orbitcapital.com,vc,CZ,soft
         +ware_saas,growth,,,,,,,107000000,EUR,107000000,latest_fund_size
         +,2026-07-02,https://tech.eu/2026/07/02/orbit-capital-closes-eur
         +107m-venture-debt-fund-for-cee-scaleups/,IAG,2026-06-02,https:/
         +/cc.cz/dalsich-140-milionu-na-rychlejsi-nakup-autodilu-cesi-cht
         +eji-pomoci-mechanikum-a-miri-do-evropy/,1,"Conseq-Orbit SICAV, 
         +a.s. (formerly Orbit Capital SICAV, a.s.) (CZ-OR 08223467)"    
      17 +presto-ventures,Presto Tech Horizons (Tech Horizons),https://pr
         +estoventures.com,vc,CZ,,seed;series_a,500000,5000000,EUR,500000
         +,5000000,https://prestoventures.com,150000000,EUR,150000000,lat
         +est_fund_size,2024-10-25,https://tech.eu/2024/10/25/presto-tech
         +-horizons-fund-announces-investment-in-three-startups/,Occam,20
         +26-02-11,https://cc.cz/investori-v-cele-s-miliardarem-michalem-
         +strnadem-posilaji-desitky-milionu-na-vyvoj-autonomnich-dronu/,3
         +,"Presto Ventures II a.s., osoba rizikového kapitálu (CZ-OR 116
         +78704)"                                                        
      18 +purple-ventures,Purple Ventures,https://www.purple-ventures.com
         +,vc,CZ,,pre_seed;seed,250000,400000,EUR,250000,400000,https://w
         +ww.purple-ventures.com,40000000,EUR,40000000,latest_fund_size,2
         +024-06-27,https://tech.eu/2024/06/27/purple-ventures-launches-e
         +ur40m-fund-for-early-stage-software-startups/,Fether Labs,2026-
         +05-27,https://www.euro.cz/clanky/cesky-fond-purple-ventures-saz
         +i-na-technologii-ovladanou-pohybem-prstu-do-britskeho-startupu-
         +posilaji-11-milionu-korun/,1,Purple Ventures s.r.o. (CZ-OR 0577
         +5574)                                                          
      19 +reflex-capital,Reflex Capital,https://www.reflexcapital.com,vc,
         +CZ,,,,,,,,,,,,,,,Merchantee,2026-06-09,https://raising.fi/news/
         +merchantee-undisclosed-june-2026,2,Reflex Capital SE (CZ-OR 242
         +69158)                                                         
      20 +rockaway-ventures,Rockaway Ventures,https://www.rockawayventure
         +s.com,vc,CZ,consumer_ecommerce;logistics_supply_chain;media_gam
         +ing;cybersecurity_defense;climate_energy,seed;series_a,,,,,,,,,
         +,,,,Vermeer,2025-10-23,https://vestbee.com/insights/articles/ve
         +rmeer-raises-funds,2,Rockaway Ventures a.s. (CZ-OR 06387136)   
      21 +seed-starter,Seed Starter (Ceska sporitelna),https://www.seedst
         +arter.cz,cvc,CZ,fintech,pre_seed;seed,200000,1000000,EUR,200000
         +,1000000,https://www.seedstarter.cz,,,,,,,Definic,2026-06-12,ht
         +tps://cc.cz/nakup-it-sluzeb-v-korporacich-je-casto-nefunkcni-hl
         +asi-do-jejich-reseni-investuje-i-ceska-sporitelna/,3,"ČS Seed S
         +tarter, a.s. (CZ-OR 61058769)"                                 
      22 +soulmates-ventures,Soulmates Ventures,https://www.soulmatesvent
         +ures.com,vc,CZ,climate_energy;health_biotech;agri_food;mobility
         +_transport;edtech,seed,,3000000,EUR,,3000000,https://www.soulma
         +tesventures.com/,50000000,EUR,50000000,latest_fund_size,2025-03
         +-18,https://vestbee.com/insights/articles/soulmates-ventures-ra
         +ises-50-m-fund,Rightcharge,2026-09-03,https://vestbee.com/insig
         +hts/articles/rightcharge-raises-500-k,3,"Soulmates Ventures, os
         +oba rizikového kapitálu, s.r.o. (CZ-OR 09789561)"              
      23 +springtide-ventures,Springtide Ventures,https://www.springtide.
         +cz,cvc,CZ,software_saas;cybersecurity_defense;ai_data,seed;seri
         +es_a;series_b_plus,1000000,10000000,USD,894374,8943744,https://
         +www.springtide.cz/about/,,,,,,,ThreatMark,2025-01-07,https://th
         +reatmark.com/threatmark-to-advance-the-fight-against-online-fra
         +ud,1,Springtide Ventures s.r.o. (CZ-OR 01726587)               
      24 +startupyard,StartupYard,https://startupyard.com,vc,CZ,ai_data;d
         +eeptech_hardware,pre_seed;seed,25000,25000,EUR,25000,25000,http
         +s://startupyard.com/frequently-asked-questions-about-startupyar
         +d/,,,,,,,Ydoca,2025-02-14,https://cc.cz/live/petkrat-rychlejsi-
         +vyberova-rizeni-do-cesko-slovenske-ai-platformy-ydoca-investova
         +li-depo-ventures-a-startupyard/,1,StartupYard Batch 15 s.r.o. (
         +CZ-OR 22266852)                                                
      25 +tensor-ventures,Tensor Ventures,https://tensor.ventures,vc,CZ,a
         +i_data;deeptech_hardware;health_biotech;climate_energy,seed;ser
         +ies_a,,,,,,,50000000,EUR,50000000,latest_fund_size,2024-05-15,h
         +ttps://cc.cz/evropsky-investicni-fond-uz-vlozil-penize-do-17-ce
         +skych-fondu-miliardovy-ted-otevira-s-tensor-ventures/,Edmund,20
         +26-04-09,https://www.lupa.cz/aktuality/ostravsky-startup-veri-v
         +-ai-misto-zkuseneho-technika-s-investici-se-ma-rozsirit-po-evro
         +pe-i-americe/,2,Tensor Ventures a.s. (CZ-OR 06257241)          
      26 +tilia-impact-ventures,Tilia Impact Ventures,https://tilia.vc,vc
         +,CZ,generalist,,300000,1200000,EUR,300000,1200000,https://tilia
         +.vc,,,,,,,FaceUp,2026-05-19,https://www.jic.cz/en/about-us/pro-
         +media/prvni-investice-noveho-fondu-jic-ventures-miri-do,1,"Tili
         +a Impact Ventures, osoba rizikového kapitálu, s.r.o. (CZ-OR 178
         +48911)"                                                        
      27 +united-founders,United Founders,https://www.unitedfounders.vc/,
         +vc,CZ,deeptech_hardware;ai_data;cybersecurity_defense;medtech;i
         +ndustrial_manufacturing;climate_energy,pre_seed;seed,100000,100
         +0000,EUR,100000,1000000,https://www.unitedfounders.vc/,80000000
         +,EUR,80000000,latest_fund_size,2025-11-05,https://www.lupa.cz/a
         +ktuality/havrlant-spoluzaklada-united-founders-novy-fond-chce-d
         +o-evropskych-technologii-investovat-2-miliardy/,Peak Quantum,20
         +26-04-14,https://www.munich-quantum-valley.de/news-events/detai
         +l/peakquantum-secures-five-million-in-total-funding,2,United Fo
         +unders Advisors s.r.o. (CZ-OR 21594813); United Founders SCSp (
         +LU-RCS B300691)                                                
      28 +y-soft-ventures,Y Soft Ventures,https://www.ysoft.com/ventures,
         +cvc,CZ,deeptech_hardware;software_saas;cybersecurity_defense;ai
         +_data,pre_seed;seed,,,,,,,,,,,,,RoboTwin,2025-07-02,https://eit
         +jumpstarter.eu/robotwin-secures-1-million-eur/,1,"Y Soft Ventur
         +es, a.s. (CZ-OR 29314445); Y Soft Ventures II, a.s. (CZ-OR 0789
         +0150)"                                                         
  ⎿  Created data/records/decided/3ts-capital-partners.json (+168 -0)
        1 +{                                                             
        2 +  "schema_version": "1.0",                                    
        3 +  "id": "3ts-capital-partners",                               
        4 +  "name": "3TS Capital Partners",                             
        5 +  "website": "https://3tscapital.com",                        
        6 +  "hq_country": {                                             
        7 +    "value": "FI",                                            
        8 +    "source": {                                               
        9 +      "url": "https://en.ain.ua/2024/02/05/3ts-capital-partner
          +-closes-fund-iv-111m",                                        
       10 +      "tier": 3,                                              
       11 +      "publisher": "AIN.UA",                                  
       12 +      "published_date": "2024-02-05",                         
       13 +      "accessed_date": "2026-10-13",                          
       14 +      "quote": "based in Helsinki and Vienna",                
       15 +      "self_reported": false                                  
       16 +    },                                                        
       17 +    "note": "Offices Helsinki and Vienna per 2024 article; tea
          +m also in other countries incl. Czechia (per search summary, u
          +nverified). Not a Czech-based team."                          
       18 +  },                                                          
       19 +  "legal_entities": [                                         
       20 +    {                                                         
       21 +      "name": "3TS Capital Partners Oy",                      
       22 +      "registry": "FI-PRH",                                   
       23 +      "registry_id": "1505569-6",                             
       24 +      "role": "management_company",                           
       25 +      "source": {                                             
       26 +        "url": "https://fonecta.fi/profiili/3ts-capital-partne
          +rs-oy/545161",                                                
       27 +        "tier": 3,                                            
       28 +        "publisher": "Fonecta",                               
       29 +        "published_date": null,                               
       30 +        "accessed_date": "2026-10-13",                        
       31 +        "quote": "3TS Capital Partners Oy",                   
       32 +        "self_reported": false                                
       33 +      }                                                       
       34 +    }                                                         
       35 +  ],                                                          
       36 +  "type": {                                                   
       37 +    "value": "vc",                                            
       38 +    "subtype": "growth equity",                               
       39 +    "source": {                                               
       40 +      "url": "https://3tscapital.com/",                       
     … 128 more lines (ctrl+o to expand)
  ⎿  Created data/records/decided/500-emerging-europe.json (+148 -0)
        1 +{                                                             
        2 +  "schema_version": "1.0",                                    
        3 +  "id": "500-emerging-europe",                                
        4 +  "name": "e2vc (formerly 500 Emerging Europe)",              
        5 +  "website": "https://e2.vc",                                 
        6 +  "hq_country": {                                             
        7 +    "value": "TR",                                            
        8 +    "source": {                                               
        9 +      "url": "https://www.vestbee.com/insights/articles/e2vc-s
          +ecures-first-close-of-100-m-fund",                            
       10 +      "tier": 3,                                              
       11 +      "publisher": "Vestbee",                                 
       12 +      "published_date": "2026-01-14",                         
       13 +      "accessed_date": "2026-10-13",                          
       14 +      "quote": "Turkey-based venture capital firm e2vc has ann
          +ounced the close of its €100 million Fund III",               
       15 +      "self_reported": false                                  
       16 +    },                                                        
       17 +    "note": "Same article says the team has offices in San Fra
          +ncisco, New York and London; e2.vc shows clocks for San Franci
          +sco, London, Istanbul. Country of the investment team is not f
          +irmly established."                                           
       18 +  },                                                          
       19 +  "legal_entities": [],                                       
       20 +  "type": {                                                   
       21 +    "value": "vc",                                            
       22 +    "subtype": null,                                          
       23 +    "source": {                                               
       24 +      "url": "https://www.vestbee.com/insights/articles/e2vc-s
          +ecures-first-close-of-100-m-fund",                            
       25 +      "tier": 3,                                              
       26 +      "publisher": "Vestbee",                                 
       27 +      "published_date": "2026-01-14",                         
       28 +      "accessed_date": "2026-10-13",                          
       29 +      "quote": "e2vc primarily invests in pre-seed and idea-st
          +age startups",                                                
       30 +      "self_reported": false                                  
       31 +    }                                                         
       32 +  },                                                          
       33 +  "sectors": {                                                
       34 +    "value": [                                                
       35 +      "software_saas",                                        
       36 +      "ai_data",                                              
       37 +      "fintech",                                              
       38 +      "media_gaming"                                          
       39 +    ],                                                        
       40 +    "raw": "enterprise software, AI, fintech, and gaming",    
     … 108 more lines (ctrl+o to expand)
  ⎿  Created data/records/decided/alpha-intelligence-capital.json (+129 -0)
        1 +{                                                             
        2 +  "schema_version": "1.0",                                    
        3 +  "id": "alpha-intelligence-capital",                         
        4 +  "name": "Alpha Intelligence Capital",                       
        5 +  "website": null,                                            
        6 +  "hq_country": {                                             
        7 +    "value": null,                                            
        8 +    "null_reason": "conflicting_sources",                     
        9 +    "note": "Maddyness lists offices in US, France, UAE, Singa
          +pore with one partner each; other directories say San Francisc
          +o/Paris/Singapore or Luxembourg. No single team country establ
          +ished."                                                       
       10 +  },                                                          
       11 +  "legal_entities": [],                                       
       12 +  "type": {                                                   
       13 +    "value": "vc",                                            
       14 +    "subtype": "AI-focused",                                  
       15 +    "source": {                                               
       16 +      "url": "https://www.maddyness.com/uk/2023/01/16/an-ai-fo
          +cused-fund-with-a-tech-first-approach-a-profile-of-alpha-intel
          +ligence-capital/",                                            
       17 +      "tier": 3,                                              
       18 +      "publisher": "Maddyness",                               
       19 +      "published_date": "2023-01-16",                         
       20 +      "accessed_date": "2026-10-13",                          
       21 +      "quote": "as a preeminent artificial intelligence focuse
          +d venture capital firm",                                      
       22 +      "self_reported": false                                  
       23 +    }                                                         
       24 +  },                                                          
       25 +  "sectors": {                                                
       26 +    "value": [                                                
       27 +      "ai_data",                                              
       28 +      "health_biotech",                                       
       29 +      "industrial_manufacturing",                             
       30 +      "cybersecurity_defense"                                 
       31 +    ],                                                        
       32 +    "raw": "AI companies; healthcare, manufacturing, cybersecu
          +rity, etc.",                                                  
       33 +    "source": {                                               
       34 +      "url": "https://www.maddyness.com/uk/2023/01/16/an-ai-fo
          +cused-fund-with-a-tech-first-approach-a-profile-of-alpha-intel
          +ligence-capital/",                                            
       35 +      "tier": 3,                                              
       36 +      "publisher": "Maddyness",                               
       37 +      "published_date": "2023-01-16",                         
       38 +      "accessed_date": "2026-10-13",                          
       39 +      "quote": "We invest across a wide swath of industries, i
          +ncluding, but not limited to, healthcare, manufacturing, cyber
          +security, etc.",                                              
       40 +      "self_reported": false                                  
     … 89 more lines (ctrl+o to expand)
  ⎿  … 68 more files changed

⏺ Agent "Verify zaka-vc" finished · 36s

⏺ Results so far: 27 active, 2 dormant, 41 pipeline-excluded, 67
  triage-excluded, and 89 pending (88 unprocessed queue rows plus one
  duplicate). Now I'll check the per-candidate flags for agent errors.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && sed -i ''
      's/^2026-10-13,evidence-verifier,opus,zaka-vc,,,,ok$/2026-10-13,evidence-v
      erifier,opus,zaka-vc…)
  ⎿  candidate_id,name,decided_by,status,exclusion_reason,type,hq_country,l
     atest_investment,latest_investment_date,flags,changes
     3ts-capital-partners        excluded out_of_scope_geography  | hq_coun
     … +135 lines (ctrl+o to expand)
  ⎿  Updated data/runs/run_log.csv (+1 -1)
      168  2026-10-13,evidence-verifier,opus,thein,19388,9,38.9,ok
      169  2026-10-13,evidence-verifier,opus,united-founders,20379,9,36.3
           ,ok
      170  2026-10-13,evidence-verifier,opus,y-soft-ventures,18965,10,37.
           7,ok
      171 -2026-10-13,evidence-verifier,opus,zaka-vc,,,,ok               
      171 +2026-10-13,evidence-verifier,opus,zaka-vc,19353,10,36.6,ok    

⏺ R7 flags split into three buckets: six active Czech VCs wrongly excluded from
  K1 due to missing registry entities (an extraction miss, flagged for your
  decision rather than a rule change), date/attribution errors in Braiins,
  Tachles, Novira and BTCZ, and seven "unsure" type judgment calls (Aspire11,
  Chilli Ventures, Gi21, Koopeo, Miton, Orbit Capital, Springtide). I'm logging
  the first two buckets as AI errors.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && cat >>
      docs/ai-errors.md <<'EOF'
      | E-19 | 2026-10-13 | investor-extractor | czech-founders-vc, depo-vent…)
  ⎿  Updated docs/ai-errors.md (+3 -0)
      22  | E-16 | 2026-10-13 | investor-extractor | y-soft-ventures | — 
          | Agent mimo svou roli spustil `src.check_quotes` nad všemi záz
          namy (krok R5 orchestrátoru), zatímco jiní extraktoři ještě zap
          isovali. | Závěrečná zpráva agenta; nečekaná složka `data/quote
          _checks/`. | Výstup smazán, R5 poběží jednou po dokončení extra
          kce. Prompt extraktoru zatím neměním (jednorázové); oprávnění p
          rojektu příkaz povolují všem agentům. |
      23  | E-17 | 2026-10-13 | evidence-verifier / investor-extractor | 
          depo-ventures | — | Domovská stránka depoventures.com obsahuje 
          skryté pokyny pro AI čtenáře (třetí případ prompt injection po 
          E-04 a E-07). Ověřovatel je rozpoznal a ignoroval; oba běhy ext
          raktoru stránku četly, ale ve zprávě to neuvedly. Hodnoty v záz
          namu ověřovatel potvrdil (7/7 podloženo), takže vliv na data ne
          vidím. | Zpráva ověřovatele (R6). | Nic; doporučení pro README:
           obsah stránek je nedůvěryhodný vstup a nezávislé ověření je pr
          oti tomu ochrana. Ruční kontrola by měla záznam DEPO projít se 
          zvýšenou pozorností. |
      24  | E-18 | 2026-10-13 | investor-extractor (prompt) | i-and-i-pra
          gue (a další záznamy s kurzy.cz) | `hq_country`, `legal_entitie
          s` | Prompt extraktoru doporučuje `rejstrik-firem.kurzy.cz` jak
          o zrcadlo rejstříku, ale vyhledávací stránky kurzy.cz zakazuje 
          robots.txt. Ověřovatel je proto nemohl otevřít (`unverifiable`)
          , `check_quotes.py` je hlásí jako nedostupné. Chyba je v mém za
          dání, ne v modelu. | Ověřovatel (R6). | Zatím nic, aby šlo měři
          t pilot beze změny. Pro další běh: v promptu nahradit kurzy.cz 
          za ARES API / or.justice.cz (úroveň 1) a robots.txt zmínit výsl
          ovně. |
      25 +| E-19 | 2026-10-13 | investor-extractor | czech-founders-vc, d
         +epo-ventures, kaya-vc, nation1, purposetech, zaka-vc | `legal_e
         +ntities` | U šesti aktivních VC (ověřovatel u většiny „yes“) ex
         +traktor nenašel nebo nezapsal právnickou osobu, takže `decide.p
         +y` je podle K1 vyřadil s kódem `not_found_or_defunct`. U Czech 
         +Founders VC první (zkušební) běh IČO z or.justice.cz našel, dru
         +hý ne: výsledek extrakce je nestabilní. Kód `not_found_or_defun
         +ct` je navíc pro aktivní fond zavádějící. | `decide.py`, přízna
         +k „verifier opinion: yes, but excluded by rules“ + „K1: no supp
         +orted legal entity“. | Zatím nic (pravidlo K1 je v PLAN). Návrh
         + pro Davida: buď dohledat IČO ručně při kontrole, nebo extrakto
         +ru přikázat ARES API (viz E-18) a znovu spustit jen tyto záznam
         +y; zvážit samostatný kód vyřazení „identity_unconfirmed“. |    
      26 +| E-20 | 2026-10-13 | investor-extractor | braiins, tachles, no
         +vira-capital | `evidence_of_activity[].announced_date` | Datum 
         +článku použito jako datum investice: Braiins (podíl ve Firefish
         + 09/2024, blog 04/2025), Tachles (rekapitulace investic za 2024
         + v článku 02/2025), Novira (investice 2020, článek o exitu 2023
         +). Přesně chyba „datum článku ≠ datum investice“ z PLAN §5.3. |
         + Ověřovatel (R6). | Nic; ověřovatel ji zachytil, záznamy jsou s
         +tejně vyřazené z jiných důvodů. Pro další běh: v promptu výslov
         +ně „rekapitulace není oznámení“. |                             
      27 +| E-21 | 2026-10-13 | evidence-verifier | inven-capital, btcz-v
         +entures | `evidence_of_activity[0]` | Ověřovatel nezachytil rol
         +i `co_lead` u Inven/Wint převzatou ze snippetu (E-13) a u BTCZ/
         +Taveren dal jen `partially_supported`, ačkoli zdroj investici B
         +TCZ v okně nedokládá (E-14). `decide.py` počítá `partially_supp
         +orted` jako podložené, takže položky zůstaly. | Orchestrátor po
         +rovnáním se zprávami extraktoru. | Zatím nic; vstup pro metriku
         + shody ověřovatele s ruční kontrolou. BTCZ je stejně vyřazen (n
         +eznámé sídlo). |                                               

⏺ R7 is committed. Now R8, the review sheet.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && .venv/bin/python
      -m src.review_sheet 2>&1 | tail -10; ls -la data/manual_review/; wc -l
      data/manual_revi…)
  ⎿  292 review rows -> /Users/davidkoktavy/Desktop/Investor DB Starter/dat
     a/manual_review/cz_vc_todo.csv and /Users/davidkoktavy/Desktop/Investo
     r DB Starter/data/manual_review/review.html
     … +6 lines (ctrl+o to expand)
  ⎿  2 files changed (binary, mode only or too large to show)

⏺ The sheet has 292 rows. Before committing, I'll confirm it's blind, i.e.
  contains no verifier verdicts or quote-check results.

  Ran 1 shell command (ctrl+o to expand)

⏺ The sheet is blind: no verifier or quote-check terms appear, and the verdict
  column is the empty one for your own ratings. Committing R8.

  Ran 1 shell command (ctrl+o to expand)

⏺ I've run the pilot through R8 and stopped there, as the runbook says; the
  manual review is yours. Everything is committed and pushed.

  Result:
  - Database: 27 active records in data/records/cz_vc.jsonl and 2 dormant ones.
  - Excluded: 41 by the pipeline and 67 by triage.
  - Pending (89): the 88 candidates beyond the 70 extracted, plus one duplicate
    (seed-starter-ceske-sporitelny, D-018). Every candidate has a row in
    cz_vc_decisions.csv.
  - Checks: all 69 extracted records pass schema validation. The quote check
    found 409 of 419 quotes on their pages, with 3 missing and 7 pages
    unreachable. The Opus verifier checked every record.

  Changes I made beyond the runbook, each written up in docs/decisions.md:
  - D-014: triage re-runs were triggered when more than a third of a batch had
    no known HQ country.
  - D-015: decide.py now excludes a candidate on type alone only when the
    evidence is a fetched page with high confidence. Before this, Springtide
    Ventures and JSK Investments would have been dropped without extraction.
  - D-016: a new script, src/select_queue.py, picks the 70 candidates to extract
    out of the 158 queued.
  - D-017: extraction was paced because Claude Code allows 200 web searches per
    session, shared by all agents.
  - The extractor prompt changed once, after the 4-record trial, in its own
    agents: commit.

  Points you should look at first:
  - Six active-looking Czech VCs are excluded under K1 (Czech Founders VC, DEPO,
    KAYA, N1, PurposeTech, Zaka) only because the extractor didn't record a
    legal entity. For Czech Founders, the first run found its IČO and the second
    didn't. The exclusion code not_found_or_defunct is also misleading for
    funds that are clearly active (E-19). It's your call whether to look up the
    IČOs during review or re-run just these records.
  - The extractor prompt points to kurzy.cz, which blocks fetching in its 
    robots.txt. or.justice.cz does too. The verifier couldn't check those
    sources, and this conflicts with our respect-robots.txt rule (E-18). I left
    the prompt unchanged so the whole pilot runs on one prompt.
  - Seven active records are type judgment calls where the verifier was unsure:
    Aspire11, Chilli, Gi21, Koopeo, Miton, Orbit and Springtide. Orbit is mainly
    a debt investor.
  - Three sites carried hidden instructions aimed at AI agents: DEPO, gi21 and a
    Dealroom result. The agents ignored them, and the DEPO data was confirmed 7
    of 7 (E-04, E-07, E-17).
  - The verifier missed two flawed items: the Inven Capital role and the BTCZ
    deal (E-21). This will show up in the verifier-vs-human comparison.

  AI errors E-06 to E-21 are in docs/ai-errors.md. Token use across all agent
  runs is about 2.5M for extraction, 1.2M for verification and 2.1M for triage,
  including the failed first attempt. Six run-log rows from the trial and the
  stopped runs have no token figures.

  For R9, open data/manual_review/review.html (292 rows). Then save
  data/manual_review/cz_vc.csv and time_minutes.txt, and run .venv/bin/python -m
  src.metrics. The session export is also yours, since I can't run slash
  commands: type /export and save it as ai-log/01-pilot-r0-r8.md.

✻ Brewed for 27m 29s · done 4:16 PM

❯ continue                                                                      
  ⎿  You've hit your session limit · resets 8:40pm (Europe/Prague)
     /upgrade or /usage-credits to finish what you’re working on.

⏺ Usage limit reached · continuing automatically at 8:40pm · esc to 
  cancel

✻ Churned for 1s · done 8:34 PM

⏺ Usage limit reset · continuing automatically

  Ran 1 shell command (ctrl+o to expand)

⏺ Nothing is left for me to do. Steps R0–R8 finished before the limit reset, and
  the repo is clean and in sync with GitHub, with nothing uncommitted.

  The rest needs you, in this order:
  1. Manual review (R8): open data/manual_review/review.html, mark the 292 rows,
     then save data/manual_review/cz_vc.csv and the minutes you spent in
     data/manual_review/time_minutes.txt.
  2. Decisions while reviewing:
     - The six active-looking Czech VCs excluded only because no legal entity
       (IČO) was recorded, E-19: look up their IČOs or have me re-extract them.
     - Whether to add the alias seed-starter-ceske-sporitelny → seed-starter to
       aliases.csv (D-018).
  3. Session log: run /export and save it as ai-log/01-pilot-r0-r8.md.
  4. Metrics (R9): after your review, run .venv/bin/python -m src.metrics, or
     tell me to run it.

✻ Sautéed for 11s · done 8:41 PM

※ recap: We're building a public-source database of Czech VC investors, and the pilot run (R0–R8) is done: 27 active records, ready for your blind review. Next, open data/manual_review/review.html, rate the 292 rows, and save cz_vc.csv. (disable recaps in /config)

❯ caffeinate -i claude                                                          

⏺ I won't run that one from here. caffeinate -i claude starts a new interactive
  Claude Code session inside this one, which needs its own terminal and would
  hang in this tool.

  To keep the Mac awake while you work, run it in a separate Terminal window.
  Or, from this session, run ! caffeinate -i -w <PID> in the prompt, where <PID>
  is this Claude process (you can find it with pgrep -n claude). That keeps the
  machine awake for as long as this session runs.

  Nothing is running in the background right now, though. The pipeline stopped
  after R8, so there's nothing that needs the Mac awake until you finish the
  manual review and want R9 run.

✻ Cooked for 4s · done 8:54 PM

❯ epair pass before the manual review; log it as D-019 in docs/decisions.md.    
                                                                                
  In .claude/agents/investor-extractor.md, replace the kurzy.cz/firmy.cz tip    
  with: or.justice.cz or the ARES register (tier 1), and the IČO from the       
  website imprint; respect robots.txt (E-18). Commit it alone as agents: ….     
  Add the alias seed-starter-ceske-sporitelny → seed-starter to                 
  data/candidates/aliases.csv (D-018, approved by David).                       
  For the pipeline-excluded candidates flagged “K1: no supported legal entity”  
  or “hq_country unknown”, move the old staging record to                       
  data/records/repair_01/ and re-run investor-extractor, focusing on the legal  
  entity (IČO) and where the investment team sits.                              
  Re-run R4–R8 for those records: validate, check_quotes, verifier, decide,     
  review_sheet.                                                                 
  Add the before/after decision for each record to E-19 in docs/ai-errors.md.   
  Commit and push after each step. Stop after R8.                               

⏺ I'll treat the pasted text as your instructions; its first line is cut off
  ("epair pass…") but the steps are complete. These are the 12 records to
  repair:
  - No supported legal entity (6): Czech Founders VC, DEPO, KAYA, N1,
    PurposeTech, Zaka VC.
  - HQ country unknown (6): Alpha Intelligence Capital, Borovička, BTCZ, IP Lab
    Ventures, RockawayX, Tachles VC.

  I'm starting with D-019 and the prompt fix.

  Ran 1 shell command (ctrl+o to expand)

⏺ Update(.claude/agents/investor-extractor.md)  ⎿  Added 1 line, removed 1 line
      14  
      15  ## Steps
      16  
      17 -1. **Identity.** Open the website (about, team, contact, imprin
         -t/legal notice, "Kontakt", "O nás"). Find the legal entity and 
         -its registration number. For Czech companies the website imprin
         -t usually names the company and its IČO; confirm it in a regist
         -ry if you can (search `"<company name>" IČO` or `site:or.justic
         -e.cz <name>`; `rejstrik-firem.kurzy.cz` and `firmy.cz` pages ar
         -e acceptable tier-3 mirrors of the register). Regulated manager
         -s are in the ČNB JERRS register. Record where the investment te
         -am sits (`hq_country`).                                        
      17 +1. **Identity.** Open the website (about, team, contact, imprin
         +t/legal notice, "Kontakt", "O nás"). Find the legal entity and 
         +its registration number. For Czech companies the website imprin
         +t (footer, "Kontakt", legal notice) usually names the company a
         +nd its IČO: record it from there. Confirm it in a tier-1 regist
         +er: the ARES API (`https://ares.gov.cz/ekonomicke-subjekty-v-be
         +/rest/ekonomicke-subjekty/<IČO>`, returns name and seat) or or.
         +justice.cz. Respect robots.txt: do not cite pages a site disall
         +ows for crawlers (kurzy.cz and firmy.cz search pages are disall
         +owed; or.justice.cz may be too, so prefer ARES). Regulated mana
         +gers are in the ČNB JERRS register. Record where the investment
         + team sits (`hq_country`).                                     
      18  2. **Activity.** Find the most recent investments: the portfoli
          o page, the investor's news, portfolio-company press releases, 
          Czech and international tech/business media. Search in Czech an
          d English, e.g. `"<name>" investice`, `"<name>" investoval`, `"
          <name>" led round`, `"<name>" seed`. Record up to 3 of the most
           recent deals, preferring sources that state the announcement d
          ate. Always record the single most recent deal you found, even 
          if it is older than 24 months; code needs it to mark the invest
          or dormant.
      19     An undated page (e.g. the investor's own portfolio entry or 
          blog post with no printed date) cannot prove a recent deal: for
           the newest deals, find a dated source (the portfolio company's
           press release, a media article, a dated news post) and cite th
          at instead.
      20  3. **Profile.** `type`, `sectors` (map to the schema taxonomy a
          nd keep the investor's own wording in `raw`), `stages` (every s
          tage the source names, not just the first one), typical first `
          ticket`, `capital`, `funds`.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && cat >>
      docs/decisions.md <<'EOF'…)
  ⎿  1575f90 docs: D-019 repair pass before manual review
     faa5848 agents: extractor - registry via ARES / or.justice.cz and webs
     ite imprint, respect robots.txt (E-18)
  ⎿  Updated docs/decisions.md (+5 -0)
      71  ## D-018 · 2026-10-12 · `seed-starter-ceske-sporitelny` neextra
          huji, je to duplicita `seed-starter`
      72  - Alternativy: extrahovat oba (dva záznamy o tomtéž programu, d
          vojí náklad); doplnit alias a znovu sloučit kandidáty (mění sez
          nam kandidátů uprostřed pilotu).
      73  - Proč: oba řádky mají stejný web (seedstarter.cz) a popisují t
          entýž program České spořitelny; na shodu upozornila i triáž (ba
          tch 07). Extrahuji jen `seed-starter`. `aliases.csv` je ruční s
          eznam, proto alias nepřidávám sám: navrhuji ho Davidovi k dopln
          ění. Do té doby zůstane `seed-starter-ceske-sporitelny` v `cz_v
          c_decisions.csv` jako `pending`.
      74 +                                                               
      75 +## D-019 · 2026-10-13 · Opravný průchod před ruční kontrolou (r
         +epair_01)                                                      
      76 +- Alternativy: nechat výsledek pilotu beze změny a chyby jen po
         +psat; dohledat IČO a sídlo ručně při kontrole.                 
      77 +- Proč: šest zjevně aktivních českých VC vypadlo jen kvůli chyb
         +ějící podložené právnické osobě (K1, E-19) a u šesti dalších pi
         +peline nezjistila sídlo týmu. Prompt extraktoru navíc doporučov
         +al zdroje zakázané v robots.txt (E-18). Opravuji prompt (rejstř
         +ík: ARES / or.justice.cz, IČO z impresa webu, respektovat robot
         +s.txt) a jen pro těchto 12 záznamů znovu spouštím extrakci a kr
         +oky R4–R8. Původní záznamy, kontroly citací i verdikty ověřovat
         +ele přesouvám do `data/records/repair_01/`, takže porovnání pře
         +d/po zůstává v repozitáři. Alias `seed-starter-ceske-sporitelny
         + → seed-starter` doplněn (D-018, schválil David). Ruční kontrol
         +a tím měří pipeline po jedné opravné iteraci; v README to uvádí
         +m.                                                             
      78 +- Záznamy: czech-founders-vc, depo-ventures, kaya-vc, nation1, 
         +purposetech, zaka-vc (K1); alpha-intelligence-capital, borovick
         +a-capital, btcz-ventures, ip-lab-ventures, rockawayx, tachles (
         +neznámé sídlo).                                                

⏺ Now the alias. I'll re-run the merge and check that the only change is the
  removed duplicate.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && tail -c1
      data/candidates/aliases.csv | xxd | head -1; printf
      'seed-starter-ceske-sporitelny,seed-starter…)
  ⎿  00000000: 0a                                       .
     presto-tech-horizons,presto-ventures,"Tech Horizons is a Presto Ventur
     es fund; unit of record is the manager"
     … +20 lines (ctrl+o to expand)
  ⎿  Updated data/candidates/aliases.csv (+1 -0)
      11  ceska-sporitelna,seed-starter,"bank seen in a deal through its 
          Seed Starter programme"
      12  tachles-vc,tachles,"same fund"
      13  presto-tech-horizons,presto-ventures,"Tech Horizons is a Presto
           Ventures fund; unit of record is the manager"
      14 +seed-starter-ceske-sporitelny,seed-starter,"same Česká spořitel
         +na programme and website seedstarter.cz (D-018, approved by Dav
         +id)"                                                           
  ⎿  Updated data/candidates/cz_vc.csv (+2 -3)
      172  rtp-global,RTP Global,,,,vc,1,deals,https://www.lupa.cz/aktual
           ity/jel-se-do-berlina-jen-pobavit-marek-miltner-se-ale-vratil-
           s-investici-od-globalniho-hrace/,rtp-global,Example deal: Pang
           eAI seed (Apr 2026 article). HQ and website not identified.
      173  safar-and-partners,Safar & Partners,,,CZ,unknown,1,programmes,
           https://seedtable.com/rankings/investors/country/Czech%20Repub
           lic,safar-and-partners,"In Seedtable Czech ranking (aggregator
            lead, name only, not verified)."
      174  sandberg-capital,Sandberg Capital,https://sandbergcapital.com,
           sandbergcapital.com,SK,pe,3,cvca;deals;programmes,https://cvca
           .cz/en/sandberg-capital/ https://www.lupa.cz/aktuality/fond-sp
           ojeny-se-znamymi-podnikateli-investoval-do-seyforu-a-dalsich-t
           echnologickych-firem/ https://www.eif.org/files/records/eif-ba
           cked-active-funds.pdf,sandberg-capital,"Bratislava address on 
           CVCA profile. Buy-and-build and growth, EUR 5-20m. | Seen as s
           eller of its portfolio (Seyfor, Dotykacka, Revolgy, Educleus) 
           to J&T Arch II (Aug 2026); technology PE group founded 2014. L
           ikely PE rather than VC. Website from Lupa link. | Sandberg In
           vestment Fund II SCSp (EIF signed 2026-01-12; also CEFoF), man
           ager Sandberg Capital, sprav. spol., a.s.; CzechCrunch calls i
           t Slovak, invests in Czech firms. Awards PE Fund Manager final
           ist 2023-2025. Website per scout_cvca.csv (CVCA scout), not in
           dependently fetched here."
      175 -seed-starter,Seed Starter (Ceska sporitelna),https://www.seeds
          -tarter.cz,seedstarter.cz,CZ,cvc,1,deals,https://www.lupa.cz/ak
          -tuality/slovensky-startup-pocita-vyhodnost-it-zakazek-tisicovk
          -ami-datovych-bodu-to-prilakalo-ceske-investory/ https://cc.cz/
          -zmapovali-jsme-vsechny-investice-ktere-loni-oznamily-ceske-sta
          -rtupy-neseme-tri-dobre-a-tri-spatne-zpravy/,ceska-sporitelna;s
          -eed-starter,"Example deal: Definic seed (Jun 2026). Also Repse
          -nse (Lithuania, Dec 2025). Corporate accelerator / investment 
          -vehicle of Ceska sporitelna. Website from Lupa article link. |
          - Bank. Example deal: PalmApp (2025; CzechCrunch Jan 2026 says 
          -the bank is withdrawing). Also LP in JIC Ventures (E15 Apr 202
          -6) and owner of Seed Starter. Included as borderline; likely e
          -xcluded as bank. Website not identified without guessing."    
      176 -seed-starter-ceske-sporitelny,Seed Starter České spořitelny,,,
          -CZ,cvc,1,programmes,https://cc.cz/rozhoduji-jestli-startup-zis
          -ka-penize-profily-vice-nez-stovky-investoru-jsou-uz-na-jednom-
          -miste/,seed-starter-ceske-sporitelny,"Bank-run startup investm
          -ent programme; a Slovak version (Seed Starter Slovenskej spori
          -telne) is also named. Česká spořitelna is also an LP in Tilia,
          - i&i Bio and JIC Ventures. Website not identified."           
      175 +seed-starter,Seed Starter (Ceska sporitelna),https://www.seeds
          +tarter.cz,seedstarter.cz,CZ,cvc,2,deals;programmes,https://www
          +.lupa.cz/aktuality/slovensky-startup-pocita-vyhodnost-it-zakaz
          +ek-tisicovkami-datovych-bodu-to-prilakalo-ceske-investory/ htt
          +ps://cc.cz/zmapovali-jsme-vsechny-investice-ktere-loni-oznamil
          +y-ceske-startupy-neseme-tri-dobre-a-tri-spatne-zpravy/ https:/
          +/cc.cz/rozhoduji-jestli-startup-ziska-penize-profily-vice-nez-
          +stovky-investoru-jsou-uz-na-jednom-miste/,ceska-sporitelna;see
          +d-starter;seed-starter-ceske-sporitelny,"Example deal: Definic
          + seed (Jun 2026). Also Repsense (Lithuania, Dec 2025). Corpora
          +te accelerator / investment vehicle of Ceska sporitelna. Websi
          +te from Lupa article link. | Bank. Example deal: PalmApp (2025
          +; CzechCrunch Jan 2026 says the bank is withdrawing). Also LP 
          +in JIC Ventures (E15 Apr 2026) and owner of Seed Starter. Incl
          +uded as borderline; likely excluded as bank. Website not ident
          +ified without guessing. | Bank-run startup investment programm
          +e; a Slovak version (Seed Starter Slovenskej sporitelne) is al
          +so named. Česká spořitelna is also an LP in Tilia, i&i Bio and
          + JIC Ventures. Website not identified."                       
      176  seedtwo-capital,SeedTwo Capital,,,CA,vc,1,deals,https://www.lu
           pa.cz/aktuality/startup-z-olomouce-vyrabi-hotelierum-ai-kolegy
           -je-i-v-kempinski-a-chlubi-se-novou-investici/,seedtwo-capital
           ,"Example deal: RobosizeME USD 2M (Feb 2026, lead). Foreign fu
           nd, Canadian per the article. Website not identified."
      177  senovo,Senovo,,,CZ,vc,1,programmes,https://www.awards2024.eu/,
           senovo,"Senovo Capital; investor in IP Fabric and Manta (Award
           s 2024). HQ guessed CZ, not verified. Website not identified."
      178  seventure-partners,Seventure Partners,,,FR,vc,1,deals,https://
           www.lupa.cz/aktuality/ceska-firma-wultra-vybrala-dalsich-160-m
           ilionu-na-nasazeni-postkvantoveho-sifrovani/,seventure-partner
           s,"Example deal: Wultra Series A EUR 6.8M (Jun 2026, lead). HQ
            from prior knowledge. Website not identified."
     ...
      192  stratum-partners,Stratum Partners,https://stratum.eu,stratum.e
           u,CZ,pe,1,cvca,https://cvca.cz/en/stratum-partners-en/,stratum
           -partners,"Prague 2. Growth equity and buyouts, EUR 2-6m, CZ/S
           K."
      193  stredocesky-inovacni-centrum,Stredoceske inovacni centrum (SIC
           ),,,CZ,other,1,deals,https://www.lupa.cz/aktuality/cech-hodla-
           s-ai-namlouvat-audioknihy-pro-svetove-vydavatele-s-novymi-mili
           ony-to-chce-zkusit-z-ameriky/,stredocesky-inovacni-centrum,"Ex
           ample deal: Elredo (Oct 2026, new investor alongside JIC Ventu
           res and Bond Ventures). Regional innovation centre; unclear wh
           ether it invests equity itself. Website not identified."
      194  tachles,Tachles VC,,,CZ,vc,2,deals;programmes,https://www.lupa
           .cz/clanky/ceske-fondy-si-vysnily-americky-sen-investori-proni
           kli-do-silicon-valley-a-investuji-po-boku-americkych-gigantu/ 
           https://cc.cz/purple-presto-kaya-a-dalsi-investori-maji-apetit
           -startupove-fondy-nabiraji-dalsi-miliardy-korun/,tachles;tachl
           es-vc,"Named in Lupa Nov 2025 for a US partner helping portfol
           io firms ThreatMark and ShieldIOT; no investment in window see
           n. CzechCrunch Apr 2024 described a new fund by ex-Springtide 
           partners. Website not identified. | New fund targeting over CZ
           K 1bn, launched by Karel Tušek and David Marek, ex-Springtide 
           Ventures (CzechCrunch). Website not identified."
      196 -taiwania-capital,Taiwania Capital,,,Taiwan,vc,2,deals;programm
          -es,https://www.lupa.cz/aktuality/nejdriv-to-s-ai-nevyslo-ted-j
          -e-zde-druhy-pokus-tchaj-wan-poslal-200-milionu-do-ceskeho-star
          -tupu/ https://www.awards2024.eu/,taiwania-capital,"Example dea
          -l: Supernova Series A USD 9.2M (Sep 2025, lead). Taiwanese sta
          -te fund per Lupa. Website not identified. | Daytrip investor (
          -Series B lead per Newstream 2024) and Photoneo, Sensoneo (list
          -ed as Taiwania Fund) in Awards 2024."                         
      195 +taiwania-capital,Taiwania Capital,,,TW,vc,2,deals;programmes,h
          +ttps://www.lupa.cz/aktuality/nejdriv-to-s-ai-nevyslo-ted-je-zd
          +e-druhy-pokus-tchaj-wan-poslal-200-milionu-do-ceskeho-startupu
          +/ https://www.awards2024.eu/,taiwania-capital,"Example deal: S
          +upernova Series A USD 9.2M (Sep 2025, lead). Taiwanese state f
          +und per Lupa. Website not identified. | Daytrip investor (Seri
          +es B lead per Newstream 2024) and Photoneo, Sensoneo (listed a
          +s Taiwania Fund) in Awards 2024."                             
      196  tarpan-partners,TARPAN Partners,https://www.tarpanpartners.com
           ,tarpanpartners.com,CZ,unknown,1,cvca,https://cvca.cz/en/tarpa
           n-partners-s-r-o-2/,tarpan-partners,CVCA profile could not be 
           opened (fetch permission not granted). Own site found by domai
           n-restricted search (team and product/services pages exist); w
           hether it advises or invests is unknown. An aggregator also li
           sts it (lead only).
      197  tcf-capital,TCF Capital,,,,vc,1,programmes,https://www.awards2
           024.eu/,tcf-capital,Keboola investor (Awards 2024). HQ and web
           site not verified.
      198  tensor-ventures,Tensor Ventures,https://tensor.ventures,tensor
           .ventures,CZ,vc,3,cvca;deals;programmes,https://cvca.cz/en/ten
           sor-ventures/ https://www.lupa.cz/aktuality/ostravsky-startup-
           veri-v-ai-misto-zkuseneho-technika-s-investici-se-ma-rozsirit-
           po-evrope-i-americe/ https://cc.cz/evropsky-investicni-fond-uz
           -vlozil-penize-do-17-ceskych-fondu-miliardovy-ted-otevira-s-te
           nsor-ventures/,tensor-ventures,"Prague 1. Deeptech VC. CVCA pr
           ofile shows no website; tensor.ventures inferred from its offi
           cial blog subdomain blog.tensor.ventures (apex page not opened
           ). | Example deal: Edmund (Apr 2026, with Forward.one lead). A
           lso Cnuic (UK, Apr 2026), PangeAI (2026). Lupa May 2024 links 
           it to EIF / National Recovery Plan money. Website from Lupa ar
           ticle links. | Manager Tensor Advisory s.r.o. Tensor Co-Invest
           ment Fund SCSp is the first fund selected under the RRF Czech 
           Republic FoF (EIF up to EUR 20m; article date not checked). Al
           so in EIF Czechia list and Awards 2025 VC Fund Manager finalis
           t. Website left empty: scout_cvca.csv only inferred tensor.ven
           tures from a blog subdomain."

⏺ The merge reduced seed-starter's duplicate, leaving 224 candidates; the only
  side effect is Taiwania Capital's hq_guess normalizing from "Taiwan" to "TW,"
  which is harmless since it's just a scout hint. I'll commit this now.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && git add -A && git
      commit -qm "data: alias seed-starter-ceske-sporitelny -> seed-starter
      (D-018); re-merg…)
  ⎿  41
     57
  ⎿  Deleted data/quote_checks/alpha-intelligence-capital.json (+0 -49)
       1 -{                                                              
       2 -  "id": "alpha-intelligence-capital",                          
       3 -  "checked_at": "2026-10-13T14:01:53+00:00",                   
       4 -  "items": [                                                   
       5 -    {                                                          
       6 -      "path": "type",                                          
       7 -      "url": "https://www.maddyness.com/uk/2023/01/16/an-ai-foc
         -used-fund-with-a-tech-first-approach-a-profile-of-alpha-intelli
         -gence-capital/",                                               
       8 -      "status": "found",                                       
       9 -      "score": 100,                                            
      10 -      "http_status": 200,                                      
      11 -      "note": ""                                               
      12 -    },                                                         
      13 -    {                                                          
      14 -      "path": "sectors",                                       
      15 -      "url": "https://www.maddyness.com/uk/2023/01/16/an-ai-foc
         -used-fund-with-a-tech-first-approach-a-profile-of-alpha-intelli
         -gence-capital/",                                               
      16 -      "status": "found",                                       
      17 -      "score": 100,                                            
      18 -      "http_status": 200,                                      
      19 -      "note": ""                                               
      20 -    },                                                         
      21 -    {                                                          
      22 -      "path": "stages",                                        
      23 -      "url": "https://www.maddyness.com/uk/2023/01/16/an-ai-foc
         -used-fund-with-a-tech-first-approach-a-profile-of-alpha-intelli
         -gence-capital/",                                               
      24 -      "status": "found",                                       
      25 -      "score": 100,                                            
      26 -      "http_status": 200,                                      
      27 -      "note": ""                                               
      28 -    },                                                         
      29 -    {                                                          
      30 -      "path": "funds[0]",                                      
      31 -      "url": "https://www.maddyness.com/uk/2023/01/16/an-ai-foc
         -used-fund-with-a-tech-first-approach-a-profile-of-alpha-intelli
         -gence-capital/",                                               
      32 -      "status": "found",                                       
      33 -      "score": 100,                                            
      34 -      "http_status": 200,                                      
      35 -      "note": ""                                               
      36 -    },                                                         
      37 -    {                                                          
      38 -      "path": "evidence_of_activity[0]",                       
      39 -      "url": "https://www.mcdermottlaw.com/news/mcdermott-will-
         -schulte-advises-owkin-on-the-carve-out-of-waiv-and-its-33-milli
         -on-financing/",                                                
      40 -      "status": "found",                                       
     … 9 more lines (ctrl+o to expand)
  ⎿  Deleted data/quote_checks/borovicka-capital.json (+0 -25)
       1 -{                                                              
       2 -  "id": "borovicka-capital",                                   
       3 -  "checked_at": "2026-10-13T14:01:53+00:00",                   
       4 -  "items": [                                                   
       5 -    {                                                          
       6 -      "path": "type",                                          
       7 -      "url": "https://www.borovickacapital.com",               
       8 -      "status": "found",                                       
       9 -      "score": 100,                                            
      10 -      "http_status": 200,                                      
      11 -      "note": ""                                               
      12 -    },                                                         
      13 -    {                                                          
      14 -      "path": "evidence_of_activity[0]",                       
      15 -      "url": "https://cc.cz/poklada-jednoduche-otazky-a-tim-ule
         -hcuje-slozite-nakupy-startup-outfindo-ted-nabira-dalsi-miliony/
         -",                                                             
      16 -      "status": "found",                                       
      17 -      "score": 100,                                            
      18 -      "http_status": 200,                                      
      19 -      "note": ""                                               
      20 -    }                                                          
      21 -  ],                                                           
      22 -  "summary": {                                                 
      23 -    "found": 2                                                 
      24 -  }                                                            
      25 -}                                                              
  ⎿  Deleted data/quote_checks/btcz-ventures.json (+0 -33)
       1 -{                                                              
       2 -  "id": "btcz-ventures",                                       
       3 -  "checked_at": "2026-10-13T14:01:53+00:00",                   
       4 -  "items": [                                                   
       5 -    {                                                          
       6 -      "path": "type",                                          
       7 -      "url": "https://www.uochb.cz/en/news/756/the-butterfly-a-
         -symbol-of-hope-for-oncology-patients-chosen-as-the-emblem-of-ta
         -veren-therapeutics-a-new-biotech-company-emerging-from-iocb-pra
         -gue",                                                          
       8 -      "status": "found",                                       
       9 -      "score": 100,                                            
      10 -      "http_status": 200,                                      
      11 -      "note": ""                                               
      12 -    },                                                         
      13 -    {                                                          
      14 -      "path": "sectors",                                       
      15 -      "url": "https://www.uochb.cz/en/news/756/the-butterfly-a-
         -symbol-of-hope-for-oncology-patients-chosen-as-the-emblem-of-ta
         -veren-therapeutics-a-new-biotech-company-emerging-from-iocb-pra
         -gue",                                                          
      16 -      "status": "found",                                       
      17 -      "score": 100,                                            
      18 -      "http_status": 200,                                      
      19 -      "note": ""                                               
      20 -    },                                                         
      21 -    {                                                          
      22 -      "path": "evidence_of_activity[0]",                       
      23 -      "url": "https://www.uochb.cz/en/news/756/the-butterfly-a-
         -symbol-of-hope-for-oncology-patients-chosen-as-the-emblem-of-ta
         -veren-therapeutics-a-new-biotech-company-emerging-from-iocb-pra
         -gue",                                                          
      24 -      "status": "found",                                       
      25 -      "score": 100,                                            
      26 -      "http_status": 200,                                      
      27 -      "note": ""                                               
      28 -    }                                                          
      29 -  ],                                                           
      30 -  "summary": {                                                 
      31 -    "found": 3                                                 
      32 -  }                                                            
      33 -}                                                              
  ⎿  Deleted data/quote_checks/czech-founders-vc.json (+0 -57)
       1 -{                                                              
       2 -  "id": "czech-founders-vc",                                   
       3 -  "checked_at": "2026-10-13T14:01:53+00:00",                   
       4 -  "items": [                                                   
       5 -    {                                                          
       6 -      "path": "hq_country",                                    
       7 -      "url": "https://czechfounders.vc",                       
       8 -      "status": "found",                                       
       9 -      "score": 97,                                             
      10 -      "http_status": 200,                                      
      11 -      "note": ""                                               
      12 -    },                                                         
      13 -    {                                                          
      14 -      "path": "type",                                          
      15 -      "url": "https://cc.cz/uspesni-cesti-startupiste-budou-pom
         -ahat-novym-nadejim-vybrali-na-to-mezi-sebou-ctvrt-miliardy/",  
      16 -      "status": "found",                                       
      17 -      "score": 100,                                            
      18 -      "http_status": 200,                                      
      19 -      "note": ""                                               
      20 -    },                                                         
      21 -    {                                                          
      22 -      "path": "stages",                                        
      23 -      "url": "https://czechfounders.vc",                       
      24 -      "status": "found",                                       
      25 -      "score": 100,                                            
      26 -      "http_status": 200,                                      
      27 -      "note": ""                                               
      28 -    },                                                         
      29 -    {                                                          
      30 -      "path": "ticket",                                        
      31 -      "url": "https://czechfounders.vc",                       
      32 -      "status": "found",                                       
      33 -      "score": 100,                                            
      34 -      "http_status": 200,                                      
      35 -      "note": ""                                               
      36 -    },                                                         
      37 -    {                                                          
      38 -      "path": "evidence_of_activity[0]",                       
      39 -      "url": "https://nordic9.com/news/merchantee-raised-18-mil
         -lion-in-a-pre-seed-fu/",                                       
      40 -      "status": "found",                                       
     … 17 more lines (ctrl+o to expand)
  ⎿  Deleted data/quote_checks/depo-ventures.json (+0 -65)
       1 -{                                                              
       2 -  "id": "depo-ventures",                                       
       3 -  "checked_at": "2026-10-13T14:01:53+00:00",                   
       4 -  "items": [                                                   
       5 -    {                                                          
       6 -      "path": "hq_country",                                    
       7 -      "url": "https://depoventures.com",                       
       8 -      "status": "found",                                       
       9 -      "score": 100,                                            
      10 -      "http_status": 200,                                      
      11 -      "note": ""                                               
      12 -    },                                                         
      13 -    {                                                          
      14 -      "path": "type",                                          
      15 -      "url": "https://depoventures.com/latest/turning-any-smart
         -phone-into-a-payment-terminal-czech-fintech-tapaya-has-raised-e
         -ur-1-million",                                                 
      16 -      "status": "found",                                       
      17 -      "score": 100,                                            
      18 -      "http_status": 200,                                      
      19 -      "note": ""                                               
      20 -    },                                                         
      21 -    {                                                          
      22 -      "path": "sectors",                                       
      23 -      "url": "https://depoventures.com",                       
      24 -      "status": "found",                                       
      25 -      "score": 100,                                            
      26 -      "http_status": 200,                                      
      27 -      "note": ""                                               
      28 -    },                                                         
      29 -    {                                                          
      30 -      "path": "stages",                                        
      31 -      "url": "https://depoventures.com",                       
      32 -      "status": "found",                                       
      33 -      "score": 100,                                            
      34 -      "http_status": 200,                                      
      35 -      "note": ""                                               
      36 -    },                                                         
      37 -    {                                                          
      38 -      "path": "ticket",                                        
      39 -      "url": "https://depoventures.com",                       
      40 -      "status": "found",                                       
     … 25 more lines (ctrl+o to expand)
  ⎿  … 67 more files changed

⏺ 57 records remain in staging, and the 12 originals are in repair_01/ along
  with their quote checks and verifications. Starting re-extraction, 4 at a
  time.

⏺ 4 background agents launched (↓ to manage)
   ├ Re-extract czech-founders-vc
   ├ Re-extract depo-ventures
   ├ Re-extract kaya-vc
   └ Re-extract nation1

⏺ The setup steps are done and pushed:
  - D-019 is written in docs/decisions.md.
  - The extractor prompt fix is committed on its own: registry checks now go
    through ARES or or.justice.cz plus the IČO from the website imprint, and
    robots.txt must be respected.
  - The seed-starter alias is added. The candidate list now has 224 entries.
  - The 12 old records, with their quote checks and verifications, are moved to
    data/records/repair_01/.

  The first 4 repair extractions are running: Czech Founders VC, DEPO, KAYA VC
  and N1. The other 8 follow in rounds of 4. After that come R4–R8 for these 12
  records.

✻ Worked for 1m 1s · done 8:55 PM

› Message from investor-extractor
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/czech-founders-vc.json. src.validate passed (1/1
  valid).
  - Legal entity resolved: Czech Founders Ventures s.r.o., osoba rizikového
  kapitálu, IČO 17051835. The website footer gives the name without an IČO. I
  found the IČO through an ARES name search. The cited page is the tier-3
  kurzy.cz register mirror, which says its data came from justice.cz. Registered
  purpose lists property rental, own-asset management and consulting, not
  venture investing. The "osoba rizikového kapitálu" tag in the name is the only
  venture-capital marker.
  - hq_country is CZ, quoted from the Prague office address (Gen. Píky 430/26).
  The site also lists a Bratislava office and doesn't say where individual team
  members sit; that is noted in meta.notes.
  - Evidence: 2 items dated within 24 months. Merchantee (pre-seed, participant,
  Nordic9, 2026-06-03) is the newest; Maxfusion (CzechCrunch, 2026-01-14) has
  role and instrument unknown.
  - Left null: sectors (not published), capital (not published), funds (empty
  list; no fund size on the site). Stage is pre_seed and ticket is EUR 50-350k,
  both from the site.
  - Borderline: other 2026 deals (AdSpawn April 2026) were seen only via
  aggregators and not recorded. The separate nonprofit Czech Founders z.ú. (IČO
  09761187) is not recorded.

⏺ The Czech Founders VC record now has its legal entity and IČO, found via an
  ARES name search. But it cites a kurzy.cz mirror page despite the new prompt.
  Before deciding whether that's a violation, I'll check whether kurzy.cz's
  robots.txt actually disallows company detail pages.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && grep -o '"url":
      *"[^"]*kurzy[^"]*"' data/records/staging/czech-founders-vc.json; curl -s
      -m 15 https://r…)
  ⎿  "url": "https://rejstrik-firem.kurzy.cz/17051835/czech-founders-ventur
     es-sro/"
     User-agent: Mediapartners-Google
     … +28 lines (ctrl+o to expand)
  ⎿  (another command ran in this repository at the same time; a change 
     made by either may show under either result)

⏺ Agent "Re-extract czech-founders-vc" finished · 1m 32s

⏺ kurzy.cz's robots.txt only blocks search pages, and the cited company page is
  allowed—so no robots violation—but the agent should have cited ARES (where it
  actually found the IČO) rather than the tier-3 mirror; I'll flag this in E-19,
  log the run, and launch the next extraction.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo "2026-10-13,
      investor-extractor,sonnet,czech-founders-vc,40257,19,91.8,rerun" >>
      data/runs/run_log.c…)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      169  2026-10-13,evidence-verifier,opus,united-founders,20379,9,36.3
           ,ok
      170  2026-10-13,evidence-verifier,opus,y-soft-ventures,18965,10,37.
           7,ok
      171  2026-10-13,evidence-verifier,opus,zaka-vc,19353,10,36.6,ok
      172 +2026-10-13,investor-extractor,sonnet,czech-founders-vc,40257,1
          +9,91.8,rerun                                                  

⏺ investor-extractor(Re-extract purposetech)
  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)

⏺ Czech Founders VC is done and logged, and the PurposeTech re-extraction has
  started. Four are running now: DEPO, KAYA VC, N1 and PurposeTech. Seven of the
  12 repair records are still to start.

✻ Sautéed for 14s · done 8:57 PM

› Message from investor-extractor
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/kaya-vc.json. src.validate passed (1/1 valid).
  Evidence: 2 activity items within 24 months, newest 2026-05-19 (Viktor Series
  A, Fortune); the other is E2B Series A, 2025-07-28 (Insight Partners page).
  Legal entity: KAYA (fka Enern) s.r.o., IČO 10838821, from the ARES REST JSON
  at ares.gov.cz (tier 1). The seat is Türkova 2319/5b, Praha 4, active. The
  match is by name and rebrand, which is an inference: the website has no
  imprint or IČO. TechCrunch (2021-03-31) says "Previously called Enern". I did
  not cite TechCrunch in the record because its text carries no company number.
  Other Kaya s.r.o. entities sit at Thámova 183/11 (Kaya Advisory 22585737, Kaya
  F3 GP 19844166, and others). I did not verify them as fund vehicles. ČNB
  JERRS was not checked.
  hq_country is CZ but weakly evidenced. The site lists offices in Warsaw,
  Prague, San Francisco and London, and does not say where the team sits. The
  cited quote is the Prague address ("Thámova 183/11, 186 00"), and meta.notes
  says so.
  Fields left null: sectors (the wording "digital, physical, and consumer
  economies" does not map to the taxonomy). The hint deals TopK, E2B seed and
  Upheal could not be confirmed from dated sources.
  Borderline: the website figures (ticket $1–3M, AUM $500M, $85M current fund)
  are undated and self-reported. The ticket, AUM and fund-size quotes ("$1–3M
  Ticket", "$500M AUM Total", "$85M Current Fund") may fail the exact-quote
  check, because the label and the number sit in separate page elements. A
  decided record from an earlier run was left untouched.

⏺ KAYA VC is done. It now has a legal entity, KAYA (fka Enern) s.r.o., IČO
  10838821, from ARES (tier 1). The match is by name and rebrand only, since
  kaya.vc publishes no IČO, so you should check it in manual review. Its Czech
  base still rests only on the Prague office address. I'll log the run once its
  usage figures arrive.

✻ Sautéed for 2s · done 8:57 PM

⏺ Agent "Re-extract kaya-vc" finished · 1m 49s

› Message from investor-extractor
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/depo-ventures.json; src.validate passed (1/1).
  Legal entity confirmed: DEPO VENTURES, s.r.o., IČO 04753101. The contact page
  prints the ID, and the ARES REST API (tier 1) shows it as an active company,
  seat Plynární 1617/10, Praha 7, formerly Hagberg s.r.o. The registry quote is
  a JSON fragment, so check_quotes may find it weak. hq_country = CZ, sourced
  from the contact page address; the team location is not stated outright, so a
  Czech media quote that backs it is in the hq note.
  Evidence: 3 items, all within 24 months, newest 2026-08-28 (ArcSpace, lead,
  HeyStartup). The other two are Tapaya 2026-04-28 (co_lead, Tapaya's own blog)
  and WanderWallet 2026-03-13 (participant, CzechCrunch). DEPO's own portfolio
  and news pages carry no dates, so I did not use them for dates.
  Left null or empty: capital (the 9M€ on the home page is not labelled as AUM)
  and funds[] (DEPO Ventures One and DEPO Angels fund I are named, but no size
  was found).
  Borderline: the ticket quote "Ticket €250K - 500K" joins a label and a value
  that sit on separate lines of the home page, so check_quotes may mark it weak.
  The WanderWallet quote is a fragment ("a andělský fond Depo Ventures")
  because the sentence is split by link tags, and the ArcSpace round type (seed)
  comes from an aggregator. The hidden AI-directed text on the home page was
  ignored.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-13,investor-extractor,sonnet,kaya-vc,43254,23,108.9,rerun" >>
      data/runs/run_log.csv)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      170  2026-10-13,evidence-verifier,opus,y-soft-ventures,18965,10,37.
           7,ok
      171  2026-10-13,evidence-verifier,opus,zaka-vc,19353,10,36.6,ok
      172  2026-10-13,investor-extractor,sonnet,czech-founders-vc,40257,1
           9,91.8,rerun
      173 +2026-10-13,investor-extractor,sonnet,kaya-vc,43254,23,108.9,re
          +run                                                           

⏺ investor-extractor(Re-extract zaka-vc)
  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)

⏺ Agent "Re-extract depo-ventures" finished · 2m 6s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-13,investor-extractor,sonnet,depo-ventures,44252,29,126.1,rerun"
      >> data/runs/run_log.csv…)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      171  2026-10-13,evidence-verifier,opus,zaka-vc,19353,10,36.6,ok
      172  2026-10-13,investor-extractor,sonnet,czech-founders-vc,40257,1
           9,91.8,rerun
      173  2026-10-13,investor-extractor,sonnet,kaya-vc,43254,23,108.9,re
           run
      174 +2026-10-13,investor-extractor,sonnet,depo-ventures,44252,29,12
          +6.1,rerun                                                     

⏺ investor-extractor(Re-extract alpha-intelligence-capital)
  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)

⏺ Three repair re-extractions are done and committed: Czech Founders VC, DEPO
  and KAYA VC. All three now have a legal entity with an IČO. DEPO's IČO comes
  from its contact page and is confirmed in ARES, with three dated deals in the
  window.

  Four are running: N1, PurposeTech, Zaka VC and Alpha Intelligence Capital.
  Five are still to start: Borovička, BTCZ, IP Lab Ventures, RockawayX and
  Tachles.
✻ Crunched for 14s · done 8:58 PM

› Message from investor-extractor
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/nation1.json; src.validate passed.
  - Evidence: 1 activity item (Flick seed, Lupa.cz, 2026-05-15), within 24
  months; newest date 2026-05-15.
  - Left null or empty: legal_entities (empty), stages, ticket, funds[]. capital
  is USD 60M self-reported AUM (undated).
  - Legal entity not confirmed. n1.rocks/disclosure names Luxembourg GPs "Nation
  1 GP S.à r.l." and "Nation 1 GP II S.à r.l." with no RCS number, and the
  Luxembourg register was not retrievable. ARES has "Nation1 Investment s.r.o."
  (IČO 09172807). Its jednatelé/společníci are Jaroslav Ton and Petr Jiříček, so
  I found no link to Moravec/Trojan and did not use it. It is probably a
  namesake.
  - hq_country=CZ is borderline. The site lists offices in San Francisco, Prague
  (Národní 135/14) and Luxembourg without saying where the team sits. The only
  source is a 2021 e15 interview saying Moravec heads the fund from Prague (tier
  3). Human Archive was not recorded, because the pages I found do not name N1.

⏺ N1 Ventures is done, but its legal entity is still unconfirmed. It names only
  Luxembourg general partners (GPs) with no register number. The agent correctly
  rejected the Czech company of the same name, Nation1 Investment s.r.o.,
  because its owners don't match. So N1 will likely stay excluded under K1. I'll
  log the run once its usage figures arrive.

✻ Cooked for 2s · done 8:58 PM

⏺ Agent "Re-extract nation1" finished · 2m 28s

› Message from investor-extractor
  Written: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/purposetech.json. src.validate passed (1/1
  valid).
  - Legal entity resolved: PurposeTech s.r.o., IČO 19183992, registry CZ-OR,
  cited from the ARES API URL (tier 1). ARES seat is Drtinova 557/10, Praha 5,
  created 2023-03-24, active. The website footer names "PurposeTech, s.r.o." at
  the same address but prints no IČO, so the match is by name and address. The
  ARES quote is the JSON text `"ico":"19183992","obchodniJmeno":"PurposeTech
  s.r.o."`.
  - hq_country is CZ, sourced from Vestbee (2024-09-25, tier 3): "Prague-based
  PurposeTech". The site gives only a Prague mailing address plus unspecified
  "regional locations".
  - 2 evidence items are dated within 24 months: Auryx pre-seed (2026-04-30,
  Cambridge Enterprise page, participant; round led by Celero Ventures) and
  Lifeyear (2025-07-01, AIN.UA, participant). The newest date is 2026-04-30.
  - Left null (not_published): ticket and capital. funds[] is empty because no
  fund size is stated on any fetched page, and the hint's EUR 2.3m was not on
  the Vestbee page.
  - Borderline: the second fund PT Capital (pt.capital, HealthTech, first
  investments planned autumn 2026) is not recorded because no size is stated on
  the page. Tingit and other deals appear only on aggregators, so I did not cite
  them. The Auryx and Lifeyear sources are tier 3 (the portfolio company's
  investor list and media).

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && echo
      "2026-10-13,investor-extractor,sonnet,nation1,46519,26,147.9,rerun" >>
      data/runs/run_log.csv)
  ⎿  Updated data/runs/run_log.csv (+1 -0)
      172  2026-10-13,investor-extractor,sonnet,czech-founders-vc,40257,1
           9,91.8,rerun
      173  2026-10-13,investor-extractor,sonnet,kaya-vc,43254,23,108.9,re
           run
      174  2026-10-13,investor-extractor,sonnet,depo-ventures,44252,29,12
           6.1,rerun
      175 +2026-10-13,investor-extractor,sonnet,nation1,46519,26,147.9,re
          +run                                                           

⏺ investor-extractor(Re-extract borovicka-capital)
  ⎿  Backgrounded agent (↓ to manage · ctrl+o to expand)

⏺ Agent "Re-extract purposetech" finished · 1m 33s

› Message from investor-extractor
  - Written: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/alpha-intelligence-capital.json. src.validate
  passed.
  - Evidence dated within the last 24 months: 1 activity item (Waiv Series A,
  2026-03-19, McDermott Will & Schulte). Fund II headline (DealStreetAsia,
  2024-04-10) is older than 24 months.
  - Null fields: hq_country (conflicting_sources), ticket (not_published),
  website, legal_entities (empty). I found no imprint or registry entry.
  - hq_country stays null. Maddyness (2023) lists one partner each in the US,
  France, the UAE and Singapore. Other directories say Luxembourg, San Francisco
  or Hong Kong. No source puts the team in Czechia, and aic.group is a parked
  domain. The Slovak register (registeruz.sk) reportedly lists "Alpha
  Intelligence Capital Fund I" as a Photoneo shareholder, but I did not fetch
  it.
  - Borderline: foreign team (not Czech), so this will likely be excluded as
  out_of_scope_geography. I added Fund II at USD 150m (DealStreetAsia headline,
  "close" set to "unknown"). The "capital" field now uses that figure as
  latest_fund_size. The Waiv round is Series A per McDermott but "seed" per
  Nordic9, and the investor is one of several co-leads.

⏺ Agent "Re-extract alpha-intelligence-capital" finished · 1m 0s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && printf '%s\n'
      "2026-10-13,investor-extractor,sonnet,purposetech,41258,20,92.7,rerun"
      "2026-10-13,investo…)
  ⎿  Updated data/runs/run_log.csv (+2 -0)
      173  2026-10-13,investor-extractor,sonnet,kaya-vc,43254,23,108.9,re
           run
      174  2026-10-13,investor-extractor,sonnet,depo-ventures,44252,29,12
           6.1,rerun
      175  2026-10-13,investor-extractor,sonnet,nation1,46519,26,147.9,re
           run
      176 +2026-10-13,investor-extractor,sonnet,purposetech,41258,20,92.7
          +,rerun                                                        
      177 +2026-10-13,investor-extractor,sonnet,alpha-intelligence-capita
          +l,23827,12,60.0,rerun                                         

⏺ 2 background agents launched (↓ to manage)
   ├ Re-extract btcz-ventures
   └ Re-extract ip-lab-ventures

⏺ Six of the 12 repair re-extractions are done and committed. Results so far:

  - Legal entity confirmed: Czech Founders VC, DEPO, KAYA VC and PurposeTech, so
    these should pass K1 now.
  - Still unconfirmed: N1, which has only Luxembourg GPs with no register
    number.
  - Still no country: Alpha Intelligence Capital. No source puts its team in
    Czechia, so it will stay excluded.

  Four are running: Zaka VC, Borovička, BTCZ and IP Lab Ventures. Then come
  RockawayX and Tachles.

✻ Sautéed for 18s · done 8:59 PM

› Message from investor-extractor
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/zaka-vc.json. `src.validate` passed (1/1 valid).

  - **Legal entity:** ZAKA VC I, osoba rizikového kapitálu, a.s., IČO 21514992.
    - The IČO comes from the privacy policy on zaka.vc ("ID number: 215 14
  992").
    - ARES confirms the name and the seat at Italská 2581/67, Praha 2; I cited
  the ARES page as the tier-1 source.
    - The policy lists a second address (Panská 854/2, Prague 1) that conflicts
  with ARES. This is noted in `meta.notes`.
    - ZAKA Management s.r.o. and ZAKA Holding s.r.o. exist in ARES, but the site
  doesn't name them, so I didn't record them.
  - **hq_country:** CZ, a judgment call. The team page says the head of the
  investment committee is "currently based in Prague". The site also lists
  Silicon Valley, London and Bratislava offices, and there is a US presence.
  - **Evidence:** 3 items, all within 24 months, newest 2026-04-15 (Sygaldry
  Series A, participant). The other two are Cirrus Therapeutics (2026-02-05) and
  DeepSeq.AI (2026-01-12, role unknown). All three come from the investor's own
  dated posts, so they are self-reported.
  - **Left null:** `ticket`, because the homepage "minimum ticket is 130K" has
  no currency and sits in a qualified-investor disclaimer.
  - **Borderline:**
    - The fund size conflicts: the about page says EUR 15M (used for `capital`
  and `funds`), while the homepage shows "17M" with no currency.
    - ZAKA VC I is a ČNB-listed "risk capital entity". I did not check JERRS.
    - The portfolio is mostly biotech.

⏺ Zaka VC's legal entity is now resolved: ZAKA VC I, osoba rizikového kapitálu,
  a.s., IČO 21514992. The IČO comes from the fund's own privacy policy and is
  confirmed in ARES, the tier-1 register. Its three deals are all inside the
  window. The Czech team location remains a judgment call, since the head of the
  investment committee is based in Prague but the fund also lists offices in
  Silicon Valley, London and Bratislava. I'll log the run once its usage figures
  arrive and then start the next extraction.

✻ Worked for 2s · done 8:59 PM

⏺ Agent "Re-extract zaka-vc" finished · 1m 41s

› Message from investor-extractor
  Written: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/btcz-ventures.json. src.validate passed (1/1
  valid).
  Evidence dated within 24 months: 1 item, the Taveren Therapeutics spin-off,
  newest date 2025-12-03 (IOCB Prague page, tier 3). It says BTCZ is the largest
  shareholder. The only quote with a role names no round, so role, instrument
  and round are unknown.
  Legal entity found: BTCZ Ventures s.r.o., IČO 05277817. ARES (tier 1) shows
  seat Evropská 2758/11, Praha 6, the same address as bpd partners a.s. The
  company has no website of its own, so `website` is null.
  Left null: website, stages, ticket, capital (all not_published), funds (empty
  list).
  Borderline:
  - hq_country is CZ, resting only on the ARES registered seat. No page states
  where the team sits.
  - BTCZ is a BPD Partners Group and B3 Holding vehicle that funds biotech and
  medtech, so `type` vc is a judgment. It may be a corporate or family arm.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && printf '%s\n'
      "2026-10-13,investor-extractor,sonnet,zaka-vc,47831,17,101.2,rerun"
      "2026-10-13,investor-e…)
  ⎿  Updated data/runs/run_log.csv (+2 -0)
      175  2026-10-13,investor-extractor,sonnet,nation1,46519,26,147.9,re
           run
      176  2026-10-13,investor-extractor,sonnet,purposetech,41258,20,92.7
           ,rerun
      177  2026-10-13,investor-extractor,sonnet,alpha-intelligence-capita
           l,23827,12,60.0,rerun
      178 +2026-10-13,investor-extractor,sonnet,zaka-vc,47831,17,101.2,re
          +run                                                           
      179 +2026-10-13,investor-extractor,sonnet,btcz-ventures,,,,rerun   

⏺ 2 background agents launched (↓ to manage)
   ├ Re-extract rockawayx
   └ Re-extract tachles

⏺ Agent "Re-extract btcz-ventures" finished · 1m 14s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && sed -i ''
      's/^2026-10-13,investor-extractor,sonnet,btcz-ventures,,,,rerun$/2026-10-1
      3,investor-extractor…)
  ⎿  Updated data/runs/run_log.csv (+1 -1)
      176  2026-10-13,investor-extractor,sonnet,purposetech,41258,20,92.7
           ,rerun
      177  2026-10-13,investor-extractor,sonnet,alpha-intelligence-capita
           l,23827,12,60.0,rerun
      178  2026-10-13,investor-extractor,sonnet,zaka-vc,47831,17,101.2,re
           run
      179 -2026-10-13,investor-extractor,sonnet,btcz-ventures,,,,rerun   
      179 +2026-10-13,investor-extractor,sonnet,btcz-ventures,37191,14,73
          +.9,rerun                                                      

⏺ Eight of the 12 repair re-extractions are done and committed. Zaka VC and BTCZ
  now both have legal entities confirmed in ARES. Still running: Borovička, IP
  Lab Ventures, RockawayX and Tachles. Once those finish I'll run R4–R8 on the
  12 records.

✻ Worked for 15s · done 9:00 PM

› Message from investor-extractor
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/borovicka-capital.json and `src.validate` passed
  (1/1 valid).
  - Evidence: 1 item within 24 months, and it is the newest. Outfindo late-seed,
  2025-01-20, CzechCrunch, role participant (Eleven Ventures led).
  - Left null: `hq_country` (not_found), `sectors`, `stages`, `ticket` and
  `capital` (all not_published); `funds` is empty.
  - Legal entity: Borovicka Capital s.r.o., IČO 19966784, confirmed on the ARES
  page (seat Breitfeldova 709/17, Praha 8, established 2023-11-28). The website
  prints no IČO or imprint, so the link between the brand and the entity rests
  on the exact name match. Cited as tier 1; `meta.notes` records the linkage
  doubt.
  - Borderline: no page I could fetch says where the investment team sits
  (website, team page and CzechCrunch interview are silent). Only aggregators
  say Prague, so I left `hq_country` null rather than infer it from the ARES
  seat. Other deals (NutritionPro 2025-07-31, Edmund 2025-02-12) appear only on
  PitchBook, so I did not use them. I found no 2026 deal.

⏺ Borovička Capital is done. ARES confirms Borovicka Capital s.r.o. with a
  Prague seat, but the agent left hq_country empty: no fetched page says where
  the team works, and it wouldn't infer location from the registered seat. The
  BTCZ run did infer CZ from its ARES seat, so the two agents handled the same
  situation differently. I'll note that inconsistency in E-19. Three
  re-extractions are still running.

✻ Baked for 3s · done 9:01 PM

⏺ Agent "Re-extract borovicka-capital" finished · 2m 6s

› Message from investor-extractor
  Written: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/ip-lab-ventures.json. src.validate passed (1/1).
  - Evidence dated within 24 months: 3 (sectors, fund size, and ARES has no
  date); newest 2026-09-23. There are no evidence_of_activity items.
  - Null fields: hq_country, type, stages, ticket, capital. The candidate row
  had no website; I found https://www.iplventures.com and set it.
  - Legal entities: IP Lab Holding s.r.o., IČO 24586200, cited from the ARES
  page (seat Praha 1, registered 2026-03-05). The site footer shows "© 2026 IP
  Lab Holding s.r.o." and also lists IP Lab GP S.à r.l., RCS Luxembourg B307163
  (recorded as general partner).
  - hq_country is still null because no allowed source says where the team sits.
  Prague HQ appears only on the paywalled Private Equity International profile,
  which I did not use. The website does not state the team's location. Czech
  base is probable (Prague seat, Czech partners) but unsourced.
  - Borderline: Fund I is brand new (EIF CZK 656m, target CZK 1.2bn). I found no
  dated investment by the investor. The site lists portfolio companies
  (Atomiver, MendelFOLD and others), but they have no dates or deal terms and
  look like venture-builder projects. Type is null and no exclusion signals are
  set. I could only read the site through WebFetch, because curl got 403.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && printf '%s\n' "20
      26-10-13,investor-extractor,sonnet,borovicka-capital,40343,23,126.4,rerun"
      "2026-10-13,…)
  ⎿  Updated data/runs/run_log.csv (+2 -0)
      177  2026-10-13,investor-extractor,sonnet,alpha-intelligence-capita
           l,23827,12,60.0,rerun
      178  2026-10-13,investor-extractor,sonnet,zaka-vc,47831,17,101.2,re
           run
      179  2026-10-13,investor-extractor,sonnet,btcz-ventures,37191,14,73
           .9,rerun
      180 +2026-10-13,investor-extractor,sonnet,borovicka-capital,40343,2
          +3,126.4,rerun                                                 
      181 +2026-10-13,investor-extractor,sonnet,ip-lab-ventures,,,,rerun 

⏺ Agent "Re-extract ip-lab-ventures" finished · 2m 1s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && sed -i ''
      's/^2026-10-13,investor-extractor,sonnet,ip-lab-ventures,,,,rerun$/2026-10
      -13,investor-extract…)  ⎿  Updated data/runs/run_log.csv (+1 -1)
      178  2026-10-13,investor-extractor,sonnet,zaka-vc,47831,17,101.2,re
           run
      179  2026-10-13,investor-extractor,sonnet,btcz-ventures,37191,14,73
           .9,rerun
      180  2026-10-13,investor-extractor,sonnet,borovicka-capital,40343,2
           3,126.4,rerun
      181 -2026-10-13,investor-extractor,sonnet,ip-lab-ventures,,,,rerun 
      181 +2026-10-13,investor-extractor,sonnet,ip-lab-ventures,43318,26,
          +120.5,rerun                                                   

⏺ Ten of the 12 repair re-extractions are done and committed.

  - Borovička Capital: its legal entity is now confirmed in ARES (IČO 19966784),
    but the team location is still unknown.
  - IP Lab Ventures: ARES confirms IP Lab Holding s.r.o., but there is still no
    team location, investor type or dated investment. Fund I was only announced
    in September 2026.

  RockawayX and Tachles VC are still running. When they finish I'll start R4–R8
  on all 12.

✻ Sautéed for 11s · done 9:01 PM

› Message from investor-extractor
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/rockawayx.json. src.validate passed (1/1 valid).
  Evidence dated in the last 24 months: 4 items (Exponent seed 2026-04-30,
  Crypto Briefing 2026-08-25 for type and AUM, The Block 2025-04-24 for sector
  and fund). The newest date is 2026-08-25. The newest deal is Exponent, a seed
  round announced 2026-04-30 (The Block). RockawayX was a participant; the
  instrument is SAFE.
  Fields left null: hq_country, stages, ticket (all not_published). I did not
  assert hq_country: the homepage and Crypto Briefing say only "offices in
  London, Prague, and Dubai". The Block does not mention Prague. No source says
  where the investment team sits.
  Legal entity: Blockad s.r.o., IČO 08006458, seat Praha 6 (confirmed on the
  ARES API, tier 1). The link to the brand is the homepage footer "© 2026
  Blockad s.r.o. | RockawayX (previously Rockaway Blockchain Fund)". Role is
  null, since no source says what role the entity plays. If you accept Prague
  plus the Czech legal entity as enough, hq_country could be set to CZ. I judged
  that too weak.
  Borderline: this is a crypto/blockchain VC, mapped to sector "other". Capital
  is USD 2B reported AUM from media (tier 3). Fund II is USD 125M (The Block,
  2025-04-24). The August 2026 Relayer Capital acquisition is not recorded as an
  investment. The Exponent investor sentence and the Fund II quote are as
  returned by WebFetch and may need the quote check.

⏺ RockawayX is done. ARES confirms its legal entity, Blockad s.r.o., but the
  agent still left hq_country empty. Its offices are in London, Prague and
  Dubai, and no source says where the investment team works, so code will
  exclude it on geography. Only Tachles VC is still running; R4–R8 starts when
  it finishes.

✻ Baked for 2s · done 9:02 PM

⏺ Agent "Re-extract rockawayx" finished · 1m 30s

› Message from investor-extractor
  Wrote /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/records/staging/tachles.json. src.validate passed (1/1).
  - Evidence within 24 months: 1 item (Boost.space round, newest 2025-10-09,
  CzechCrunch, role participant behind lead Jet Investment). I dropped the
  earlier Hirundo item because its quote did not name Tachles.
  - Nulls: stages (only generic "Early-stage"), ticket, capital, funds (the ~CZK
  500m first phase has no fund label in the quote). No 2026 deal found.
  - Entity: Tachles VC Management s.r.o., IČO 14376032, active, seat Chudenická
  1059/30 Praha, cited from ARES (tier 1). The website imprint only says
  "Tachles VC Management, LLC" (Peachtree Corners GA) with no IČO, so linking
  the LLC to the s.r.o. rests on the identical name and on Tušek and Marek being
  the jednatelé (an earlier finding I did not re-verify).
  - Borderline: hq_country is set to CZ, but no source states where the team
  sits. The source (CzechCrunch 2025-02-12) calls it "Český fond Tachles VC"
  with Czech founders, and the website team page shows Czech flags for Tušek and
  Marek. The partners and offices are also in Israel and the US (Atlanta,
  Tel-Aviv, Prague). I explained this in the hq_country note. Lupa 2025-11-26
  says Tachles does not invest directly in US startups.

⏺ All 12 repair re-extractions are done. Running R4 (validate) and R5 (quote
  check) for them now.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && printf '%s\n'
      "2026-10-13,investor-extractor,sonnet,rockawayx,37167,19,89.7,rerun"
      "2026-10-13,investor-…)
  ⎿  69

     69/69 valid
     … +13 lines (ctrl+o to expand)
  ⎿  Updated data/quote_checks/3ts-capital-partners.json (+1 -1)
      1  {
      2    "id": "3ts-capital-partners",
      3 -  "checked_at": "2026-10-13T14:01:53+00:00",                    
      3 +  "checked_at": "2026-10-13T19:03:10+00:00",                    
      4    "items": [
      5      {
      6        "path": "hq_country",
  ⎿  Updated data/quote_checks/500-emerging-europe.json (+1 -1)
      1  {
      2    "id": "500-emerging-europe",
      3 -  "checked_at": "2026-10-13T14:01:53+00:00",                    
      3 +  "checked_at": "2026-10-13T19:03:10+00:00",                    
      4    "items": [
      5      {
      6        "path": "hq_country",
  ⎿  Created data/quote_checks/alpha-intelligence-capital.json (+65 -0)
       1 +{                                                              
       2 +  "id": "alpha-intelligence-capital",                          
       3 +  "checked_at": "2026-10-13T19:03:10+00:00",                   
       4 +  "items": [                                                   
       5 +    {                                                          
       6 +      "path": "type",                                          
       7 +      "url": "https://www.maddyness.com/uk/2023/01/16/an-ai-foc
         +used-fund-with-a-tech-first-approach-a-profile-of-alpha-intelli
         +gence-capital/",                                               
       8 +      "status": "found",                                       
       9 +      "score": 100,                                            
      10 +      "http_status": 200,                                      
      11 +      "note": ""                                               
      12 +    },                                                         
      13 +    {                                                          
      14 +      "path": "sectors",                                       
      15 +      "url": "https://www.maddyness.com/uk/2023/01/16/an-ai-foc
         +used-fund-with-a-tech-first-approach-a-profile-of-alpha-intelli
         +gence-capital/",                                               
      16 +      "status": "found",                                       
      17 +      "score": 100,                                            
      18 +      "http_status": 200,                                      
      19 +      "note": ""                                               
      20 +    },                                                         
      21 +    {                                                          
      22 +      "path": "stages",                                        
      23 +      "url": "https://www.maddyness.com/uk/2023/01/16/an-ai-foc
         +used-fund-with-a-tech-first-approach-a-profile-of-alpha-intelli
         +gence-capital/",                                               
      24 +      "status": "found",                                       
      25 +      "score": 100,                                            
      26 +      "http_status": 200,                                      
      27 +      "note": ""                                               
      28 +    },                                                         
      29 +    {                                                          
      30 +      "path": "capital",                                       
      31 +      "url": "https://dealstreetasia.com/?p=391288",           
      32 +      "status": "found",                                       
      33 +      "score": 100,                                            
      34 +      "http_status": 200,                                      
      35 +      "note": ""                                               
      36 +    },                                                         
      37 +    {                                                          
      38 +      "path": "funds[0]",                                      
      39 +      "url": "https://www.maddyness.com/uk/2023/01/16/an-ai-foc
         +used-fund-with-a-tech-first-approach-a-profile-of-alpha-intelli
         +gence-capital/",                                               
      40 +      "status": "found",                                       
     … 25 more lines (ctrl+o to expand)
  ⎿  Updated data/quote_checks/aspire11.json (+1 -1)
      1  {
      2    "id": "aspire11",
      3 -  "checked_at": "2026-10-13T14:01:53+00:00",                    
      3 +  "checked_at": "2026-10-13T19:03:10+00:00",                    
      4    "items": [
      5      {
      6        "path": "hq_country",
  ⎿  Updated data/quote_checks/aternus-family-office.json (+1 -1)
      1  {
      2    "id": "aternus-family-office",
      3 -  "checked_at": "2026-10-13T14:01:53+00:00",                    
      3 +  "checked_at": "2026-10-13T19:03:10+00:00",                    
      4    "items": [
      5      {
      6        "path": "hq_country",
  ⎿  … 65 more files changed
  ⎿  (timeout 10m)

⏺ Agent "Re-extract tachles" finished · 1m 45s

⏺ All 69 records validate, and the quote check found every quote in the 12
  repaired records on its page. Committing, then starting R6, the verifier on
  those 12.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && sed -i ''
      's/^2026-10-13,investor-extractor,sonnet,tachles,,,,rerun$/2026-10-13,inve
      stor-extractor,sonne…)
  ⎿  12 remaining: alpha-intelligence-capital borovicka-capital btcz-ventur
     es czech-founders-vc depo-ventures ip-lab-ventures kaya-vc nation1 pur
     posetech rockawayx tachles zaka-vc
  ⎿  Updated data/runs/run_log.csv (+1 -1)
      180  2026-10-13,investor-extractor,sonnet,borovicka-capital,40343,2
           3,126.4,rerun
      181  2026-10-13,investor-extractor,sonnet,ip-lab-ventures,43318,26,
           120.5,rerun
      182  2026-10-13,investor-extractor,sonnet,rockawayx,37167,19,89.7,r
           erun
      183 -2026-10-13,investor-extractor,sonnet,tachles,,,,rerun         
      183 +2026-10-13,investor-extractor,sonnet,tachles,39954,19,105.2,re
          +run                                                           

⏺ 4 background agents launched (↓ to manage)
   ├ Verify czech-founders-vc (repair)
   ├ Verify depo-ventures (repair)
   ├ Verify kaya-vc (repair)
   └ Verify nation1 (repair)

⏺ R4 and R5 are done and committed for the 12 repaired records. R6 verification
  is running on the first four: Czech Founders VC, DEPO, KAYA VC and N1. The
  other eight will follow as these finish.

✻ Worked for 53s · done 9:03 PM

› Message from evidence-verifier
  nation1: 4 supported, 1 partially_supported, 0 unsupported, 0 contradicted, 0
  unverifiable.
  - hq_country is only partly supported. Its only source is a 2021 E15 article
  saying managing partner Moravec runs the fund from Prague. The current
  n1.rocks site lists offices in San Francisco, Prague and Luxembourg but
  doesn't say where the team works.
  - Other items: type, sectors and the self-reported, undated USD 60M capital
  match n1.rocks. The Flick deal (Lupa.cz, 15 May 2026, USD 6M seed round, N1
  took part but did not lead) is inside the window.
  - Opinion: yes, an active VC, with Czechia likely but not firmly confirmed.
  The fund's general partners are registered in Luxembourg.
  File: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/nation1.json

⏺ N1 is verified as an active VC, likely Czech but not confirmed. It still has
  no supported legal entity, so decide will keep it out under K1. Czech Founders
  VC, DEPO and KAYA VC are still being verified. I'll log N1's run when its
  usage numbers arrive.

✻ Baked for 2s · done 9:03 PM

⏺ Agent "Verify nation1 (repair)" finished · 26s

› Message from evidence-verifier
  kaya-vc: 6 supported, 3 partially_supported, 0
  unsupported/contradicted/unverifiable. Record opinion: unsure.
  1. hq_country (partial): the site lists Prague as one of four offices (Warsaw
  is listed first, plus SF and London) and never says where the team is, so CZ
  is not shown by the cited source.
  2. legal_entities[0] (partial): ARES confirms the name and IČO 10838821, but
  its role as management company is only a guess from the name.
  3. stages (partial): the site says "pre-seed through to meaningful scale" and
  both deals are Series A, so pre_seed/seed alone is incomplete.
  File: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/kaya-vc.json

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && printf '%s\n'
      "2026-10-13,evidence-verifier,opus,nation1,16550,8,27.0,rerun"
      "2026-10-13,evidence-verifi…)
  ⎿  Updated data/runs/run_log.csv (+2 -0)
      181  2026-10-13,investor-extractor,sonnet,ip-lab-ventures,43318,26,
           120.5,rerun
      182  2026-10-13,investor-extractor,sonnet,rockawayx,37167,19,89.7,r
           erun
      183  2026-10-13,investor-extractor,sonnet,tachles,39954,19,105.2,re
           run
      184 +2026-10-13,evidence-verifier,opus,nation1,16550,8,27.0,rerun  
      185 +2026-10-13,evidence-verifier,opus,kaya-vc,,,,rerun            

⏺ 2 background agents launched (↓ to manage)
   ├ Verify purposetech (repair)
   └ Verify zaka-vc (repair)

⏺ Agent "Verify kaya-vc (repair)" finished · 29s

› Message from evidence-verifier
  depo-ventures: 8 supported, 1 partially_supported, 0 unsupported, 0
  contradicted, 0 unverifiable. Opinion: yes, an active Czech VC.
  Problem: evidence_of_activity[0] (ArcSpace) gives the round as "seed", but the
  cited HeyStartup page doesn't say what kind of round it was. The lead role
  and the 2026-08-28 date are confirmed.
  Other: the hq_country source is an office address only and doesn't say where
  the team works (minor).
  Written to: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/depo-ventures.json

⏺ Agent "Verify depo-ventures (repair)" finished · 30s

› Message from evidence-verifier
  czech-founders-vc: 7 supported, 0 partially_supported, 0 unsupported, 0
  contradicted, 0 unverifiable. Opinion: yes.
  Minor caveats: the record's quote for `hq_country` is just the Prague street
  address, the site also lists a Bratislava office, and it doesn't say where the
  team sits. The `type` subtype "founders-backed" is the extractor's own
  reading of the page; the site never says "fund".
  Output: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/czech-founders-vc.json

⏺ Agent "Verify czech-founders-vc (repair)" finished · 34s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && sed -i ''
      's/^2026-10-13,evidence-verifier,opus,kaya-vc,,,,rerun$/2026-10-13,evidenc
      e-verifier,opus,kaya…)
  ⎿  Updated data/runs/run_log.csv (+3 -1)
      182  2026-10-13,investor-extractor,sonnet,rockawayx,37167,19,89.7,r
           erun
      183  2026-10-13,investor-extractor,sonnet,tachles,39954,19,105.2,re
           run
      184  2026-10-13,evidence-verifier,opus,nation1,16550,8,27.0,rerun
      185 -2026-10-13,evidence-verifier,opus,kaya-vc,,,,rerun            
      185 +2026-10-13,evidence-verifier,opus,kaya-vc,17962,8,29.2,rerun  
      186 +2026-10-13,evidence-verifier,opus,depo-ventures,18772,11,30.1,
          +rerun                                                         
      187 +2026-10-13,evidence-verifier,opus,czech-founders-vc,17678,8,34
          +.3,rerun                                                      

⏺ 2 background agents launched (↓ to manage)
   ├ Verify alpha-intelligence-capital (repair)
   └ Verify borovicka-capital (repair)

⏺ Four of the 12 repaired records are verified and committed: Czech Founders VC,
  DEPO, KAYA VC and N1. The verifier rates Czech Founders VC and DEPO as active
  Czech VCs, and is unsure about KAYA.

  Four verifiers are running now: PurposeTech, Zaka VC, Alpha Intelligence
  Capital and Borovička. BTCZ, IP Lab Ventures, RockawayX and Tachles come next,
  then R7 decide and the R8 review sheet.

✻ Cogitated for 17s · done 9:04 PM

› Message from evidence-verifier
  purposetech: 7 supported, 0 partially_supported, 0 unsupported, 0
  contradicted, 0 unverifiable. I opened the website, Vestbee and both deal
  pages; I relied on the quote check alone for ARES.
  Serious problems: none. Minor: the only evidence that the team is in Czechia
  is the Prague address plus Vestbee's 2024 "Prague-based"; Vestbee lists EdTech
  where the site now says Future of Work.
  Opinion: yes, an active Czech pre-seed VC, with Auryx (2026-04-30) and
  Lifeyear (2025-07-01) both inside the window.
  File: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/purposetech.json

⏺ PurposeTech is verified with all 7 items supported, and the verifier rates it
  an active Czech pre-seed VC. It now has an ARES-confirmed legal entity, so it
  should pass K1 at the decide step. Three verifiers are still running: Zaka VC,
  Alpha Intelligence Capital and Borovička.

✻ Churned for 2s · done 9:04 PM

⏺ Agent "Verify purposetech (repair)" finished · 28s
› Message from evidence-verifier
  Verified borovicka-capital: 2 supported, 1 partially_supported, 0 unsupported,
  contradicted or unverifiable.
  1. `type`: "vc" matches the homepage wording, but the subtype "family
  investment company" is not on the cited page.
  2. The record has just one activity item: Outfindo, CzechCrunch, 2025-01-20,
  named as co-investor. It is inside the 24-month window, so K2 depends on it
  alone.
  3. `hq_country` is null, but the cited CzechCrunch article calls the firm
  Czech ("čeští") and ARES gives a Prague seat. My record opinion is "yes"
  (active CZ VC).
  Output: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/borovicka-capital.json

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && printf '%s\n'
      "2026-10-13,evidence-verifier,opus,purposetech,17622,9,28.2,rerun"
      "2026-10-13,evidence-ve…)
  ⎿  Updated data/runs/run_log.csv (+2 -0)
      185  2026-10-13,evidence-verifier,opus,kaya-vc,17962,8,29.2,rerun
      186  2026-10-13,evidence-verifier,opus,depo-ventures,18772,11,30.1,
           rerun
      187  2026-10-13,evidence-verifier,opus,czech-founders-vc,17678,8,34
           .3,rerun
      188 +2026-10-13,evidence-verifier,opus,purposetech,17622,9,28.2,rer
          +un                                                            
      189 +2026-10-13,evidence-verifier,opus,borovicka-capital,,,,rerun  

⏺ 2 background agents launched (↓ to manage)
   ├ Verify btcz-ventures (repair)
   └ Verify ip-lab-ventures (repair)

⏺ Agent "Verify borovicka-capital (repair)" finished · 21s

› Message from evidence-verifier
  alpha-intelligence-capital: 6 supported, 1 partially_supported, 0 unsupported,
  0 contradicted, 0 unverifiable.
  1. `capital`: the $150m is money raised so far towards a $250m target. The
  source doesn't say whether it is a first or final close, so it shouldn't be
  treated as the fund size.
  2. Opinion is "no". It is an active AI-focused VC (co-led the Waiv Series A in
  Mar 2026), but its cited offices are in the US, France, UAE and Singapore,
  with no Czech team.
  File: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/alpha-intelligence-capital.json

⏺ Agent "Verify alpha-intelligence-capital (repair)" finished · 26s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && sed -i ''
      's/^2026-10-13,evidence-verifier,opus,borovicka-capital,,,,rerun$/2026-10-
      13,evidence-verifier…)
  ⎿  Updated data/runs/run_log.csv (+2 -1)
      186  2026-10-13,evidence-verifier,opus,depo-ventures,18772,11,30.1,
           rerun
      187  2026-10-13,evidence-verifier,opus,czech-founders-vc,17678,8,34
           .3,rerun
      188  2026-10-13,evidence-verifier,opus,purposetech,17622,9,28.2,rer
           un
      189 -2026-10-13,evidence-verifier,opus,borovicka-capital,,,,rerun  
      189 +2026-10-13,evidence-verifier,opus,borovicka-capital,15102,7,21
          +.8,rerun                                                      
      190 +2026-10-13,evidence-verifier,opus,alpha-intelligence-capital,1
          +7429,8,26.6,rerun                                             

⏺ 2 background agents launched (↓ to manage)
   ├ Verify rockawayx (repair)
   └ Verify tachles (repair)

⏺ Seven of the 12 repaired records are verified and committed. Alpha
  Intelligence Capital is confirmed out of scope (no Czech team). Borovička is
  rated an active Czech VC, but its record still lacks hq_country.

  Five verifiers are running now: Zaka VC, BTCZ, IP Lab Ventures, RockawayX and
  Tachles VC. After they finish I'll run R7 (decide) and R8 (review sheet), then
  add the before/after decisions to E-19.

✻ Brewed for 16s · done 9:04 PM

› Message from evidence-verifier
  zaka-vc: 6 supported, 4 partially_supported, 0 unsupported, 0 contradicted, 0
  unverifiable. Written to /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/zaka-vc.json
  1. Fund size conflict in `capital` and `funds[0]`: the record says EUR 15M,
  from the our-story page. The homepage says "17M", labelled "Current fund size"
  and "Fund 1", with no currency.
  2. No dates on the activity pages: none of the three deal posts shows a
  publication date. Sygaldry's investment is still in window, because the page
  says it was made in June 2025. Cirrus and DeepSeq can only be dated from the
  image upload paths.
  3. `hq_country` (CZ) rests on one person: the Head of Investment Committee is
  in Prague. The team also has offices in Bratislava, London and Silicon Valley.

⏺ Zaka VC is verified, but with a new problem. The extractor described its three
  deals as coming from "dated posts", yet the verifier found no dates printed
  on those pages. Two of the dates can only be inferred from image upload paths.
  I'll note this in E-19. Four verifiers are still running.

✻ Baked for 3s · done 9:04 PM

⏺ Agent "Verify zaka-vc (repair)" finished · 45s

› Message from evidence-verifier
  btcz-ventures: 3 supported, 2 partially_supported, 0 unsupported, 0
  contradicted, 0 unverifiable. Opinion: unsure.
  1. The `type` value vc is doubtful. The cited page says BTCZ is "part of BPD
  Partners Group", founded with B3 Holding (owned by the Brůžek family). It has
  one known holding, so it may be a corporate or family arm rather than an
  independent VC.
  2. `hq_country` CZ rests only on the registered seat in ARES. No source says
  where the investment team sits.
  3. The only activity item (Taveren, 3 Dec 2025, inside the window) is
  supported, but no amount or instrument is stated.
  File: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/btcz-ventures.json

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && printf '%s\n'
      "2026-10-13,evidence-verifier,opus,zaka-vc,21654,12,45.7,rerun"
      "2026-10-13,evidence-verif…)
  ⎿  Updated data/runs/run_log.csv (+2 -0)
      188  2026-10-13,evidence-verifier,opus,purposetech,17622,9,28.2,rer
           un
      189  2026-10-13,evidence-verifier,opus,borovicka-capital,15102,7,21
           .8,rerun
      190  2026-10-13,evidence-verifier,opus,alpha-intelligence-capital,1
           7429,8,26.6,rerun
      191 +2026-10-13,evidence-verifier,opus,zaka-vc,21654,12,45.7,rerun 
      192 +2026-10-13,evidence-verifier,opus,btcz-ventures,,,,rerun      

⏺ Agent "Verify btcz-ventures (repair)" finished · 36s

› Message from evidence-verifier
  ip-lab-ventures: 3 supported, 1 partially_supported, 0
  unsupported/contradicted/unverifiable.
  1. The record has no activity evidence (empty `evidence_of_activity`), and the
  CZK 656m EIF commitment is not stated as a fund close.
  2. `hq_country` and `type` are null. cc.cz calls it a "venture kapitálový
  fond", so the null `type` is too cautious.
  3. `legal_entities[1]`: the general_partner role is inferred only from "GP" in
  the entity name. The sources also differ on fund size: CZK 1.2bn target in
  cc.cz, "až 40 milionů eur" (up to EUR 40m) in Lupa.
  Written: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/ip-lab-ventures.json

⏺ Agent "Verify ip-lab-ventures (repair)" finished · 36s

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && sed -i ''
      's/^2026-10-13,evidence-verifier,opus,btcz-ventures,,,,rerun$/2026-10-13,e
      vidence-verifier,opu…)
  ⎿  Updated data/runs/run_log.csv (+2 -1)
      189  2026-10-13,evidence-verifier,opus,borovicka-capital,15102,7,21
           .8,rerun
      190  2026-10-13,evidence-verifier,opus,alpha-intelligence-capital,1
           7429,8,26.6,rerun
      191  2026-10-13,evidence-verifier,opus,zaka-vc,21654,12,45.7,rerun
      192 -2026-10-13,evidence-verifier,opus,btcz-ventures,,,,rerun      
      192 +2026-10-13,evidence-verifier,opus,btcz-ventures,16984,6,36.5,r
          +erun                                                          
      193 +2026-10-13,evidence-verifier,opus,ip-lab-ventures,17975,8,36.7
          +,rerun                                                        

› Message from evidence-verifier
  rockawayx: 3 supported, 3 partially_supported, 0 unsupported, contradicted or
  unverifiable. Written to /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/rockawayx.json
  1. type=vc: the quote doesn't say VC. The page calls it a firm "across
  venture, credit, liquidity, and infrastructure" (multi-strategy). The USD 2B
  is firm-wide assets, not VC capital.
  2. No cited source puts the investment team in Czechia (offices in Prague,
  London, Dubai). The cited ARES page doesn't tie Blockad s.r.o. to RockawayX;
  that link rests on an uncited homepage footer.
  3. funds[0]: the name "RockawayX Fund II" and the "final" close aren't on the
  page (it says "officially closed in Q1 2025"). Opinion: unsure.

⏺ Agent "Verify rockawayx (repair)" finished · 33s

› Message from evidence-verifier
  tachles: 4 supported, 1 partially supported, 0 unsupported, 0 contradicted, 0
  unverifiable. Record opinion: unsure.
  1. hq_country is only partly supported. The article calls Tachles a "Czech
  fund" with Czech founders, but no cited source says the team sits in Prague.
  Its own website names only an Atlanta office plus Israel.
  2. The ARES legal entity matches Tachles VC by name only; no cited source
  links it to the fund.
  Activity (Boost.space, EUR 3m round, 2025-10-09) is a new deal inside the
  window, with Tachles named as co-investor.
  File: /Users/davidkoktavy/Desktop/Investor DB
  Starter/data/verification/tachles.json

⏺ Agent "Verify tachles (repair)" finished · 33s

⏺ All 12 repaired records are verified. Running R7 (decide) now, then comparing
  each record before and after the repair.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && printf '%s\n'
      "2026-10-13,evidence-verifier,opus,rockawayx,18149,9,33.0,rerun"
      "2026-10-13,evidence-veri…)
  ⎿  a06ad33
       88  none      pending
       34  pipeline  active
     … +14 lines (ctrl+o to expand)
  ⎿  Updated data/candidates/cz_vc_decisions.csv (+11 -12)
      11  akcelerator-vsem,Akcelerátor VŠEM,none,pending,,,,,,"queued, no
          t extracted",
      12  alea-capital,Alea Capital Partners,triage,excluded,out_of_scope
          _geography,pe,PT,,,"triage evidence: page, confidence medium",
      13  alfa8,alfa8,none,pending,,,,,,"queued, not extracted",
      14 -alpha-intelligence-capital,Alpha Intelligence Capital,pipeline,
         -excluded,out_of_scope_geography,vc,,Waiv,2026-03-19,hq_country 
         -unknown,capital: computed (latest_fund_size)                   
      14 +alpha-intelligence-capital,Alpha Intelligence Capital,pipeline,
         +excluded,out_of_scope_geography,vc,,Waiv,2026-03-19,capital: ve
         +rifier=partially_supported | hq_country unknown,               
      15  angelinvest,Angelinvest,none,pending,,,,,,"queued, not extracte
          d",
      16  arctern-ventures,ArcTern Ventures,none,pending,,,,,,"queued, no
          t extracted",
      17  arieli-capital,Arieli Capital,none,pending,,,,,,"queued, not ex
          tracted",
     ...
      32  bpd-partners,BPD Partners,pipeline,excluded,out_of_scope_type,f
          amily_office,CZ,Powerful Medical,2022-09-28,type: verifier=part
          ially_supported | sectors: verifier=partially_supported,
      33  braiins,Braiins,pipeline,excluded,out_of_scope_type,,CZ,Firefis
          h,2025-04-08,evidence_of_activity[0]: verifier=partially_suppor
          ted | type unknown,
      34  brightcap-ventures,BrightCap Ventures,none,pending,,,,,,"queued
          , not extracted",
      35 -btcz-ventures,BTCZ Ventures,pipeline,excluded,out_of_scope_geog
         -raphy,vc,,Taveren Therapeutics,2025-12-03,type: verifier=partia
         -lly_supported | evidence_of_activity[0]: verifier=partially_sup
         -ported | hq_country unknown,                                   
      35 +btcz-ventures,BTCZ Ventures,pipeline,active,,vc,CZ,Taveren Ther
         +apeutics,2025-12-03,hq_country: verifier=partially_supported | 
         +type: verifier=partially_supported | verifier opinion: unsure, 
      36  budeto,Budeto,pipeline,excluded,out_of_scope_type,,,Vetstor,202
          5-12-09,evidence_of_activity[0]: verifier=partially_supported |
           type unknown,
      37  category-ventures,Category Ventures,triage,excluded,out_of_scop
          e_geography,vc,US,,,"triage evidence: page, confidence medium",
      38  cb-espri,CB Espri,triage,excluded,out_of_scope_geography,unknow
          n,SK,,,"triage evidence: snippet, confidence low",
     ...
      43  crowdberry,Crowdberry,triage,excluded,out_of_scope_geography,un
          known,SK,,,"triage evidence: snippet, confidence low",
      44  cvi,CVI,triage,excluded,out_of_scope_geography,lender,PL,,,"tri
          age evidence: snippet, confidence medium",
      45  czech-business-angels-association,Czech Business Angels Associa
          tion (CBAA),none,pending,,,,,,"queued, not extracted",
      46 -czech-founders-vc,Czech Founders VC,pipeline,excluded,not_found
         -_or_defunct,vc,CZ,Merchantee,2026-06-03,"K1: no supported legal
         - entity | verifier opinion: yes, but excluded by rules",       
      46 +czech-founders-vc,Czech Founders VC,pipeline,active,,vc,CZ,Merc
         +hantee,2026-06-03,,                                            
      47  czechinvest,CzechInvest,none,pending,,,,,,"queued, not extracte
          d",
      48  danube-angels,Danube Angels,triage,excluded,out_of_scope_geogra
          phy,platform,AT,,,"triage evidence: snippet, confidence low",
      49  day-one-capital,Day One Capital,triage,excluded,out_of_scope_ge
          ography,vc,HU,,,"triage evidence: snippet, confidence medium",
      50  decibel,Decibel,none,pending,,,,,,"queued, not extracted",
      51  decibel-vc,Decibel VC,none,pending,,,,,,"queued, not extracted"
          ,
      52  dendis-capital,Dendis Capital,pipeline,excluded,out_of_scope_ty
          pe,family_office,CZ,HTG Medical,2026-07-14,"sectors: verifier=p
          artially_supported | verifier opinion: yes, but excluded by rul
          es",
      53 -depo-ventures,DEPO Ventures,pipeline,excluded,not_found_or_defu
         -nct,vc,CZ,Tapaya,2026-04-29,"K1: no supported legal entity | ve
         -rifier opinion: yes, but excluded by rules",                   
      53 +depo-ventures,DEPO Ventures,pipeline,active,,vc,CZ,ArcSpace,202
         +6-08-28,evidence_of_activity[0]: verifier=partially_supported, 
      54  dff-ventures,DFF Ventures,triage,excluded,out_of_scope_geograph
          y,vc,NL,,,"triage evidence: page, confidence medium",
      55  diaspora-ventures,Diaspora Ventures,pipeline,excluded,out_of_sc
          ope_geography,vc,US,,,ticket: verifier=partially_supported,
      56  dreamcraft-ventures,Dreamcraft Ventures,triage,excluded,out_of_
          scope_geography,vc,DK,,,"triage evidence: page, confidence medi
          um",
     ...
      103  inven-capital,Inven Capital,pipeline,active,,vc,CZ,Wint,2026-0
           9-11,capital: verifier=partially_supported,
      104  invera,Invera,triage,excluded,out_of_scope_geography,pe,HR,,,"
           triage evidence: page, confidence medium",
      105  investown,Investown,none,pending,,,,,,"queued, not extracted",
      106 -ip-lab-ventures,IP Lab Ventures,pipeline,excluded,out_of_scope
          -_geography,vc,,,,type: verifier=partially_supported | evidence
          -_of_activity[0]: verifier=partially_supported | hq_country unk
          -nown,capital: computed (latest_fund_size)                     
      106 +ip-lab-ventures,IP Lab Ventures,pipeline,excluded,out_of_scope
          +_type,,,,,legal_entities[1]: verifier=partially_supported | ty
          +pe unknown,capital: computed (latest_fund_size)               
      107  ipm,IPM,none,pending,,,,,,"queued, not extracted",
      108  irregular-expressions,Irregular Expressions,triage,excluded,ou
           t_of_scope_geography,vc,US,,,"triage evidence: page, confidenc
           e medium",
      109  itaca-business-incubator,ITACA Business Incubator,none,pending
           ,,,,,,"queued, not extracted",
     … 53 more lines (ctrl+o to expand)
  ⎿  Updated data/records/cz_vc.csv (+7 -0)
       1  id,name,website,type,hq_country,sectors,stages,ticket_min,ticke
          t_max,ticket_currency,ticket_min_eur,ticket_max_eur,ticket_sour
          ce,capital,capital_currency,capital_eur,capital_basis,capital_a
          s_of,capital_source,latest_investment,latest_investment_date,la
          test_investment_source,n_investments_in_window,legal_entity
       2  aspire11,Aspire11,https://www.aspire11cap.com,vc,CZ,generalist,
          growth,,,,,,,515000000,EUR,515000000,latest_fund_size,,https://
          www.aspire11cap.com,Vinted,2026-06-23,https://www.lupa.cz/aktua
          lity/fond-aspire11-muchy-a-borkovce-poslal-skoro-pul-miliardy-d
          o-platformy-vinted/,2,"Aspire 11 Capital SICAV, a.s. (CZ-OR 236
          20030); Partners investiční společnost, a.s. (CZ-OR 24716006)"
       3 +btcz-ventures,BTCZ Ventures,,vc,CZ,medtech;health_biotech,,,,,,
         +,,,,,,,,Taveren Therapeutics,2025-12-03,https://www.uochb.cz/en
         +/news/756/the-butterfly-a-symbol-of-hope-for-oncology-patients-
         +chosen-as-the-emblem-of-taveren-therapeutics-a-new-biotech-comp
         +any-emerging-from-iocb-prague,1,BTCZ Ventures s.r.o. (CZ-OR 052
         +77817)                                                         
       4  chilli-ventures,Chilli Ventures,https://www.chilliventures.cz,v
          c,CZ,,pre_seed;seed,200000,600000,EUR,200000,600000,https://www
          .chilliventures.cz,,,,,,,DecisionRules,2025-05-06,https://www.d
          ecisionrules.io/articles/decisionrules-raises-eu1-6m-to-scale-a
          utomation-globally,1,Chilli Ventures a.s. (CZ-OR 04106059)
       5  credo-ventures,Credo Ventures,https://www.credoventures.com,vc,
          CZ,,pre_seed,1000000,5000000,USD,894374,4471872,https://www.cre
          doventures.com,,,,,,,Picogrid,2026-05-29,https://buttondown.com
          /raisetrack/archive/angel-registry-update-may-29-2026/,2,Credo 
          Ventures a.s. (CZ-OR 28538137)
       6 +czech-founders-vc,Czech Founders VC,https://czechfounders.vc,vc
         +,CZ,,pre_seed,50000,350000,EUR,50000,350000,https://czechfounde
         +rs.vc,,,,,,,Merchantee,2026-06-03,https://nordic9.com/news/merc
         +hantee-raised-18-million-in-a-pre-seed-fu/,2,"Czech Founders Ve
         +ntures s.r.o., osoba rizikového kapitálu (CZ-OR 17051835)"     
       7 +depo-ventures,DEPO Ventures,https://depoventures.com,vc,CZ,cybe
         +rsecurity_defense;deeptech_hardware;fintech;industrial_manufact
         +uring;climate_energy,pre_seed,250000,500000,EUR,250000,500000,h
         +ttps://depoventures.com,,,,,,,ArcSpace,2026-08-28,https://www.h
         +eystartup.com/en/arcspace-secures-over-2-million-euros-to-turn-
         +disposable-satellites-into-repairable-assets,3,"DEPO VENTURES, 
         +s.r.o. (CZ-OR 04753101)"                                       
       8  fazole-ventures,Fazole Ventures,https://www.fazole.vc,vc,CZ,,se
          ed,50000,800000,EUR,50000,800000,https://www.fazole.vc/indexEN.
          html,,,,,,,Everbot,2025-09-16,https://www.lupa.cz/aktuality/sta
          rtup-z-opavy-slucuje-desitky-ai-typu-gpt-llama-ci-deepseek-do-j
          ednoho-rozhrani-ziskal-na-to-investici/,1,Fazole Ventures s.r.o
          . (CZ-OR 07491492)
       9  gi21-capital,Gi21 Capital,https://www.gi21capital.com,vc,CZ,sof
          tware_saas;ai_data;deeptech_hardware,,,,,,,,,,,,,,Hermetiq,2026
          -08-24,https://www.lupa.cz/aktuality/cesky-miliardar-investuje-
          do-americke-firmy-ktera-pomoci-ai-automatizuje-buildovani-softw
          aru/,3,Gi21 Capital a.s. (CZ-OR 19584229)
      10  i-and-i-biotech,i&i Biotech Fund (i&i Bio),https://www.inibio.e
          u,vc,CZ,health_biotech;medtech,,500000,2000000,EUR,500000,20000
          00,https://www.inibio.eu,47000000,EUR,47000000,latest_fund_size
          ,,https://www.inibio.eu/news,Antiverse,2026-03-03,https://vestb
          ee.com/insights/articles/antiverse-raises-9-3-m,2,Biotech Inves
          tments s.r.o. (CZ-OR 10885978)
     ...
      12  j-t-ventures,J&T Ventures,https://www.jtventures.cz,vc,CZ,gener
          alist,pre_seed;seed;series_a,300000,3000000,EUR,300000,3000000,
          https://www.jtventures.cz,,,,,,,Wultra,2026-06-29,https://pulse
          2.com/wultra-raises-e6-8-million-series-a-to-expand-post-quantu
          m-digital-identity-solutions/,2,J&T Ventures CG SICAV a.s. (CZ-
          OR 08220867)
      13  jic-ventures,JIC Ventures,https://www.jic.cz/ventures/,vc,CZ,de
          eptech_hardware;software_saas,pre_seed;seed,,1000000,EUR,,10000
          00,https://www.jic.cz/ventures/,400000000,CZK,16399492,latest_f
          und_size,2026-04-07,https://ctp.eu/news/ctp-becomes-largest-inv
          estor-in-new-e16-million-jic-ventures-start-up-fund/,Elredo,202
          6-10-01,https://cc.cz/driv-je-v-usa-ignorovali-ted-uz-uzaviraji
          -obri-kontrakty-a-stehuji-se-tam-navic-ziskali-dalsi-investory/
          ,3,"JIC Ventures 2 a.s., osoba rizikového kapitálu (CZ-OR 24320
          358)"
      14  jsk-investments,JSK Investments,https://www.jskinvestments.cz,v
          c,CZ,consumer_ecommerce;logistics_supply_chain;industrial_manuf
          acturing;health_biotech,pre_seed;seed,,,,,,,2000000000,CZK,8199
          7458,latest_fund_size,2025-10-01,https://www.newstream.cz/money
          /kijonkova-spousti-vlastni-fond-pro-kvalifikovane-investory,Min
          tNeuro,2026-10-09,https://www.jskinvestments.cz/cs/media/jsk-in
          vestments-sicav-a-s-investuje-do-britskeho-vyvojare-cipu-pro-ne
          urotechnologie-mint-neuro,3,JSK Investments SICAV a.s. (CZ-OR 2
          3823445)
      15 +kaya-vc,KAYA VC,https://www.kaya.vc,vc,CZ,,pre_seed;seed,100000
         +0,3000000,USD,894374,2683123,https://www.kaya.vc,500000000,USD,
         +447187193,reported_aum,,https://www.kaya.vc,Viktor,2026-05-19,h
         +ttps://fortune.com/2026/05/19/viktor-ai-startup-raises-75-milli
         +on-for-virtual-coworker-exclusive/,2,KAYA (fka Enern) s.r.o. (C
         +Z-OR 10838821)                                                 
      16  koopeo-ventures,Koopeo Ventures,https://koopeoventures.com,vc,C
          Z,,,,,,,,,,,,,,,TRIFFT Loyalty,2025-07-17,https://tech.eu/2025/
          07/17/trifft-loyalty-raises-550k-pre-seed-to-scale-its-ai-drive
          n-emotional-loyalty-platform/,1,KOOPEO Ventures SE (CZ-OR 05269
          113)
      17  lighthouse-ventures,Lighthouse Ventures,https://lhv.vc,vc,CZ,so
          ftware_saas;fintech;ai_data,pre_seed;seed,200000,1000000,EUR,20
          0000,1000000,https://lhv.vc/faq/,,,,,,,Hermetiq,2026-08-31,http
          s://lhv.vc/news-and-events/,2,Lighthouse Ventures GP s.r.o. (CZ
          -OR 07500912)
      18  look-ai-ventures,Look AI Ventures,https://lookai.vc,vc,CZ,ai_da
          ta,seed,250000,250000,EUR,250000,250000,https://tech.eu/2023/04
          /13/czech-republic-has-a-new-investment-fund-for-ai-start-ups,2
          0000000,EUR,20000000,latest_fund_size,2023-04-13,https://tech.e
          u/2023/04/13/czech-republic-has-a-new-investment-fund-for-ai-st
          art-ups,Sodex Innovations,2026-07-13,https://tech.eu/2026/07/13
          /sodex-innovations-secures-4m-to-bring-real-time-intelligence-t
          o-construction-sites/,3,"FTP Dimension investiční společnost, a
          .s. (CZ-OR 29659302)"
     ...
      20  orbit-capital,Orbit Capital,https://orbitcapital.com,vc,CZ,soft
          ware_saas,growth,,,,,,,107000000,EUR,107000000,latest_fund_size
          ,2026-07-02,https://tech.eu/2026/07/02/orbit-capital-closes-eur
          107m-venture-debt-fund-for-cee-scaleups/,IAG,2026-06-02,https:/
          /cc.cz/dalsich-140-milionu-na-rychlejsi-nakup-autodilu-cesi-cht
          eji-pomoci-mechanikum-a-miri-do-evropy/,1,"Conseq-Orbit SICAV, 
          a.s. (formerly Orbit Capital SICAV, a.s.) (CZ-OR 08223467)"
      21  presto-ventures,Presto Tech Horizons (Tech Horizons),https://pr
          estoventures.com,vc,CZ,,seed;series_a,500000,5000000,EUR,500000
          ,5000000,https://prestoventures.com,150000000,EUR,150000000,lat
          est_fund_size,2024-10-25,https://tech.eu/2024/10/25/presto-tech
          -horizons-fund-announces-investment-in-three-startups/,Occam,20
          26-02-11,https://cc.cz/investori-v-cele-s-miliardarem-michalem-
          strnadem-posilaji-desitky-milionu-na-vyvoj-autonomnich-dronu/,3
          ,"Presto Ventures II a.s., osoba rizikového kapitálu (CZ-OR 116
          78704)"
      22  purple-ventures,Purple Ventures,https://www.purple-ventures.com
          ,vc,CZ,,pre_seed;seed,250000,400000,EUR,250000,400000,https://w
          ww.purple-ventures.com,40000000,EUR,40000000,latest_fund_size,2
          024-06-27,https://tech.eu/2024/06/27/purple-ventures-launches-e
          ur40m-fund-for-early-stage-software-startups/,Fether Labs,2026-
          05-27,https://www.euro.cz/clanky/cesky-fond-purple-ventures-saz
          i-na-technologii-ovladanou-pohybem-prstu-do-britskeho-startupu-
          posilaji-11-milionu-korun/,1,Purple Ventures s.r.o. (CZ-OR 0577
          5574)
      23 +purposetech,PurposeTech,https://www.purposetech.vc,vc,CZ,health
         +_biotech;climate_energy;hr_work,pre_seed,,,,,,,,,,,,,Auryx,2026
         +-04-30,https://www.enterprise.cam.ac.uk/news/auryx-2m-earbuds-c
         +ontinuous-health-monitors/,2,PurposeTech s.r.o. (CZ-OR 19183992
         +)                                                              
      24  reflex-capital,Reflex Capital,https://www.reflexcapital.com,vc,
          CZ,,,,,,,,,,,,,,,Merchantee,2026-06-09,https://raising.fi/news/
          merchantee-undisclosed-june-2026,2,Reflex Capital SE (CZ-OR 242
          69158)
      25  rockaway-ventures,Rockaway Ventures,https://www.rockawayventure
          s.com,vc,CZ,consumer_ecommerce;logistics_supply_chain;media_gam
          ing;cybersecurity_defense;climate_energy,seed;series_a,,,,,,,,,
          ,,,,Vermeer,2025-10-23,https://vestbee.com/insights/articles/ve
          rmeer-raises-funds,2,Rockaway Ventures a.s. (CZ-OR 06387136)
      26  seed-starter,Seed Starter (Ceska sporitelna),https://www.seedst
          arter.cz,cvc,CZ,fintech,pre_seed;seed,200000,1000000,EUR,200000
          ,1000000,https://www.seedstarter.cz,,,,,,,Definic,2026-06-12,ht
          tps://cc.cz/nakup-it-sluzeb-v-korporacich-je-casto-nefunkcni-hl
          asi-do-jejich-reseni-investuje-i-ceska-sporitelna/,3,"ČS Seed S
          tarter, a.s. (CZ-OR 61058769)"
      27  soulmates-ventures,Soulmates Ventures,https://www.soulmatesvent
          ures.com,vc,CZ,climate_energy;health_biotech;agri_food;mobility
          _transport;edtech,seed,,3000000,EUR,,3000000,https://www.soulma
          tesventures.com/,50000000,EUR,50000000,latest_fund_size,2025-03
          -18,https://vestbee.com/insights/articles/soulmates-ventures-ra
          ises-50-m-fund,Rightcharge,2026-09-03,https://vestbee.com/insig
          hts/articles/rightcharge-raises-500-k,3,"Soulmates Ventures, os
          oba rizikového kapitálu, s.r.o. (CZ-OR 09789561)"
      28  springtide-ventures,Springtide Ventures,https://www.springtide.
          cz,cvc,CZ,software_saas;cybersecurity_defense;ai_data,seed;seri
          es_a;series_b_plus,1000000,10000000,USD,894374,8943744,https://
          www.springtide.cz/about/,,,,,,,ThreatMark,2025-01-07,https://th
          reatmark.com/threatmark-to-advance-the-fight-against-online-fra
          ud,1,Springtide Ventures s.r.o. (CZ-OR 01726587)
      29  startupyard,StartupYard,https://startupyard.com,vc,CZ,ai_data;d
          eeptech_hardware,pre_seed;seed,25000,25000,EUR,25000,25000,http
          s://startupyard.com/frequently-asked-questions-about-startupyar
          d/,,,,,,,Ydoca,2025-02-14,https://cc.cz/live/petkrat-rychlejsi-
          vyberova-rizeni-do-cesko-slovenske-ai-platformy-ydoca-investova
          li-depo-ventures-a-startupyard/,1,StartupYard Batch 15 s.r.o. (
          CZ-OR 22266852)
      30 +tachles,Tachles VC,https://tachlesvc.com,vc,CZ,cybersecurity_de
         +fense;ai_data,,,,,,,,,,,,,,Boost.space,2025-10-09,https://cc.cz
         +/cesi-delaji-poradek-v-datech-pro-firmy-ve-vice-nez-140-zemich-
         +sveta-ted-zaujali-i-miliardare-igora-faita/,1,Tachles VC Manage
         +ment s.r.o. (CZ-OR 14376032)                                   
      31  tensor-ventures,Tensor Ventures,https://tensor.ventures,vc,CZ,a
          i_data;deeptech_hardware;health_biotech;climate_energy,seed;ser
          ies_a,,,,,,,50000000,EUR,50000000,latest_fund_size,2024-05-15,h
          ttps://cc.cz/evropsky-investicni-fond-uz-vlozil-penize-do-17-ce
          skych-fondu-miliardovy-ted-otevira-s-tensor-ventures/,Edmund,20
          26-04-09,https://www.lupa.cz/aktuality/ostravsky-startup-veri-v
          -ai-misto-zkuseneho-technika-s-investici-se-ma-rozsirit-po-evro
          pe-i-americe/,2,Tensor Ventures a.s. (CZ-OR 06257241)
      32  tilia-impact-ventures,Tilia Impact Ventures,https://tilia.vc,vc
          ,CZ,generalist,,300000,1200000,EUR,300000,1200000,https://tilia
          .vc,,,,,,,FaceUp,2026-05-19,https://www.jic.cz/en/about-us/pro-
          media/prvni-investice-noveho-fondu-jic-ventures-miri-do,1,"Tili
          a Impact Ventures, osoba rizikového kapitálu, s.r.o. (CZ-OR 178
          48911)"
      33  united-founders,United Founders,https://www.unitedfounders.vc/,
          vc,CZ,deeptech_hardware;ai_data;cybersecurity_defense;medtech;i
          ndustrial_manufacturing;climate_energy,pre_seed;seed,100000,100
          0000,EUR,100000,1000000,https://www.unitedfounders.vc/,80000000
          ,EUR,80000000,latest_fund_size,2025-11-05,https://www.lupa.cz/a
          ktuality/havrlant-spoluzaklada-united-founders-novy-fond-chce-d
          o-evropskych-technologii-investovat-2-miliardy/,Peak Quantum,20
          26-04-14,https://www.munich-quantum-valley.de/news-events/detai
          l/peakquantum-secures-five-million-in-total-funding,2,United Fo
          unders Advisors s.r.o. (CZ-OR 21594813); United Founders SCSp (
          LU-RCS B300691)
      34  y-soft-ventures,Y Soft Ventures,https://www.ysoft.com/ventures,
          cvc,CZ,deeptech_hardware;software_saas;cybersecurity_defense;ai
          _data,pre_seed;seed,,,,,,,,,,,,,RoboTwin,2025-07-02,https://eit
          jumpstarter.eu/robotwin-secures-1-million-eur/,1,"Y Soft Ventur
          es, a.s. (CZ-OR 29314445); Y Soft Ventures II, a.s. (CZ-OR 0789
          0150)"
      35 +zaka-vc,ZAKA VC,https://zaka.vc,vc,CZ,health_biotech;industrial
         +_manufacturing,pre_seed;seed,,,,,,,15000000,EUR,15000000,latest
         +_fund_size,,https://zaka.vc/our-story/,Sygaldry Technologies,20
         +26-04-15,https://zaka.vc/sygaldry-backed-by-zaka-vc-raises-139m
         +-to-build-quantum-accelerated-ai-infrastructure/,3,"ZAKA VC I, 
         +osoba rizikového kapitálu, a.s. (CZ-OR 21514992)"              
  ⎿  Updated data/records/decided/alpha-intelligence-capital.json (+30 -13)
       6    "hq_country": {
       7      "value": null,
       8      "null_reason": "conflicting_sources",
       9 -    "note": "Maddyness lists offices in US, France, UAE, Singap
         -ore with one partner each; other directories say San Francisco/
         -Paris/Singapore or Luxembourg. No single team country establish
         -ed."                                                           
       9 +    "note": "Maddyness (2023-01-16): offices in US, France, UAE
         + and Singapore, one partner each; no Czech team found. No singl
         +e team country."                                               
      10    },
      11    "legal_entities": [],
      12    "type": {
     ...
      62    },
      63    "capital": {
      64      "value": {
      65 -      "amount": 184000000,                                     
      65 +      "amount": 150000000,                                     
      66        "currency": "USD",
      67        "basis": "latest_fund_size",
      68 -      "as_of": "2023-01-16"                                    
      68 +      "as_of": "2024-04-10"                                    
      69      },
      70      "source": {
      71 -      "url": "https://www.maddyness.com/uk/2023/01/16/an-ai-foc
         -used-fund-with-a-tech-first-approach-a-profile-of-alpha-intelli
         -gence-capital/",                                               
      71 +      "url": "https://dealstreetasia.com/?p=391288",           
      72        "tier": 3,
      73 -      "publisher": "Maddyness",                                
      74 -      "published_date": "2023-01-16",                          
      73 +      "publisher": "DealStreetAsia",                           
      74 +      "published_date": "2024-04-10",                          
      75        "accessed_date": "2026-10-13",
      76 -      "quote": "the team raised a first fund of 184m$ to back i
         -nnovative companies with strong algorithmic science expertise."
         -,                                                              
      76 +      "quote": "Alpha Intelligence Capital raises $150m for sec
         +ond AI fund, targets $250m",                                   
      77        "self_reported": false
      78 -    },                                                         
      79 -    "note": "computed by decide.py from 1 fund size(s) in funds
         -[]; source is the newest fund's source"                        
      78 +    }                                                          
      79    },
      80    "funds": [
      81      {
     ...
       95          "quote": "the team raised a first fund of 184m$ to bac
           k innovative companies with strong algorithmic science experti
           se.",
       96          "self_reported": false
       97        }
       98 +    },                                                        
     … 37 more lines (ctrl+o to expand)
  ⎿  Updated data/records/decided/borovicka-capital.json (+26 -9)
       6    "hq_country": {
       7      "value": null,
       8      "null_reason": "not_found",
       9 -    "note": "Only third-party aggregator profiles say Prague; n
         -o primary or media page fetched states where the team sits."   
       9 +    "note": "No fetched primary or media page states where the 
         +investment team sits. ARES gives the s.r.o. seat in Praha 8 and
         + aggregators (not usable) say Prague, but the team location its
         +elf is not stated."                                            
      10    },
      11 -  "legal_entities": [],                                        
      11 +  "legal_entities": [                                          
      12 +    {                                                          
      13 +      "name": "Borovicka Capital s.r.o.",                      
      14 +      "registry": "CZ-OR",                                     
      15 +      "registry_id": "19966784",                               
      16 +      "role": "management_company",                            
      17 +      "source": {                                              
      18 +        "url": "https://ares.gov.cz/ekonomicke-subjekty-v-be/re
         +st/ekonomicke-subjekty/19966784",                              
      19 +        "tier": 1,                                             
      20 +        "publisher": "ARES (Ministerstvo financí ČR)",         
      21 +        "published_date": null,                                
      22 +        "accessed_date": "2026-10-13",                         
      23 +        "quote": "\"ico\":\"19966784\",\"obchodniJmeno\":\"Boro
         +vicka Capital s.r.o.\"",                                       
      24 +        "self_reported": false                                 
      25 +      }                                                        
      26 +    }                                                          
      27 +  ],                                                           
      28    "type": {
      29      "value": "vc",
      14 -    "subtype": "family fund",                                  
      30 +    "subtype": "family investment company",                    
      31      "source": {
      32        "url": "https://www.borovickacapital.com",
      33        "tier": 2,
      34        "publisher": "Borovicka Capital",
      35        "published_date": null,
      36        "accessed_date": "2026-10-13",
      21 -      "quote": "strategic focus on venture capital investments 
         -in the Central European region.",                              
      37 +      "quote": "Borovicka Capital is an investment company with
         + a strategic focus on venture capital investments",            
      38        "self_reported": true
      39      }
      40    },
     ...
      44    },
     … 31 more lines (ctrl+o to expand)
  ⎿  Updated data/records/decided/btcz-ventures.json (+39 -16)
       4    "name": "BTCZ Ventures",
       5    "website": null,
       6    "hq_country": {
       7 -    "value": null,                                             
       8 -    "null_reason": "not_published",                            
       9 -    "note": "No page found stating the team location; website n
         -ot identified."                                                
       7 +    "value": "CZ",                                             
       8 +    "source": {                                                
       9 +      "url": "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest
         +/ekonomicke-subjekty/05277817",                                
      10 +      "tier": 1,                                               
      11 +      "publisher": "ARES (Ministerstvo financí ČR)",           
      12 +      "published_date": null,                                  
      13 +      "accessed_date": "2026-10-13",                           
      14 +      "quote": "\"textovaAdresa\":\"Evropská 2758/11, Dejvice, 
         +16000 Praha 6\"",                                              
      15 +      "self_reported": false                                   
      16 +    },                                                         
      17 +    "note": "Registered seat of BTCZ Ventures s.r.o. in Prague;
         + no page found that states the team location explicitly."      
      18    },
      11 -  "legal_entities": [],                                        
      19 +  "legal_entities": [                                          
      20 +    {                                                          
      21 +      "name": "BTCZ Ventures s.r.o.",                          
      22 +      "registry": "CZ-OR",                                     
      23 +      "registry_id": "05277817",                               
      24 +      "role": "management_company",                            
      25 +      "source": {                                              
      26 +        "url": "https://ares.gov.cz/ekonomicke-subjekty-v-be/re
         +st/ekonomicke-subjekty/05277817",                              
      27 +        "tier": 1,                                             
      28 +        "publisher": "ARES (Ministerstvo financí ČR)",         
      29 +        "published_date": null,                                
      30 +        "accessed_date": "2026-10-13",                         
      31 +        "quote": "\"ico\":\"05277817\",\"obchodniJmeno\":\"BTCZ
         + Ventures s.r.o.\"",                                           
      32 +        "self_reported": false                                 
      33 +      }                                                        
      34 +    }                                                          
      35 +  ],                                                           
      36    "type": {
      37      "value": "vc",
      38      "subtype": null,
     ...
      41        "tier": 3,
     … 51 more lines (ctrl+o to expand)
  ⎿  … 11 more files changed

  Ran 1 shell command (ctrl+o to expand)

⏺ The repair reactivated 7 records (Czech Founders, DEPO, KAYA, PurposeTech,
  Zaka, BTCZ, Tachles), left N1, Alpha, Borovička and RockawayX excluded,
  reclassified IP Lab's exclusion reason, and removed the merged
  duplicate—bringing active records from 27 to 34. I'll log this before/after
  comparison in E-19.

⏺ Bash(cd "/Users/davidkoktavy/Desktop/Investor DB Starter" && cat >>
      docs/ai-errors.md <<'EOF'…)
  ⎿  342 review rows -> /Users/davidkoktavy/Desktop/Investor DB Starter/dat
     a/manual_review/cz_vc_todo.csv and /Users/davidkoktavy/Desktop/Investo
     r DB Starter/data/manual_review/review.html
     … +4 lines (ctrl+o to expand)
  ⎿  Updated docs/ai-errors.md (+21 -0)
      25  | E-19 | 2026-10-13 | investor-extractor | czech-founders-vc, d
          epo-ventures, kaya-vc, nation1, purposetech, zaka-vc | `legal_e
          ntities` | U šesti aktivních VC (ověřovatel u většiny „yes“) ex
          traktor nenašel nebo nezapsal právnickou osobu, takže `decide.p
          y` je podle K1 vyřadil s kódem `not_found_or_defunct`. U Czech 
          Founders VC první (zkušební) běh IČO z or.justice.cz našel, dru
          hý ne: výsledek extrakce je nestabilní. Kód `not_found_or_defun
          ct` je navíc pro aktivní fond zavádějící. | `decide.py`, přízna
          k „verifier opinion: yes, but excluded by rules“ + „K1: no supp
          orted legal entity“. | Zatím nic (pravidlo K1 je v PLAN). Návrh
           pro Davida: buď dohledat IČO ručně při kontrole, nebo extrakto
          ru přikázat ARES API (viz E-18) a znovu spustit jen tyto záznam
          y; zvážit samostatný kód vyřazení „identity_unconfirmed“. |
      26  | E-20 | 2026-10-13 | investor-extractor | braiins, tachles, no
          vira-capital | `evidence_of_activity[].announced_date` | Datum 
          článku použito jako datum investice: Braiins (podíl ve Firefish
           09/2024, blog 04/2025), Tachles (rekapitulace investic za 2024
           v článku 02/2025), Novira (investice 2020, článek o exitu 2023
          ). Přesně chyba „datum článku ≠ datum investice“ z PLAN §5.3. |
           Ověřovatel (R6). | Nic; ověřovatel ji zachytil, záznamy jsou s
          tejně vyřazené z jiných důvodů. Pro další běh: v promptu výslov
          ně „rekapitulace není oznámení“. |
      27  | E-21 | 2026-10-13 | evidence-verifier | inven-capital, btcz-v
          entures | `evidence_of_activity[0]` | Ověřovatel nezachytil rol
          i `co_lead` u Inven/Wint převzatou ze snippetu (E-13) a u BTCZ/
          Taveren dal jen `partially_supported`, ačkoli zdroj investici B
          TCZ v okně nedokládá (E-14). `decide.py` počítá `partially_supp
          orted` jako podložené, takže položky zůstaly. | Orchestrátor po
          rovnáním se zprávami extraktoru. | Zatím nic; vstup pro metriku
           shody ověřovatele s ruční kontrolou. BTCZ je stejně vyřazen (n
          eznámé sídlo). |
      28 +                                                               
      29 +### E-19 · opravný průchod repair_01 (D-019), 2026-10-13: rozho
         +dnutí před → po                                                
      30 +                                                               
      31 +Upravený prompt (rejstřík přes ARES / or.justice.cz a IČO z imp
         +resa webu), znovu extrakce, citace, ověřovatel a `decide.py` je
         +n pro těchto 12 záznamů. Původní soubory jsou v `data/records/r
         +epair_01/`.                                                    
      32 +                                                               
      33 +| Záznam | Před | Po | Co se změnilo |                         
      34 +|---|---|---|---|                                              
      35 +| czech-founders-vc | excluded `not_found_or_defunct` (K1) | **
         +active** | IČO 17051835 (nalezeno přes ARES, citováno zrcadlo k
         +urzy.cz, které robots.txt u detailu firmy povoluje); ověřovatel
         + 7/7 podloženo |                                               
      36 +| depo-ventures | excluded `not_found_or_defunct` (K1) | **acti
         +ve** | IČO 04753101 z kontaktní stránky, potvrzeno v ARES; 3 da
         +tované investice v okně |                                      
      37 +| kaya-vc | excluded `not_found_or_defunct` (K1) | **active** |
         + KAYA (fka Enern) s.r.o., IČO 10838821 z ARES; shoda jen podle 
         +názvu a přejmenování, sídlo týmu jen částečně podložené; ověřov
         +atel „unsure“ |                                                
      38 +| purposetech | excluded `not_found_or_defunct` (K1) | **active
         +** | IČO 19183992 z ARES (shoda názvu a adresy); ověřovatel 7/7
         + |                                                             
      39 +| zaka-vc | excluded `not_found_or_defunct` (K1) | **active** |
         + IČO 21514992 ze zásad ochrany osobních údajů na webu, potvrzen
         +o v ARES; data investic nejsou na stránkách vytištěná (extrakto
         +r je uvedl jako datovaná, ověřovatel ne) |                     
      40 +| nation1 | excluded `not_found_or_defunct` (K1) | excluded `no
         +t_found_or_defunct` (beze změny) | jen lucemburské GP bez čísla
         + RCS; česká Nation1 Investment s.r.o. je jmenovec (jiní společn
         +íci), správně nepoužita |                                      
      41 +| btcz-ventures | excluded `out_of_scope_geography` | **active*
         +* | BTCZ Ventures s.r.o., IČO 05277817 z ARES; sídlo CZ jen pod
         +le sídla v rejstříku; typ `vc` sporný (vehikulum BPD Partners);
         + ověřovatel „unsure“ |                                         
      42 +| tachles | excluded `out_of_scope_geography` | **active** | CZ
         + podle CzechCrunch („Český fond“); nová investice Boost.space 2
         +025-10-09; vazba IČO 14376032 na fond jen podle názvu; ověřovat
         +el „unsure“ |                                                  
      43 +| alpha-intelligence-capital | excluded `out_of_scope_geography
         +` | excluded `out_of_scope_geography` (beze změny) | tým v USA/
         +FR/SAE/SG, žádný český tým |                                   
      44 +| borovicka-capital | excluded `out_of_scope_geography` | exclu
         +ded `out_of_scope_geography` (beze změny) | IČO 19966784 z ARES
         + nalezeno, ale sídlo týmu ze zdroje nedoloženo; ověřovatel „yes
         +“ |                                                            
      45 +| rockawayx | excluded `out_of_scope_geography` | excluded `out
         +_of_scope_geography` (beze změny) | Blockad s.r.o. z ARES, ale 
         +kanceláře Londýn/Praha/Dubaj bez určení týmu; multistrategická 
         +krypto firma |                                                 
      46 +| ip-lab-ventures | excluded `out_of_scope_geography` | exclude
         +d `out_of_scope_type` | IP Lab Holding s.r.o. z ARES; typ a síd
         +lo `null`, žádná datovaná investice (fond oznámen 09/2026) |   
      47 +                                                               
      48 +Shrnutí: 7 z 12 záznamů přešlo do `active` (aktivních celkem 27
         + → 34). Extrakce je nestabilní ve dvou směrech: (a) stejný agen
         +t u stejného kandidáta jednou IČO najde, jindy ne; (b) dva extr
         +aktoři řeší stejnou situaci různě: u BTCZ odvodil sídlo týmu ze
         + sídla v rejstříku, u Borovička Capital to odmítl. Navíc u ip-l
         +ab-ventures nechal typ `null`, ačkoli zdroj píše „venture kapit
         +álový fond“ (ověřovatel: „příliš opatrné“). Pravidlo pro sídlo 
         +(sídlo v rejstříku ≠ sídlo týmu) chybí v promptu i v PLAN a je 
         +to kandidát na další rozhodnutí.                               
  ⎿  … 2 more files changed

⏺ The repair pass is finished. 7 of the 12 records moved from excluded to
  active, so the database now has 34 active records instead of 27. I stopped
  after R8, and everything is committed and pushed.

  What I did:
  - D-019 is written in docs/decisions.md.
  - Extractor prompt: the kurzy.cz/firmy.cz tip is replaced with ARES /
    or.justice.cz plus the IČO from the website imprint, and robots.txt must be
    respected. That change is in its own agents: commit.
  - Alias seed-starter-ceske-sporitelny → seed-starter is added. The candidate
    list is now 224. The re-merge also changed Taviwania Capital's hq_guess from
    "Taiwan" to "TW"; it's only a scout hint, so it's harmless.
  - The 12 old records (6 flagged "no supported legal entity", 6 flagged
    "hq_country unknown") are in data/records/repair_01/, with their quote
    checks and verifications.
  - R4–R8 for those 12: all valid, every quote found on its page, all verified.
    Then I ran decide and regenerated the review sheet, which now has 342 rows.

  Before → after (full table in E-19 in docs/ai-errors.md):

  ┌───────────────────────────────────┬─────────────────────────────────────┐
  │        Moved to active (7)        │         Still excluded (5)          │
  ├───────────────────────────────────┼─────────────────────────────────────┤
  │ Czech Founders VC, DEPO, KAYA VC, │ N1: no legal entity with a register │
  │  PurposeTech, Zaka VC: legal      │  number                             │
  │ entity found                      │                                     │
  ├───────────────────────────────────┼─────────────────────────────────────┤
  │ BTCZ, Tachles VC: Czech base now  │ Alpha Intelligence Capital,         │
  │ recorded                          │ Borovička, RockawayX: team location │
  │                                   │  still unknown                      │
  ├───────────────────────────────────┼─────────────────────────────────────┤
  │                                   │ IP Lab Ventures: now excluded on    │
  │                                   │ type instead of geography           │
  └───────────────────────────────────┴─────────────────────────────────────┘

  Worth your attention during review:
  - Shaky new actives. KAYA, BTCZ and Tachles got verifier opinion "unsure".
    Their Czech base or their link to the legal entity rests on a registered
    seat or a name match.
  - Zaka VC deal dates. None are printed on the pages, so the dates come from
    image upload paths.
  - Inconsistent location handling. One extractor inferred the team's country
    from the registered seat (BTCZ); another refused to (Borovička). Neither the
    prompt nor PLAN says whether a registered seat counts as the team's
    location, and you'll need to decide that.
  - Citation slip. The Czech Founders extractor found the IČO through ARES but
    cited the kurzy.cz company page. That page is allowed by robots.txt (only
    search pages are blocked), but the new prompt asked for ARES.

  Your next steps are unchanged: the manual review in
  data/manual_review/review.html, then /export of the session log, then R9
  metrics.

✻ Worked for 11m 13s · done 9:06 PM