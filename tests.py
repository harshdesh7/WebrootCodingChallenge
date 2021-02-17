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








if __name__ == '__main__':
    unittest.main()


