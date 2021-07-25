import requests
import json
from geopy.geocoders import Nominatim

def state_of_user(coordinates):
    # CHANGING LAT&LONG TO ADDRESS
    locator = Nominatim(user_agent= "myGeocoder")
    # location we get from the website
    location = locator.reverse(coordinates)
    location.raw
    state_of_user = location.raw["address"]["state"]
    return state_of_user


def endpoint(state):

    #1 Alabama
    if state == "Alabama":
        al = requests.get("https://www.vaccinespotter.org/api/v0/states/AL.json")
        json = al.json()
    #2 Alaska
    elif state == "Alaska":
        ak = requests.get("https://www.vaccinespotter.org/api/v0/states/AK.json")
        json = ak.json()
    #3 Arizona
    elif state == "Arizona":
        az = requests.get("https://www.vaccinespotter.org/api/v0/states/AZ.json")
        json = az.json()
    #4 Arkansas
    elif state == "Arkansas":
        ar = requests.get("https://www.vaccinespotter.org/api/v0/states/AR.json")
        json = ar.json()
    #5 California
    elif state == "California":
        ca = requests.get("https://www.vaccinespotter.org/api/v0/states/CA.json")
        json = ca.json()
    #6 Colorado
    elif state == "Colorado":
        co = requests.get("https://www.vaccinespotter.org/api/v0/states/CO.json")
        json = co.json()
    #7 Connecticut
    elif state == "Connecticut":
        ct = requests.get("https://www.vaccinespotter.org/api/v0/states/CT.json")
        json = ct.json()
    #8 Delaware
    elif state == "Delaware":
        de = requests.get("https://www.vaccinespotter.org/api/v0/states/DE.json")
        json = de.json()
    #9 District of Columbia
    elif state == "District of Columbia":
        dc = requests.get("https://www.vaccinespotter.org/api/v0/states/DC.json")
        json = dc.json()
    #10 Florida
    elif state == "Florida":
        fl = requests.get("https://www.vaccinespotter.org/api/v0/states/FL.json")
        json = fl.json()
    #11 Georgia
    elif state == "Georgia":
        ga = requests.get("https://www.vaccinespotter.org/api/v0/states/GA.json")
        json = ga.json()
    #12 Hawaii
    elif state == "Hawaii":
        hi = requests.get("https://www.vaccinespotter.org/api/v0/states/HI.json")
        json = hi.json()
    #13 Idaho
    elif state == "Idaho":
        id = requests.get("https://www.vaccinespotter.org/api/v0/states/ID.json")
        json = id.json()
    #14 Illinois
    elif state == "Illinois":
        il = requests.get("https://www.vaccinespotter.org/api/v0/states/IL.json")
        json = il.json()
    #15 Indiana
    elif state == "Indiana":
        In = requests.get("https://www.vaccinespotter.org/api/v0/states/IN.json")
        json = In.json()
    #16 Iowa
    elif state == "Iowa":
        ia = requests.get("https://www.vaccinespotter.org/api/v0/states/IA.json")
        json = ia.json()
    #17 Kansas
    elif state == "Kansas":
        ks = requests.get("https://www.vaccinespotter.org/api/v0/states/KS.json")
        json = ks.json()
    #18 Kentucky
    elif state == "Kentucky":
        ky = requests.get("https://www.vaccinespotter.org/api/v0/states/KY.json")
        json = ky.json()
    #19 Louisiana
    elif state == "Louisiana":
        la = requests.get("https://www.vaccinespotter.org/api/v0/states/LA.json")
        json = la.json()
    #20 Maine
    elif state == "Maine":
        me = requests.get("https://www.vaccinespotter.org/api/v0/states/ME.json")
        json = me.json()
    #21 Maryland
    elif state == "Maryland":
        md = requests.get("https://www.vaccinespotter.org/api/v0/states/MD.json")
        json = md.json()
    #22 Massachusetts
    elif state == "Massachusetts":
        ma = requests.get("https://www.vaccinespotter.org/api/v0/states/MA.json")
        json = ma.json()
    #23 Michigan
    elif state == "Michigan":
        mi = requests.get("https://www.vaccinespotter.org/api/v0/states/MI.json")
        json = mi.json()
    #24 Minnesota
    elif state == "Minnesota":
        mn = requests.get("https://www.vaccinespotter.org/api/v0/states/MN.json")
        json = mn.json()
    #25 Mississippi
    elif state == "Mississippi":
        ms = requests.get("https://www.vaccinespotter.org/api/v0/states/MS.json")
        json = ms.json()
    #26 Missouri
    elif state == "Missouri":
        mo = requests.get("https://www.vaccinespotter.org/api/v0/states/MO.json")
        json = mo.json()
    #27 Montana
    elif state == "Montana":
        mt = requests.get("https://www.vaccinespotter.org/api/v0/states/MT.json")
        json = mt.json()
    #28 Nebraska
    elif state == "Nebraska":
        ne = requests.get("https://www.vaccinespotter.org/api/v0/states/NE.json")
        json = ne.json()
    #29 Nevada
    elif state == "Nevada":
        nv = requests.get("https://www.vaccinespotter.org/api/v0/states/NV.json")
        json = nv.json()
    #30 New Hampshire
    elif state == "New Hampshire":
        nh = requests.get("https://www.vaccinespotter.org/api/v0/states/NH.json")
        json = nh.json()
    #31 New Jersey
    elif state == "New Jersey":
        nj = requests.get("https://www.vaccinespotter.org/api/v0/states/NJ.json")
        json = nj.json()
    #32 New Mexico
    elif state == "New Mexico":
        nm = requests.get("https://www.vaccinespotter.org/api/v0/states/NM.json")
        json = nm.json()
    #33 New York
    elif state == "New York":
        ny = requests.get("https://www.vaccinespotter.org/api/v0/states/NY.json")
        json = ny.json()
    #34 North Carolina
    elif state == "North Carolina":
        nc = requests.get("https://www.vaccinespotter.org/api/v0/states/NC.json")
        json = nc.json()
    #35 North Dakota
    elif state == "North Dakota":
        nd = requests.get("https://www.vaccinespotter.org/api/v0/states/ND.json")
        json = nd.json()
    #36 Ohio
    elif state == "Ohio":
        oh = requests.get("https://www.vaccinespotter.org/api/v0/states/OH.json")
        json = oh.json()
    #37 Oklahoma
    elif state == "Oklahoma":
        ok = requests.get("https://www.vaccinespotter.org/api/v0/states/OK.json")
        json = ok.json()
    #38 Oregon
    elif state == "Oregon":
        Or = requests.get("https://www.vaccinespotter.org/api/v0/states/OR.json")
        json = Or.json()
    #39 Pennsylvania
    elif state == "Pennsylvania":
        pa = requests.get("https://www.vaccinespotter.org/api/v0/states/PA.json")
        json = pa.json()
    #40 Puerto Rico
    elif state == "Puerto Rico":
        pr = requests.get("https://www.vaccinespotter.org/api/v0/states/PR.json")
        json = pr.json()
    #41 Rhode Island
    elif state == "Rhode Island":
        ri = requests.get("https://www.vaccinespotter.org/api/v0/states/RI.json")
        json = ri.json()
    #42 South Carolina
    elif state == "South Carolina":
        sc = requests.get("https://www.vaccinespotter.org/api/v0/states/SC.json")
        json = sc.json()
    #43 South Dakota
    elif state == "South Dakota":
        sd = requests.get("https://www.vaccinespotter.org/api/v0/states/SD.json")
        json = sd.json()
    #44 Tennessee
    elif state == "Tennessee":
        tn = requests.get("https://www.vaccinespotter.org/api/v0/states/TN.json")
        json = tn.json()
    #45 Texas
    elif state == "Texas":
        tx = requests.get("https://www.vaccinespotter.org/api/v0/states/TX.json")
        json = tx.json()
    #46 Virgin Island
    elif state == "Virgin Island":
        vi = requests.get("https://www.vaccinespotter.org/api/v0/states/VI.json")
        json = vi.json()
    #47 Utah
    elif state == "Utah":
        ut = requests.get("https://www.vaccinespotter.org/api/v0/states/UT.json")
        json = ut.json()
    #48 vermont
    elif state == "vermont":
        vt = requests.get("https://www.vaccinespotter.org/api/v0/states/VT.json")
        json = vt.json()
    #49 Virginia
    elif state == "Virginia":
        va = requests.get("https://www.vaccinespotter.org/api/v0/states/VA.json")
        json = va.json()
    #50 Washington
    elif state == "Washington":
        wa = requests.get("https://www.vaccinespotter.org/api/v0/states/WA.json")
        json = wa.json()
    # West Virginia
    elif state == "West Virginia":
        wv = requests.get("https://www.vaccinespotter.org/api/v0/states/WV.json")
        json = wv.json()
    # Wisconsin
    elif state == "Wisconsin":
        wi = requests.get("https://www.vaccinespotter.org/api/v0/states/WI.json")
        json = wi.json()
    # Wyoming
    elif state == "Wyoming":
        wy = requests.get("https://www.vaccinespotter.org/api/v0/states/WY.json")
        json = wy.json()
    return json