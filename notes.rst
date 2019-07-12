- Metinis pirkimų planas (Anual Procurement Plan (APP))

  PLANNED_PROCUREMENT

  unikalus id: external

  parties:

    PLANNED_PROCUREMENT
    - NAME
    - ORG_NR

  amounts:

    PLANNED_PROCUREMENT
    - PLANNED_VALUE (valiuta)
    - PLANNED_SCOPE (kiekis)
    
  items:

    PLANNED_PROCUREMENT
    - PUSHASE_TYPE
    - TITLE

    PLANNED_PROCUREMENT_CPV_CODES - tas pats kas BVPŽ kodai

  periods:
    
    PLANNED_PROCUREMENT
    - ANTICIPATED_* laukai, gali būti datos arba ketvirčiai


- F02_2014 - pirkimo skelbimas

  laukai:

     - CVPIS_APPENDIX_NUMBER - siejasi su CVPIS_APPENDIX.ID

  CVPIS_APPENDIX (laukas EXTERNAL_REF)

  laukai:

    - EXTERNAL_REF - siejasi su ATN1.PROCUEMENT_NUMBER

  parties:

    Įstaiga gali pirkti sau arba kitai, reikia išsiaiškinti, kaip tai
    identifikuoti lentelėse.

  amounts

    F02_2014

      - VAL_ESTIMATED_TOTAL - bendra vertė viso pirkimo, be pvm

  items:

    F02_OBJECT_DESC

      - VAL_OBJECT - pirkimo vertė, atskiros pirkimo dalies
                     laukas F02_2014.LOT_DIVISION, jei 1 tai pirkimas skaidomas
                     į dalis, jei 0 tai neskaidomas

  periods:
    

- ATN1 (Ataskaita) - pagrindinė ataskaita

   laukai:

     - TENDER_ID - CVPIS_APPENDIX.EXTERNAL_REF
     - PROCUEMENT_NUMBER - įveda perkančioji organizacija


  ATN2 - pasikeitimų ataskaita
  ATN3 - metinė ataskaita (į ANT3 patenka maži pirkimai, kurių nėra ATN1)


  parties:
    Perkančioji organizacija (PO):
      ATN1
        - OFFICIAL_NAME_1 - tas kas gauna pregkę ar paslaugą
        - LEGAL_ENTITY_CODE_1 - įstaigos kodas
        - OFFICIAL_NAME_2 - tas kas vykdo pirkimą
        - LEGAL_ENTITY_CODE_2 - įstaigos kodas
    Konkurso dalyviai
      ATN1_TENDERER_LIST - pirkime dalyvavę dalyviai
      ATN1_DESIGN_CONTEST_WINNER_LIST - kai glai būti keli laimėtojai
      ATN1_CONTRACT_LIST - pirkimą laimėjusi organizacija
   
    Subtiekėjai:
      ATN1_SUBCONTRACTORS_CONCLUDED_TENDERER_LIST

   amounts:
     ATN1_DESIGN_CONTEST_WINNER_LIST
       - contract_total_value
     ATN1_CONTRACT_LIST
       - TOTAL_VALUE_OF_PART - suma

   items:
     ATN1_PART_OF_OBJECT_PURCHASS_LIST
     ATN1_CANTRACTED_CANDIDATE_LIST - ATN1_TENDERER_LIST ir ATN1_PART_OF_OBJECT_PURCHASS_LIST many to many
     ATN1_SEQUENCE_OF_DESIGNES_LIST - ATN1_DESIGN_CONTEST_WINNER_LIST ir ATN1_PART_OF_OBJECT_PURCHASS_LIST

- F03_2014 - skelbimas apie sutarties skyrima (tik tarptautiniams pirkimams)

    laukai:

      - CVPIS_APPENDIX_NUMBER - siejasi su CVPIS_APPENDIX.ID

- VPT_N_SUTARTYS (senoje db), nėra ryšio su skelbimais.
    




Sena VS Nauja
-------------



