<!-- Web Technologies Lab 3 | Author: Javier Pardos | javier.pardos10@e-uvt.ro-->

<!--File to transform XML to HTML-->
<?xml version="1.0" encoding="ISO-8859-1"?>

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <xsl:template match="/">

    <html> 
        <body>
            
            <h2>My database collection</h2>
            <table border="1">

                <tr>

                    <th style="text-align:center; background-color: #FFD700">Name</th>
                    <th style="text-align:center; background-color: #FFD700">Date</th>
                    <th style="text-align:center; background-color: #FFD700">URI</th>
                    <th style="text-align:center; background-color: #FFD700">Type</th>

                    <th style="text-align:center; background-color: lightblue">Subrecord 1</th>
                    <th style="text-align:center; background-color: lightblue">Subrecord 2</th>
                    <th style="text-align:center; background-color: lightblue">Subrecord 3</th>

                </tr>

                
                <xsl:for-each select="db/record">

                    <tr>
                        <!--Recover each attribute from the 'record' element to be shown-->
                        <td style="text-align:center"><xsl:value-of select="@name"/></td>
                        <td style="text-align:center"><xsl:value-of select="@date"/></td>
                        <td style="text-align:center"><xsl:value-of select="@uri"/></td>
                        <td style="text-align:center"><xsl:value-of select="@type"/></td>

                        <!--Show the value of 'subrecords' elements-->
                        <td style="text-align:center"><xsl:value-of select="subrecord1"/></td>
                        <td style="text-align:center"><xsl:value-of select="subrecord2"/></td>
                        <td style="text-align:center"><xsl:value-of select="subrecord3"/></td>
                    </tr>

                </xsl:for-each>
            </table>
        </body>
    </html>

    </xsl:template>
</xsl:stylesheet>

