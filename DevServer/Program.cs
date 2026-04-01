using Microsoft.Extensions.FileProviders;

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

var siteRoot = Path.GetFullPath(Path.Combine(app.Environment.ContentRootPath, ".."));
var fileProvider = new PhysicalFileProvider(siteRoot);

app.UseDefaultFiles(new DefaultFilesOptions { FileProvider = fileProvider });
app.UseStaticFiles(new StaticFileOptions { FileProvider = fileProvider });

app.Run();
