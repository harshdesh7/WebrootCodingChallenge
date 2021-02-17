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

if __name__ == '__main__':
    unittest.main()


