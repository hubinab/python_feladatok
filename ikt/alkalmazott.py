from menu import m_fomenu
import file, kereses

t_alkalmazottak = file.load_json ("alkalmazottak.json")

m_fomenu (list=t_alkalmazottak)

#kereses.lista(t_alkalmazottak)
kereses.lista10(t_alkalmazottak)

file.save_json ("alkalmazottak.json", t_alkalmazottak)
