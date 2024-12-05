from menu import m_fomenu
import file, kereses

alkalmazottak = file.load_json (".//ikt/alkalmazottak.json")

m_fomenu (alkalmazottak)

file.save_json (".//ikt/alkalmazottak.json", alkalmazottak)
