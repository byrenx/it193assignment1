

class CsvParser:

    def __init__(self, input_file, output_file):
        self.inf = input_file
        self.outf = output_file

    def parseInputFile(self):
        field_name = []
        row_inputs = []
        fin = open(self.inf)

        first = True
        for line in fin:
            if(first == True):
                first = False
                field_name = line.strip().split(",")
            else:
                row_inputs.append(line.strip().split(","))
        fin.close()    

        return (field_name, row_inputs)
            
    def createInsertStmt(self, field):
        str_init_stmt = "INSERT INTO sample("
        str_init_stmt += ', '.join(field) + ')'

        return str_init_stmt
        
    def createValuesInsert(self, rows):
        return ' VALUES(' + ', '.join(rows) + ');'
        
           
    def convertToInsert(self):
        data_inputs = self.parseInputFile();
        str_output = ""
        str_temp_stmt = self.createInsertStmt(data_inputs[0])

        for row in data_inputs[1]:
            self.createValuesInsert(row)
            str_output += str_temp_stmt + self.createValuesInsert(row)
            str_output += "\n"

        return str_output
            
      
    def writeToOutputFile(self, str_output):
        outw = open(self.outf, "w")
        outw.write(str_output)
        outw.close()

    def parse_convert_writeToFile(self):
        self.writeToOutputFile(self.convertToInsert())
        
    



if __name__=='__main__':
    samp = CsvParser("sample.csv", "sample.sql")
    samp.parse_convert_writeToFile()
    
