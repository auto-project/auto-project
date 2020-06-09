#ifndef DIAGLIB_HPP
#define DIAGLIB_HPP

#include <string>

/* Description: Library API used for storing DTC codes in file system
 * Input params: id
 * Output params: -
 * Use: string containing DTC identifier
 * 		format of id must be [Capital letter][Four digits]
 * 		e.g. U0021
 */
extern void Diagnostic_Raise_DTC(std::string id);

/* Description: Library API used for clearing all recorded DTCs
 * Input params: -
 * Output params: -
 * Use: -
 */
extern void Diagnostic_Clear_All_DTC();

/* Description: Library API used for reading all recorded DTCs
 * Input params: -
 * Output params: return string
 * Use: return value contains all codes in a single string, separated by new line
 */
extern std::string Diagnostic_Read_All_DTC();

#endif //DIAGLIB_HPP

