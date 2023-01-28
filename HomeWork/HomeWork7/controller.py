import view
import process
import log

def button_click():
    rezhim=view.inp_mod()
    if rezhim.lower()=='импорт':
        surname=view.inp_import()
        res_search=process.search(surname)
        if isinstance(res_search, str):
            view.view_import_no()
        else: 
            view.view_import(res_search)
        log.log(rezhim, surname)
    if rezhim.lower()=='экспорт':
        result=view.inp_export()
        process.export(result)
        log.log(rezhim, result[1])