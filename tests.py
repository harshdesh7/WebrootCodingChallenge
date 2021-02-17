import unittest
import pickle

class TestServerFunctionality(unittest.TestCase):

    def clearFileHelper(self, file_sim):
        open(file_sim, 'wb').close()

    def test_addUserToEmptyDB(self):

        self.clearFileHelper("db_sim.pickle") #clear out db

        user: dict[str, str] = {"tstUsr": "password"}
        pick = open("db_sim.pickle", "wb")
        pickle.dump(user, pick)
        pick.close()

        pick_off = open("db_sim.pickle", "rb")
        usr = pickle.load(pick_off)
        pick_off.close()

        self.assertEqual(usr["tstUsr"], "password")

    def test_addUserToFilledDB(self):

        pick_off = open("db_sim.pickle", "rb")
        usr = pickle.load(pick_off)
        pick_off.close()

        usr["tstUsr2"] = "tc2"

        # put dictionary back into pickle file (equivalent to DB modification)
        pick = open("db_sim.pickle", "wb")
        pickle.dump(usr, pick)
        pick.close()

        # get dictionary back (equivalent to DB query)
        pick_off = open("db_sim.pickle", "rb")
        retrieved = pickle.load(pick_off)
        pick_off.close()

        self.assertEqual(retrieved["tstUsr"], "password")
        self.assertEqual(retrieved["tstUsr2"], "tc2")

    def test_deleteUserFromDB(self):

        pick_off = open("db_sim.pickle", "rb")
        usr = pickle.load(pick_off)
        pick_off.close()

        del usr["tstUsr2"] #remove entry from dictionary

        # put dictionary back into pickle file (equivalent to DB modification)
        pick = open("db_sim.pickle", "wb")
        pickle.dump(usr, pick)
        pick.close()

        # get dictionary back (equivalent to DB query)
        pick_off = open("db_sim.pickle", "rb")
        retrieved = pickle.load(pick_off)
        pick_off.close()

        self.assertEqual(retrieved["tstUsr"], "password")
        self.assertTrue("tstUsr2" not in retrieved)

        self.clearFileHelper("db_sim.pickle") #clear db file

    def test_addToEmptyCookieSet(self):

        self.clearFileHelper("cookie_sim.pickle")
        cookieJar: set[str] = set(["cookie1"]) #cookie jar will be set of cookies

        pick = open("cookie_sim.pickle", "wb")
        pickle.dump(cookieJar, pick)
        pick.close()

        pick_off = open("cookie_sim.pickle", "rb")
        cJar = pickle.load(pick_off)
        pick_off.close()

        self.assertTrue("cookie1" in cJar)

    def test_addToFilledCookieSet(self):

        pick_off = open("cookie_sim.pickle", "rb")
        cJar = pickle.load(pick_off)
        pick_off.close()

        cJar.add("cookie2")

        pick = open("cookie_sim.pickle", "wb")
        pickle.dump(cJar, pick)
        pick.close()

        pick_off = open("cookie_sim.pickle", "rb")
        cJar = pickle.load(pick_off)
        pick_off.close()

        self.assertTrue("cookie1" in cJar)
        self.assertTrue("cookie2" in cJar)

    def test_deleteFromCookieSet(self):

        pick_off = open("cookie_sim.pickle", "rb")
        cJar = pickle.load(pick_off)
        pick_off.close()

        self.assertTrue("cookie2" in cJar)
        cJar.remove("cookie2")

        pick = open("cookie_sim.pickle", "wb")
        pickle.dump(cJar, pick)
        pick.close()

        pick_off = open("cookie_sim.pickle", "rb")
        cJar = pickle.load(pick_off)
        pick_off.close()

        self.assertTrue("cookie1" in cJar)
        self.assertTrue("cookie2" not in cJar)

        self.clearFileHelper("cookie_sim.pickle") #clear cookie file



if __name__ == '__main__':
    unittest.main()



